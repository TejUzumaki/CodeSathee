const roasts = [
    "Your code has more bugs than features.",
    "CSS Centering? Good luck.",
    "Using `var` in 2024? Bold move.",
    "That commit message says 'fix' again."
];
let lastIdx = -1;

export function generate() {
    const output = document.getElementById('roast-output');
    const wrapper = output.parentElement;
    
    let idx;
    do { idx = Math.floor(Math.random() * roasts.length); } 
    while(idx === lastIdx);
    lastIdx = idx;
    
    output.innerText = roasts[idx];
    wrapper.classList.add('visible');
}