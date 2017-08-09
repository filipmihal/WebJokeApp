$(document).ready(function () {
    var $wrapper = $('.like-emo');

$wrapper.find('.reaction-btn').sort(function (a, b) {
    return +a.dataset.num - +b.dataset.num;
})
.appendTo( $wrapper );

    $(".reaction").on("click", function () { // like click
        var data_reaction = $(this).attr("data-reaction");
        var reaction = data_reaction.toLowerCase();
        var txt_reaction = "";
        switch (reaction) {
            case "unamused":
                txt_reaction = "Zlé";
                break;
            case "neutral":
                txt_reaction = "Nuda";
                break;
            case "smile":
                txt_reaction = "Vtipné";
                break;
            case "funny":
                txt_reaction = "Super!";
                break;
            default:
                txt_reaction = "Ohodnotiť";
        }
        $(".like-details").html("");
        $(".like-btn-emo").removeClass().addClass('like-btn-emo').addClass('like-btn-' + data_reaction.toLowerCase());
        $(".like-btn-text").text(txt_reaction).removeClass().addClass('like-btn-text').addClass('like-btn-text-' + data_reaction.toLowerCase()).addClass("active");
    });

    $(".like-btn-text").on("click", function () {
        if ($(this).hasClass("active")) {
            $(".like-btn-text").text("Ohodnotiť").removeClass();
            $(".like-btn-emo").removeClass().addClass('like-btn-emo').addClass("like-btn-default");
            $(".like-details").html("");

        }
    })


});