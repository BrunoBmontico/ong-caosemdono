// SLIDER DE IMAGENS 
$(document).ready(function(){
    $('.slider').slick({
        infinite: false,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        dots: true,
        arrows: false
    });
});

// MENU FLUTUANTE
$(document).ready(function(){
    $(window).on('scroll', function(){
        
        const menu = $('#menu_container');
        if(window.scrollY > 300){

            menu.css('position','fixed');
            menu.css('margin-top', '10rem');

        } else if (window.scrollY < 300) {

            menu.css('position', 'absolute');
            menu.css('margin-top', '30rem');

        }
    });
});