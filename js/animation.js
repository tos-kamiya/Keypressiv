'use strict';

var renew = function (elm) {
    var newone = elm.cloneNode(true);
    elm.parentNode.replaceChild(newone, elm);
    return newone;
};

var animation_under_going = false;

var set_sliding = function (inId, outId, LRTB, doStacking) {
    var elm1 = document.getElementById(inId);
    var newone1 = renew(elm1);
    var elm2 = document.getElementById(outId);
    var newone2 = renew(elm2);
    if (! animation_under_going && (LRTB === "left" || LRTB === "right" || LRTB === "top" || LRTB === "bottom")) {
        animation_under_going = true;
        $(newone1).removeClass().css("display", "inherit").addClass(LRTB + "-slide-in");
        if (!doStacking)
            $(newone2).addClass(LRTB + "-slide-out");
        setTimeout(function () {
            $(newone1).removeClass();
            $(newone2).removeClass().css("display", "none");
            animation_under_going = false;
        }, 500);
    } else {
        $(newone1).removeClass().css("display", "inherit");
        $(newone2).removeClass().css("display", "none");
    }
};
