function setFooterStyle() {
    if ($(document).height() <= $(window).height()) {
        $("#footer").addClass("footer");
    } else {
        $("#footer").removeClass("footer");
    }

    $("#footer").css("visibility", "visible");
}

$(document).ready(function () {
    setFooterStyle();
});

window.addEventListener("resize", setFooterStyle);