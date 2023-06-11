
var ws

function sendMessage(event) {
    var input = document.getElementById("messageText")
    // var message = document.createElement('li')
    // var content = document.createTextNode(input.value)
    // message.appendChild(content);
    // messages.appendChild(message);
    ws.send(input.value);

    input.value = ''
    event.preventDefault()
}

function processMessage(event) {
    var messages = document.getElementById('messages')
    var message = document.createElement('li')
    var content = document.createTextNode(event.data)
    message.appendChild(content);
    messages.appendChild(message);
}

function showForm(event) {
    event.preventDefault()

    var clientName = document.getElementById("clientname").value;
    console.log(clientName)
    var clientID = Date.now();
    ws = new WebSocket(`ws://localhost:8000/ws/${clientName}`);

    ws.onmessage = processMessage;

    var button = document.getElementById("connect");
    var form = document.getElementById("form");
    button.style.display = "none";
    form.style.display = "block";
}
