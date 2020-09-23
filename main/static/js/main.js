$(document).ready(function () {
    var csrf_token = $("input[name=csrfmiddlewaretoken]")
    $("body").on("click", ".Download_button", function () {
        var delete_button = $(this)
        // $.ajax({
        //     url: '/download-files',
        //     type: 'POST',
        //     data: {
        //         yt_itag: $("#download_select option:selected").val(),
        //         csrfmiddlewaretoken: csrf_token.val(),
        //     },
        //     success: function (data, textStatus, request) {
        //         window.location = data

        //     }
        // });

        console.log($("#download_select option:selected").val())
        var form = $('<form action="/download-files" method="POST">' +
            '<input type="hidden" name="csrfmiddlewaretoken" value="' + csrf_token.val() + '">' +
            '<input type="hidden" name="yt_itag" value="' + $("#download_select option:selected").val() + '">' +
            '</form>');
        $(document.body).append(form);
        $(form).submit()

        // $.post("/download-files", {
        //     "yt_itag": $("#download_select option:selected").val(),
        //     "csrfmiddlewaretoken": csrf_token.val()
        // })
        //     .done(function (response) {
        //         var w = window.open('about:blank');
        //         w.document.open();
        //         w.document.write($.parseHTML(response));
        //         w.document.close();
        //     })

    });
    $(".url-field").on("click", ".my_button", function () {
        if (!isNullOrWhitespace($(".url_to_short").val())) {
            $.ajax({
                url: '/',
                type: 'POST',

                data: {
                    full_url: $(".url_to_short").val(),
                    csrfmiddlewaretoken: csrf_token.val(),
                },
                success: function (response) {
                    if (!response.error) {
                        $(".result-url").html("<p>Your short link:</p>\
                        <h4>"+ response.shorten_url + "</h4>")
                    }
                    else {
                        $(".result-url").html("<p>" + response.error + "</p>")
                    }


                }
            });
        }

    });

    function isNullOrWhitespace(input) {
        return !input || !input.trim();
    }
});