function add_joke_reaction(joke_id, reaction_id) {
    var data = {
        joke_id : joke_id,
        reaction_id : reaction_id
    }
    $.ajax({
            url: '/vtipy/rate-joke',
            data: data,
            type: 'POST',
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    }