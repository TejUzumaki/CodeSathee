export function encode() {
    const input = document.getElementById('b64-input').value;
    const output = document.getElementById('b64-output');
    try {
        output.innerText = btoa(input);
        output.parentElement.classList.add('visible');
    } catch(e) { output.innerText = "Encoding failed"; }
}

export function decode() {
    const input = document.getElementById('b64-input').value;
    const output = document.getElementById('b64-output');
    try {
        output.innerText = atob(input);
        output.parentElement.classList.add('visible');
    } catch(e) { output.innerText = "Invalid Base64 string"; }
}