import { Utils } from './utils.js';

// Import all tools dynamically or explicitly (Explicit for clarity in vanilla JS)
import * as ErrorTranslator from './tools/error-translator.js';
import * as JSONFormatter from './tools/json-formatter.js';
import * as UUID from './tools/uuid-generator.js';
import * as ColorConverter from './tools/color-converter.js';
import * as ELI5 from './tools/eli5.js';
import * as Roast from './tools/roast-generator.js';
import * as Base64 from './tools/base64.js';
import * as Password from './tools/password-generator.js';
import * as Regex from './tools/regex-tester.js';

// Namespace for tools
window.Tools = {
    ErrorTranslator,
    JSONFormatter,
    UUID,
    ColorConverter,
    ELI5,
    Roast,
    Base64,
    Password,
    Regex
};

document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initSearch();
    initFavorites();
    
    // Initialize Color Tool Preview
    Tools.ColorConverter.convert();
});

// --- Theme Management ---
function initTheme() {
    const savedTheme = Utils.get('codesathi_theme') || 'dark';
    document.body.className = `${savedTheme}-theme`;
    
    const toggleBtn = document.getElementById('theme-toggle');
    const icon = toggleBtn.querySelector('i');

    toggleBtn.addEventListener('click', () => {
        const isDark = document.body.classList.contains('dark-theme');
        const newTheme = isDark ? 'light' : 'dark';
        
        document.body.className = `${newTheme}-theme`;
        icon.className = isDark ? 'fa-solid fa-moon' : 'fa-solid fa-sun';
        Utils.save('codesathi_theme', newTheme);
    });
}

// --- Tool Search ---
function initSearch() {
    const searchInput = document.getElementById('tool-search');
    searchInput.addEventListener('input', (e) => {
        const term = e.target.value.toLowerCase();
        const cards = document.querySelectorAll('.tool-card');
        
        cards.forEach(card => {
            const tags = card.getAttribute('data-tags').toLowerCase();
            const title = card.querySelector('h3').innerText.toLowerCase();
            
            if (title.includes(term) || tags.includes(term)) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    });
}

// --- Favorites System ---
function initFavorites() {
    let favorites = Utils.get('codesathi_favs') || [];
    
    // Update UI based on saved state
    document.querySelectorAll('.tool-card').forEach(card => {
        const cardId = card.querySelector('h3').innerText; // Using title as ID for simplicity
        const btn = card.querySelector('.fav-btn');
        
        if (favorites.includes(cardId)) {
            btn.classList.add('active');
            btn.querySelector('i').className = 'fa-solid fa-heart';
        }

        btn.addEventListener('click', () => {
            if (favorites.includes(cardId)) {
                favorites = favorites.filter(id => id !== cardId);
                btn.classList.remove('active');
                btn.querySelector('i').className = 'fa-regular fa-heart';
                Utils.showToast('Removed from favorites');
            } else {
                favorites.push(cardId);
                btn.classList.add('active');
                btn.querySelector('i').className = 'fa-solid fa-heart';
                Utils.showToast('Added to favorites', 'success');
            }
            Utils.save('codesathi_favs', favorites);
        });
    });
}