var renew = function(elm) {
    var newone = elm.cloneNode(true);
    elm.parentNode.replaceChild(newone, elm);
    return newone;
}
var set_sliding_animation = function(inId, outId, LR) {
    var elm1 = document.getElementById(inId);
    var newone1 = renew(elm1);
    $(newone1).removeClass().css("display", "inherit").addClass(LR + "-slide-in");
    var elm2 = document.getElementById(outId);
    var newone2 = renew(elm2);
    $(newone2).addClass(LR + "-slide-out");
    setTimeout(function() {
        $(newone1).removeClass();
        $(newone2).removeClass().css("display", "none");
    }, 500);
}
var set_no_animation = function(inId, outId) {
    var elm1 = document.getElementById(inId);
    var newone1 = renew(elm1);
    $(newone1).removeClass().css("display", "inherit");
    var elm2 = document.getElementById(outId);
    var newone2 = renew(elm2);
    $(newone2).removeClass().css("display", "none");
}

