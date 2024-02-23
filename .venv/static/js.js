// Example AJAX request with jQuery

function askKoded(question) {
    $.ajax({
        url: '/ask-koded',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ question: question }),
        success: function(response) {
            console.log(response);
            // Update the UI with Koded's response
        },
        error: function(error) {
            console.log(error);
        }
    });
}
