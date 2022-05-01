$(document).ready(function(){
    var form = $('.code-form');
    form.on('submit', function(e){
        var code = $("[name='code']")
        var url_block = $('.code-form');
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        var data ={};
        data["csrfmiddlewaretoken"] = csrf_token;
        data.code = code
        var url = url_block.attr("action");
         $.ajax({
                  url: url,
                  type: 'POST',
                  data: data,
                  cache: true,
                  success: function (data) {
                     console.log("OK");
                 },
                 error:function(){
                    console.log('error');
                 }
            });

    )}
)}
