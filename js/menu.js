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