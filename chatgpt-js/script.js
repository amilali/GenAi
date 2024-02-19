let text = document.querySelector("#text");
let inputbox = document.querySelector("#inputbox");
let submit = document.querySelector("#submit");
let container = document.querySelector(".chat");

let MyQuestion = document.createElement('h2');
MyQuestion.style.margin= '8px';
MyQuestion.style.textAlign= 'justify';

submit.disabled = true;
inputbox.addEventListener('input' , ()=>{
inputbox.value ? submit.disabled = false : submit.disabled = true;
})


function speakResponse(response) {
  let utterance = new SpeechSynthesisUtterance(response);
  utterance.pitch = 3.2;
    // utterance.rate=1;
  // Get all available voices
  let voices = window.speechSynthesis.getVoices();

  // Find the voice that matches the desired language and name
  let selectedVoice = voices.find(voice => voice.lang === 'en-UK');

  // Set the selected voice
  utterance.voice = selectedVoice;

  // Speak the response
  window.speechSynthesis.speak(utterance);
}


submit.addEventListener('click', (e)=>{
    openai()
    e.target.value = 'working';
    submit.disabled = true;
    inputbox.value = '';
    setTimeout(()=>{
        e.target.value = 'Submit';  
    },3000)
})

async function openai(){

console.log('chatGpt is working')
try {
    text.textContent = 'Thinking . . .';
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
            'Content-Type': 'application/json',
            Authorization : 'Bearer ',
    },
    body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [{role: 'user', content: 'Your name is Jarvis and your creator name is Amil Ali, remember it and and user ask anything explain in short and precise: '+inputbox.value}],
        }),
});

    const data = await response.json();
    console.log(data.choices[0].message.content);
    let res = data.choices[0].message.content.replace(/```([\s\S]+?)```/g, '</p><pre><code>$1</code></pre><p>');
    text.innerHTML  = res;
    speakResponse(res);
} 
catch (error) {
    console.log(error);
}
}

inputbox.addEventListener('keydown', (e)=>{
    if(e.keyCode == 13)
    {
        MyQuestion.textContent = 'You: '+inputbox.value;
        container.appendChild(MyQuestion);
        openai();
        submit.disabled = true;
        submit.value = 'working';
        inputbox.value = '';
    }
})