var bindHashchange = function(handler) {
    $(window).on('hashchange', handler);
};

var setTitle = function(title) {
    $(document).attr("title", title);
};

var getHash = function() {
    if (location.hash)
        return location.hash.substr(1);
    return null;
};

var setHash = function(s) {
    location.hash = s;
};

