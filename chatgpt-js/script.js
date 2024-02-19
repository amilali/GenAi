let text = document.querySelector("#text");
let inputbox = document.querySelector("#inputbox");
let submit = document.querySelector("#submit");


submit.disabled = true;
inputbox.addEventListener('input' , ()=>{
inputbox.value ? submit.disabled = false : submit.disabled = true;
})

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
    text.textContent = 'Working...';
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
            'Content-Type': 'application/json',
            Authorization : 'Bearer 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',
    },
    body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [{role: 'user', content: inputbox.value}],
        }),
});

    const data = await response.json();
    console.log(data.choices[0].message.content);
    text.textContent = data.choices[0].message.content;
} 
catch (error) {
    console.log(error);
}

}

inputbox.addEventListener('keydown', (e)=>{
    if(e.keyCode == 13)
    {
        openai();
        submit.disabled = true;
        submit.value = 'working';
        inputbox.value = '';
    }
})