$(".reaction").on("click", function () {
    var $element = $(this);
    var data_reaction = $element.attr("data-reaction");
    var joke_id = Number($element.attr("data-jokeid"));
    var reaction_id = Number($element.attr("data-reactionid"));
    var current_reactions = Number($element.parents('.joke-reaction').prev().find(".like-details").text());

    var txt_reaction = "";
    switch (reaction_id) {
        case 1:
            txt_reaction = "Zlé";
            break;
        case 2:
            txt_reaction = "Nuda";
            break;
        case 3:
            txt_reaction = "Vtipné";
            break;
        case 4:
            txt_reaction = "Super!";
            break;
        default:
            txt_reaction = "Ohodnotiť";
    }
    var reaction_order = "";
    $element.parents('.joke-reaction').find(".like-btn-text").text(txt_reaction).addClass('like-btn-text-' + data_reaction.toLowerCase()).addClass("active");
    $element.parents('.joke-reaction').find(".like-btn-emo").removeClass().addClass('like-btn-emo').addClass('like-btn-' + data_reaction.toLowerCase());
    current_reactions += 1;
    $element.parents('.joke-reaction').prev().find(".like-details").text(current_reactions);

    var data = {
        joke_id: joke_id,
        reaction_id: reaction_id
    }
    $.ajax({
        url: '/vtipy/rate-joke',
        data: data,
        type: 'POST',
        dataType: "json",
        success: function (response) {
            console.log(response);
            if (response.status) {
                response.data.forEach(function (element) {
                    reaction_order += "<span class='reaction-btn like-btn-" + element[0] + "' rel='tooltip'  title='" + element[1] + "' data-placement='top'></span>";
                }, this);
                $element.parents('.joke-reaction').prev().find(".like-emo").html(reaction_order);
            }
        },
        error: function (error) {
            console.log(error);
        }
    });
});

$(".like-btn-text").on("click", function () {
    if ($(this).hasClass("active")) {
        $(".like-btn-text").text("Ohodnotiť").removeClass();
        $(".like-btn-emo").removeClass().addClass('like-btn-emo').addClass("like-btn-default");
    }
});