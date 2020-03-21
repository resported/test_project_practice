$(document).ready(function () {
    var form = $('.buy-product-form');
    form.on('submit', function (e) {
        e.preventDefault();
        var numb = $('.form-number').val();
        var btn_buy = $('.btn-buy');
        var product_slug = btn_buy.data('product_slug');
        var product_title = btn_buy.data('product_title');
        var product_price = btn_buy.data('product_price');
        console.log(product_title)

        var data = {};
        data.product_slug = product_slug;
        data.numb = numb;
        var csrf_token = $('.buy-product-form [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        console.log(data);

        var url = form.attr('action');
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cashe: true,
            success: function (data) {
                console.log('READY!');
            },
            error: function () {
                console.log('ERROR!')
            }
        })


        $('.basket-icon-dropdown').append('<li>' + product_title + '</li>');
        
    });
})