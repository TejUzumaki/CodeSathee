export function test() {
    const patternStr = document.getElementById('regex-pattern').value;
    const flags = document.getElementById('regex-flags').value;
    const text = document.getElementById('regex-test-string').value;
    const output = document.getElementById('regex-output');
    
    if(!patternStr) return;
    
    try {
        const regex = new RegExp(patternStr, flags);
        const matches = text.match(regex);
        
        if (matches) {
            output.innerText = `Matches Found: ${matches.length}\nFirst: ${matches[0]}`;
        } else {
            output.innerText = "No matches found.";
        }
        output.parentElement.classList.add('visible');
    } catch (e) {
        output.innerText = "Invalid Regex Pattern.";
        output.parentElement.classList.add('visible');
    }
}