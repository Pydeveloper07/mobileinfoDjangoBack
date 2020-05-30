// Preloader
jQuery(window).load(function () {
    function Preloader() {
        $('#load').delay(500).fadeOut('slow');
        $('#preloader').delay(900).fadeOut('slow');
        $('body').delay(900).css({
            'overflow': 'visible',
        });
    }
    if (!sessionStorage.getItem('doNotShow')) {
        sessionStorage.setItem('doNotShow', true);
        Preloader();
    } else {
        $('#load, #preloader').hide();
    }
    
});
jQuery(document).ready(function(){
    try {
        var sideMenuHeight = $(window).height() - parseInt($('.side-menu').css('margin-top').substring(0, $('.side-menu').css('margin-top').length - 1));
        var rightMenuHeight = $(window).height() - parseInt($('.right-menu').css('margin-top').substring(0, $('.right-menu').css('margin-top').length - 1));
        $('.side-menu').css({
            'max-height': sideMenuHeight + 'px',
        });
        $('.right-menu').css({
            'max-height': rightMenuHeight + 'px',
        });
        $(window).resize(function () {
            var sideMenuHeight = $(window).height() - parseInt($('.side-menu').css('margin-top').substring(0, $('.side-menu').css('margin-top').length - 1));
            $('.side-menu').css({
                'max-height': sideMenuHeight + 'px',
            })
            var rightMenuHeight = $(window).height() - parseInt($('.right-menu').css('margin-top').substring(0, $('.right-menu').css('margin-top').length - 1));
            $('.right-menu').css({
                'max-height': rightMenuHeight + 'px',
            })
        });
    } catch (error) {
        console.log(error.message);
    }
    try {
        $('#show-comments-btn').click(function(){
            $(".comment-body").fadeIn(500);
        });
    } catch (error) {
        console.log(error.message);
    }
    if ($('#messages')) {
        $('#messages').fadeOut(5000);
    }
    var elem = $('.custom-nav');
    $(window).resize(function(){
        var elem = $('.custom-nav');
        var css = {
            'background': 'black',
            'border-color': 'red',
            'box-shadow': '-2px 0 8px white',
        };
        elem.css(css);
    });
    $(window).scroll(function(){
        if ($(window).scrollTop() < 10){
            var css = {
                'background': 'transparent',
                'border-color': 'transparent',
                'box-shadow': 'none',
            };
        }
        else{
            var css = {
                'background': 'black',
                'border-color': 'red',
                'box-shadow': '-2px 0 8px white',
            };
        }
        elem.css(css);
    });
});