
$(document).ready(function () {
    if ($(document).height() <= $(window).height()) {
        $("#footer").addClass("footer");
    }
    
    $("#footer").css("visibility", "visible");
});