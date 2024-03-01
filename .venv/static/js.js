function askKoded(question) {
    $.ajax({
        url: '/ask-koded',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ question: question }),
        success: function(response) {
            // Update the UI with Koded's response
            $('#chat').append('<p>' + response.answer + '</p>'); // or however your response structure looks like
            $('#input').val(''); // clear the input field for new question
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function submitQuestion() {
    var question = $('#input').val();
    askKoded(question);
}

// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function() {
    // Get the chat container and input elements
    var chatContainer = document.getElementById("chat-container");
    var userInput = document.getElementById("user-input");

    // Function to handle sending user input and displaying chat messages
    function sendMessage() {
        // Get the user input
        var message = userInput.value.trim();

        // Clear the input field
        userInput.value = "";

        // Display the user message in the chat container
        var userMessageElement = document.createElement("div");
