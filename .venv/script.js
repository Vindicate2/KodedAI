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
