let lastUUID = '';

export function generate() {
    const output = document.getElementById('uuid-output');
    const wrapper = output.parentElement;
    
    let uuid = 'fallback-' + Math.random().toString(36).substr(2);
    if (typeof crypto !== 'undefined' && crypto.randomUUID) {
        uuid = crypto.randomUUID();
    }

    // Prevent duplicates
    while(uuid === lastUUID) {
        uuid = crypto.randomUUID ? crypto.randomUUID() : 'fallback-' + Math.random();
    }
    lastUUID = uuid;

    output.innerText = uuid;
    wrapper.classList.add('visible');
}