export function format() {
    const input = document.getElementById('json-input').value;
    const output = document.getElementById('json-output');
    const wrapper = output.parentElement;
    
    try {
        const obj = JSON.parse(input);
        output.innerText = JSON.stringify(obj, null, 4);
        wrapper.classList.add('visible');
    } catch (e) {
        output.innerText = "⚠️ Invalid JSON: " + e.message;
        wrapper.classList.add('visible');
    }
}