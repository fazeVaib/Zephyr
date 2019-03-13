$(function() {
    var elem = $.jInvertScroll(['.scroll'],        // an array containing the selector(s) for the elements you want to animate
        {
            // height: 6000,                   // optional: define the height the user can scroll, otherwise the overall length will be taken as scrollable height
            onScroll: function(percent) {   //optional: callback function that will be called when the user scrolls down, useful for animating other things on the page
                console.log(percent);
            }
        });
    $(window).resize(function() {
        if ($(window).width() <= 768) {
            elem.destroy();
        }
        else {
            elem.reinitialize();
        }
    });
});