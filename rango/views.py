from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rango.models import Category, Page, UserProfile
from rango.forms import UserForm, UserProfileForm, PageForm, CategoryForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
import django_team_project.settings as settings
import os

def index(request):
    category_list = Category.objects.order_by('-likes')[:3]
    movie_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['movies'] = movie_list
    visitor_cookie_handler(request)
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
        paginator = Paginator(context_dict['pages'], 3)

        page = request.GET.get('page')
        # using paginator
        try:
            topics = paginator.page(page)
        # if the page parameter from url is not int
        except PageNotAnInteger:
            topics = paginator.page(1)
        # if the url does not include page request
        except EmptyPage:
            topics = paginator.page(paginator.num_pages)
        context_dict['topics'] = topics
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request, 'rango/category.html', context=context_dict)

# using paginator to paging the movies
def process_paginator(request, movie_list):
    paginator = Paginator(movie_list, 1)
    try:
        page_number = int(request.GET.get('page', '1'))
        page = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        page = paginator.page(1)
    return page

@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rango:index'))
        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})

@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None

    if category is None:
        return redirect(reverse('rango:index'))

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}

    return render(request, 'rango/add_page.html', context=context_dict)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango/register.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rango:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rango/login.html')

@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rango:index'))

@login_required
def update_picture(request):
    message = 'Please try again!'
    if request.method == 'POST':
        # get the file from request
        pic_file = request.FILES.get('pic_file')
        user_profile = UserProfile.objects.get(user=request.user)
        # get the new url for the picture
        # it could be having no picture or having picture already
        try:
            pic_path = user_profile.picture.url.split('/')
            current_pic_path = pic_path[-2:]
            current_pic_path[-1] = request.POST.get('pic_name')
        except:
            current_pic_path = []
            current_pic_path.append('profile_images')
            current_pic_path.append(request.POST.get('pic_name'))
        # print(current_pic_path)
        # new path
        new_pic_path = '/'.join(current_pic_path)
        new_pic_url = settings.MEDIA_DIR + '/' + new_pic_path
        # print(new_pic_path)
        # write the file
        if pic_file:
            # pic_path = os.path.join(os.path.join(MEDIA_DIR, 'profile_images'), pic_file)
            with open(new_pic_url, 'wb') as f:
                for chunk in pic_file.chunks():
                    f.write(chunk)
        # save the file
        user_profile.picture = new_pic_path
        user_profile.save()
        message = 'Your picture has been updated successfully!'
    return render(request, 'rango/profile.html', context={'upload_result':message})

# profile view
@login_required
def user_profile(request):
    # if the user does not exist in the database, it will not let teh user access this page
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except:
        user_profile = None

    # if user has not sign in, jump to login page
    if user_profile is None:
        return redirect(reverse('rango:login'))

    username = user_profile.user.username
    email = user_profile.user.email
    picture = user_profile.picture
    # let the user access this page with username and picture of user
    return render(request, 'rango/profile.html', context={'username': username,
                                                   'picture': picture,'email':email})

# movie page view
def show_page(request, movie_id):
    context_dict = {}
    # get data of movie from database
    try:
        movie = Page.objects.get(id=movie_id)

        context_dict['movie'] = movie
        print(context_dict)
    # if this movie does not exist, let the html deal with it
    except Category.DoesNotExist:
        context_dict['movie'] = None

    return render(request, 'rango/movie.html', context=context_dict)

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits