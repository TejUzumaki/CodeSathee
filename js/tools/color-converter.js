export function convert() {
    const hex = document.getElementById('hex-input').value;
    const output = document.getElementById('color-output');
    const preview = document.getElementById('color-preview');
    
    preview.style.backgroundColor = hex;
    
    let r=0, g=0, b=0;
    if (hex.length === 4) {
        r = parseInt(hex[1]+hex[1], 16);
        g = parseInt(hex[2]+hex[2], 16);
        b = parseInt(hex[3]+hex[3], 16);
    } else if (hex.length === 7) {
        r = parseInt(hex.substr(1,2), 16);
        g = parseInt(hex.substr(3,2), 16);
        b = parseInt(hex.substr(5,2), 16);
    }
    
    output.innerText = `rgb(${r}, ${g}, ${b})`;
}