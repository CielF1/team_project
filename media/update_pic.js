layui.use('upload', function(){
    // using the upload method of layui 
    var $ = layui.jquery
    ,upload = layui.upload;
    var token_value = $('[name="csrfmiddlewaretoken"]').val();
    var uploadInst = upload.render({
        // indicate the element
        elem: '#pic_upload'     
        // indicate the url to upload the picture
        ,url: "{% url 'rango:update_pic' %}"
        ,accept: 'file'
        ,auto: false        
        // ,bindAction: '#formSubmit'   
        // when choose the image
        ,choose:function(obj){
            obj.preview(function(index, file, result){
                $('#user_pic').attr('src', result); 
            });
            
        }
        // when finish the upload
        ,done: function(res){
            if(res.code > 0){
                return layer.msg('failed');
            }
            $('#show_upload_result').html('sucess!')
        }
    });
    }); 
    layui.use(['jquery','form'], function(){
    var $ = layui.jquery 
    ,form = layui.form;
    // var token_value = $('[name="csrfmiddlewaretoken"]').val();
    // fit the layui method to use form
    form.on('submit(btnSubmit)', function(data){
        // send POST manually
        event.preventDefault();
        var pic_file = $('#pic_upload')[0].files[0];
        // read the picture file and analysis
        var file_reader = new FileReader();
        file_reader.readAsDataURL(pic_file);
        file_reader.onload = function(e){
            var form_data = new FormData(); 
            // add attributes into data
            form_data.append('pic_name', pic_file.name);
            form_data.append('pic_file', pic_file);
            form_data.append('csrfmiddlewaretoken', '{{ csrf_token }}');
            // alert(form_data);
            // send POST ajax request
            $.ajax({
                url: "../update_pic/",
                type: 'POST',
                data: form_data,
                processData: false,
                contentType: false,
                sucess: function(data, status){
                    alert(data);
                }
            });
            return false;
        }
        
    }); 
}); 