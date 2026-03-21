export function generate() {
    const len = document.getElementById('pwd-length').value;
    const useSym = document.getElementById('pwd-symbols').checked;
    const useNum = document.getElementById('pwd-numbers').checked;
    const output = document.getElementById('pwd-output');
    
    const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const nums = "0123456789";
    const syms = "!@#$%^&*()_+~`|}{[]:;?><,./-=";
    
    let dict = chars;
    if (useNum) dict += nums;
    if (useSym) dict += syms;
    
    let pass = "";
    for(let i=0; i<len; i++) {
        pass += dict.charAt(Math.floor(Math.random() * dict.length));
    }
    
    output.innerText = pass;
    output.parentElement.classList.add('visible');
}