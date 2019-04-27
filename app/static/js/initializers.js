document.addEventListener('DOMContentLoaded', function () {
    M.Carousel.init(document.querySelectorAll('.carousel'),{fullWidth: true});
    M.Sidenav.init(document.querySelectorAll('.sidenav'));
    M.Collapsible.init(document.querySelectorAll('.collapsible'));
    M.Parallax.init(document.querySelectorAll('.parallax'));
});
