export function translate() {
    const input = document.getElementById('err-input').value.toLowerCase();
    const output = document.getElementById('err-output');
    const wrapper = output.parentElement;
    
    if(!input.trim()) return;

    const map = {
        'undefined': 'Variable used but not defined.',
        'null': 'Value is explicitly empty.',
        '404': 'Resource not found.',
        'syntax error': 'Typo in code structure.',
        'cors': 'Server blocked request due to security.',
        'network error': 'Connection failed.',
        '500': 'Server crashed.'
    };

    let result = "Generic error. Check logic.";
    for (const key in map) {
        if (input.includes(key)) {
            result = map[key];
            break;
        }
    }

    output.innerText = result;
    wrapper.classList.add('visible');
}