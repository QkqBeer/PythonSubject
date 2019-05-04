$(function () {
    $("#focusSlides").slides({
        preload: !0,
        preloadImage: "http://static.weke.com/images/slider-loading.gif",
        effect: "fade",
        crossfade: !0,
        slideSpeed: 350,
        fadeSpeed: 500,
        play: 5e3,
        pause: 2500,
        hoverPause: !0,
        generateNextPrev: !1,
        generatePagination: !0
    })
})