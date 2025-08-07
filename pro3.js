function aler() {
    alert("file coming soon");
}

let msg_view = document.querySelector('.msg');
let send_button = document.querySelector('.sendbutton');
let userName = ''; 
let homelist = []


function showhistory(Rdata, user){
    let msgcont = document.querySelector('.msg')
    msgcont.innerHTML = ''; 
    Rdata.forEach((a)=>{
        if (!(user.includes(a))){
            let uname = document.createElement('h6')
            let txt = document.createElement('h4')
            let box = document.createElement('div')
            Object.assign(uname.style, {
                color: 'gray',
                margin: '2px'
            });
            Object.assign(txt.style, {
                color: 'black',
                margin: '2px',
                
            });
            Object.assign(box.style, {
                background: 'none',
                margin: '5px',
                border: '1px solid black'
                
            });
            uname.textContent = a.name
            txt.textContent = a.message
            box.appendChild(uname)
            box.appendChild(txt)
            document.querySelector('.msg').appendChild(box)
            homelist.push(a)
        }
        msgcont.scrollTop = msgcont.scrollHeight;
    });
}

async function receiver() {
    try {
        let response = await fetch('https://server-4zvw.onrender.com');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        let newData = await response.json(); 
        console.log('this is it',typeof(newData));
        console.log(newData)
        showhistory(newData, homelist)
    } catch (error) {
        console.error("GET Error:", error);
    }
}

receiver();


setInterval(receiver, 2000); 
let isNameEntered = false;


async function sender() {  
    let input = document.getElementById('inp').value.trim();

    if (input && !isNameEntered) {
        isNameEntered = true;
        userName = input;
        document.getElementById('inp').placeholder = 'Type...';
        document.getElementById('inp').value = '';
        document.querySelector('.sendbutton').textContent = 'Send';
        return
    }
    else if (!input && !isNameEntered) {
        alert('Please enter your name');
        return
    }
    else {
        if (input) {
            try {
                const response = await fetch('https://server-4zvw.onrender.com', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        name: userName, 
                        message: input
                    }),
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const result = await response.json();
                console.log("Post success", result);


                document.getElementById('inp').value = '';


                receiver();
            } catch (error) {
                console.error('POST error', error);
            }
            document.getElementById('inp').placeholder = 'Type...'
            document.getElementById('inp').value = ''
        }
    }
}

document.querySelector('.sendbutton').addEventListener('click', sender);
document.getElementById('inp').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sender();
});
