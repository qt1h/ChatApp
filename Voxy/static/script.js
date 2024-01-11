document.addEventListener("DOMContentLoaded", function () {
    const changerTheme = document.getElementById("bouton-changement-theme");
    const body = document.body;

    changerTheme.addEventListener("click", function () {
        body.classList.toggle("theme-sombre");
        updateBoutonTheme();
    });

    function updateBoutonTheme() {
        const iconeTheme = document.getElementById("icone-theme");
        const estModeSombre = body.classList.contains("theme-sombre");
        iconeTheme.className = estModeSombre ? "fas fa-sun" : "fas fa-moon";
    }

    updateBoutonTheme();
});
// script.js

const chatSocket = new WebSocket(
    "chatrooms://" + window.location.host +
    "/chatrooms/chatroom/" + document.body.dataset.chatroomId + "/"
);

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);

    // Ajoutez votre logique pour afficher le message en temps réel ici
    const messageList = document.querySelector('.messages-list');

    const messageElement = document.createElement('div');
    messageElement.className = 'messages';
    messageElement.innerHTML = `<p><strong>${data.username}</strong>: ${data.message}</p>`;
    messageList.appendChild(messageElement);
};

chatSocket.onclose = function (e) {
    console.error("WebSocket closed unexpectedly");
};

// Logique pour envoyer un message via WebSocket
const messageInput = document.querySelector('.saisie-message input');
const sendButton = document.querySelector('#bouton-envoi');

sendButton.addEventListener('click', function () {
    const messageContent = messageInput.value.trim();
    if (messageContent !== '') {
        const messageData = {
            message: messageContent,
            chatroom_id: document.body.dataset.chatroomId,
        };

        chatSocket.send(JSON.stringify(messageData));
        messageInput.value = ''; // Efface le champ d'entrée après l'envoi
    }
});