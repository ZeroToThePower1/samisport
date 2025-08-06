// Global variables
const API_URL = "https://server-4zvw.onrender.com";
let msg_view = document.querySelector('.msg');
let send_button = document.querySelector('.sendbutton');
let userName = '';
let messageHistory = []; // Renamed from homelist for clarity
let isNameEntered = false;

function aler() {
    alert("file coming soon");
}
function showhistory(messages) {
    const msgContainer = document.querySelector('.msg');
    msgContainer.innerHTML = '';
    
    messages.forEach(msg => {
        if (!messageHistory.some(m => m.name === msg.name && m.message === msg.message)) {
            const messageElement = document.createElement('div');
            messageElement.className = 'message-box'; // Use CSS classes instead of inline styles
            
            const nameElement = document.createElement('h6');
            nameElement.className = 'message-name';
            nameElement.textContent = msg.name;
            
            const textElement = document.createElement('p'); // Better semantics than h4
            textElement.className = 'message-text';
            textElement.textContent = msg.message;
            
            messageElement.appendChild(nameElement);
            messageElement.appendChild(textElement);
            msgContainer.appendChild(messageElement);
            
            messageHistory.push(msg);
        }
    });
    
    // Auto-scroll to bottom
    msgContainer.scrollTop = msgContainer.scrollHeight;
}

// Optimized receiver function
async function receiver() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const messages = await response.json();
        showhistory(messages);
    } catch (error) {
        console.error("GET Error:", error);
    }
}

// Enhanced sender function
async function sender() {
    const input = document.getElementById('inp').value.trim();
    const inputField = document.getElementById('inp');

    if (!input) {
        if (!isNameEntered) alert('Please enter your name');
        return;
    }

    if (!isNameEntered) {
        isNameEntered = true;
        userName = input;
        inputField.placeholder = 'Type your message...';
        inputField.value = '';
        send_button.textContent = 'Send';
        return;
    }

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: userName, message: input })
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

        inputField.value = '';
        receiver(); // Refresh messages after sending
    } catch (error) {
        console.error('POST error', error);
    }
}

// Event listeners
send_button.addEventListener('click', sender);
document.getElementById('inp').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sender();
});

// Initial setup
receiver();
setInterval(receiver, 2000); // Refresh every 2 seconds
