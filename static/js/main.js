$(document).ready(function () {
    var form = $('.buy-product-form');
    console.log(form);
    form.on('submit', function (e) {
        e.preventDefault();
        var numb = $('.form-number').val();
        var btn_buy = $('.btn-buy');
        var product_slug = btn_buy.data('product_slug');
        var product_title = btn_buy.data('product_title');
        var product_price = btn_buy.data('product_price');
        console.log(product_title)
        $('.basket-icon-dropdown').append('<li>' + product_title + '</li>')
    })


})