const dict = {
    'api': 'Waiter taking orders to kitchen.',
    'dom': 'Tree structure of the webpage.',
    'closure': 'Function + its lexical environment.',
    'callback': 'Function passed as argument.',
    'promise': 'Future value placeholder.'
};

export function explain() {
    const input = document.getElementById('eli5-input').value.toLowerCase();
    const output = document.getElementById('eli5-output');
    const wrapper = output.parentElement;

    if(!input) return;
    
    let result = dict[input];
    if (!result) result = `No definition for "${input}". Try API, DOM, Closure.`;
    
    output.innerText = result;
    wrapper.classList.add('visible');
}