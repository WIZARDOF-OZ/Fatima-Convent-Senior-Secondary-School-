//Hide Loading Box (Preloader)
function handlePreloader() {
    if ($('.preloader').length) {
        $('body').addClass('page-loaded');
        $('.preloader').delay(800).fadeOut(300);
    }
}






AOS.init();