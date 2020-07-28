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

// Scroll to top
scrollBtn = document.getElementById("scroll-to-top");

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    scrollBtn.style.display = "block";
  } else {
    scrollBtn.style.display = "none";
  }
}

function scrollToTop() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}