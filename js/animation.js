var renew = function(elm) {
    var newone = elm.cloneNode(true);
    elm.parentNode.replaceChild(newone, elm);
    return newone;
}
var set_sliding = function(inId, outId, LR) {
    var elm1 = document.getElementById(inId);
    var newone1 = renew(elm1);
    var elm2 = document.getElementById(outId);
    var newone2 = renew(elm2);
    if (LR === "left" || LR === "right") {
        $(newone1).removeClass().css("display", "inherit").addClass(LR + "-slide-in");
        $(newone2).addClass(LR + "-slide-out");
        setTimeout(function() {
            $(newone1).removeClass();
            $(newone2).removeClass().css("display", "none");
        }, 500);
    } else {
        $(newone1).removeClass().css("display", "inherit");
        $(newone2).removeClass().css("display", "none");
    }
}

