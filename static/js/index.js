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

window.onscroll = function () { scrollFunction() };

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

// Custom design price

$("#id_product_type").change(function () {
    calculateCustomPrice();
    });
$("#id_description").change(function () {
    calculateCustomPrice();
});


function calculateCustomPrice() {
    customDesignDescription = $('#id_description').val();
    customDesignType = $('#id_product_type').val();

    if (customDesignDescription != "" && customDesignType != "") {
        var price = 0;
        switch (customDesignType) {
            case "ICON":
                price = 75;
                break;
            case "LOGO":
                price = 150;
                break;
            case "POSTER":
                price = 300;
                break;
            default:
                price = 0;
        }
        $("#custom-design-price").text(price.toString() + "EUR");
    } else {
        $("#custom-design-price").text("Specify all fields to get a price");
    }
}