from pathlib import Path
import re
import shutil
import subprocess
import sys
from datetime import datetime

FILE = Path("index.html")

if not FILE.is_file():
    sys.exit("ERROR: index.html not found. Run this from ~/CodeSathee.")

source = FILE.read_text(encoding="utf-8")

# Verify this is the expected CodeSathee application.
required = [
    'id="boot-screen"',
    'const App = {',
    'const P2P = {',
    'App.init();',
    'diff_match_patch'
]
missing = [item for item in required if item not in source]
if missing:
    sys.exit("ERROR: Unexpected index.html structure. Missing: " + ", ".join(missing))

backup = FILE.with_name(
    "index.html.backup-" + datetime.now().strftime("%Y%m%d-%H%M%S")
)
shutil.copy2(FILE, backup)
print("Backup:", backup)

# Remove the previous injected visual theme, if present.
marker = "/* ── CODESATHEE / REFINED SIGNAL THEME"
if marker in source:
    start = source.index(marker)
    end = source.index("</style>", start)
    source = source[:start] + source[end:]

# Restore the original black, charcoal, grey and orange colour identity.
# Increase the clipped-corner cuts while keeping the overall geometry.
theme = r"""
        /* ==========================================================
           CODESATHEE — TACTICAL REFINEMENT
           Original black / graphite / vermilion-orange identity
           ========================================================== */

        :root {
            --bg-black: #050505;
            --bg-panel: #0b0b0b;
            --bg-editor: #070707;
            --border-grey: #242424;
            --border-light: #3a3a3a;
            --text-white: #f2f2f2;
            --text-muted: #858585;
            --accent-orange: #ff6e40;
            --accent-dim: rgba(255, 110, 64, 0.12);
            --danger-red: #ff4d4d;
            --success-green: #4caf50;
        }

        html, body {
            background: var(--bg-black);
        }

        body {
            background:
                radial-gradient(ellipse at 50% -35%,
                    rgba(255, 110, 64, 0.055), transparent 58%),
                var(--bg-black);
        }

        button, input, select {
            font: inherit;
        }

        button {
            cursor: pointer;
            touch-action: manipulation;
        }

        /* Larger diagonal cuts with subtle corner rounding. */
        .user-input,
        .section-title button,
        .tech-card,
        .project-card,
        .nav-btn,
        select.lang-select,
        .qi-btn,
        .btn,
        .ext-item,
        .recent-item,
        #call-widget,
        .modal-content {
            border-radius: 5px;
        }

        .user-input {
            clip-path: polygon(
                0 0, calc(100% - 13px) 0,
                100% 13px, 100% 100%, 0 100%
            );
            border-color: var(--border-light);
            background: #090909;
            transition: border-color .2s, background .2s, box-shadow .2s;
        }

        .user-input:focus,
        .modal-input:focus {
            border-color: var(--accent-orange);
            box-shadow: 0 0 0 2px rgba(255,110,64,.10);
        }

        .tech-card {
            clip-path: polygon(
                0 0, calc(100% - 16px) 0,
                100% 16px, 100% 100%, 0 100%
            );
            border-color: var(--border-grey);
            background: linear-gradient(145deg, #101010, #090909);
            transition: border-color .2s, transform .2s;
        }

        .tech-card:hover {
            border-color: rgba(255,110,64,.55);
            transform: translateY(-2px);
        }

        .project-card {
            clip-path: polygon(
                0 0, calc(100% - 14px) 0,
                100% 14px, 100% 100%, 0 100%
            );
            background: linear-gradient(145deg, #111, #090909);
            transition: border-color .2s, background .2s;
        }

        .project-card:active {
            border-color: var(--accent-orange);
            background: var(--accent-dim);
        }

        .nav-btn {
            clip-path: polygon(
                0 0, calc(100% - 10px) 0,
                100% 10px, 100% 100%, 0 100%
            );
            border-color: var(--border-light);
            transition: border-color .2s, color .2s, background .2s;
        }

        .nav-btn:hover,
        .btn:hover {
            border-color: var(--accent-orange);
        }

        .nav-btn.run-btn,
        .btn-primary {
            background: linear-gradient(110deg, #ff6e40, #e9572c);
            color: #080808;
            box-shadow: 0 5px 18px rgba(255,110,64,.13);
        }

        .nav-btn.run-btn:hover,
        .btn-primary:hover {
            background: linear-gradient(110deg, #ff8058, #f0643b);
        }

        select.lang-select,
        .qi-btn {
            clip-path: polygon(
                0 0, calc(100% - 9px) 0,
                100% 9px, 100% 100%, 0 100%
            );
            border-color: var(--border-grey);
        }

        #editor-pane,
        #output-pane {
            border: 1px solid #202020;
            border-radius: 5px;
            overflow: hidden;
        }

        .CodeMirror {
            background: #070707 !important;
            color: #ededed !important;
        }

        .CodeMirror-gutters {
            background: #0b0b0b !important;
            border-right: 1px solid #252525 !important;
        }

        .CodeMirror-cursor {
            border-left-color: var(--accent-orange) !important;
        }

        .CodeMirror-selected {
            background: rgba(255,110,64,.17) !important;
        }

        .CodeMirror-matchingbracket {
            color: var(--accent-orange) !important;
            border-color: var(--accent-orange) !important;
        }

        .cm-s-default .cm-keyword,
        .cm-s-default .cm-operator,
        .cm-s-default .cm-tag {
            color: var(--accent-orange) !important;
        }

        .output-tabs {
            background: #0c0c0c;
            border-color: #252525;
        }

        .tab-btn.active {
            color: var(--accent-orange);
            border-bottom-color: var(--accent-orange);
        }

        .modal-overlay {
            background: rgba(0,0,0,.82);
        }

        .modal-content {
            clip-path: polygon(
                0 0, calc(100% - 17px) 0,
                100% 17px, 100% 100%, 0 100%
            );
            border: 1px solid #393939;
            background: linear-gradient(145deg, #151515, #090909);
        }

        .ext-item,
        .recent-item {
            border-color: #292929;
            background: #101010;
        }

        .ext-item:hover,
        .recent-item:hover {
            border-color: rgba(255,110,64,.5);
        }

        .toast {
            border: 1px solid #353535;
            border-left: 3px solid var(--accent-orange);
            background: #111;
        }

        #call-widget {
            clip-path: polygon(
                0 0, calc(100% - 13px) 0,
                100% 13px, 100% 100%, 0 100%
            );
        }

        .boot-loader {
            clip-path: polygon(
                0 0, calc(100% - 7px) 0,
                100% 7px, 100% 100%, 0 100%
            );
            background: #292929;
        }

        .boot-loader::after {
            background: var(--accent-orange);
        }

        /* Prevent oversized decorative geometry on small screens. */
        @media (max-width: 640px) {
            .tech-card {
                clip-path: polygon(
                    0 0, calc(100% - 12px) 0,
                    100% 12px, 100% 100%, 0 100%
                );
            }

            .project-card {
                clip-path: polygon(
                    0 0, calc(100% - 11px) 0,
                    100% 11px, 100% 100%, 0 100%
                );
            }
        }
"""

# Insert the refinement immediately before the closing style tag.
style_end = source.rfind("</style>")
if style_end < 0:
    sys.exit("ERROR: Could not locate the closing style tag.")

source = source[:style_end] + theme + "\n" + source[style_end:]

# Make Diff Match Patch failure non-fatal.
# Without this guard, a failed CDN request can stop the entire app script
# before App.init() is reached.
source = source.replace(
    "const dmp = new diff_match_patch();",
    r"""
        const dmp = (() => {
            if (typeof window.diff_match_patch === 'function') {
                return new window.diff_match_patch();
            }

            console.warn('Diff Match Patch unavailable; using full-text sync fallback.');

            return {
                diff_main: (a, b) => [[0, a], [1, b]],
                diff_cleanupSemantic: () => {},
                patch_make: (a, b) => {
                    const text = Array.isArray(b)
                        ? b.map(part => part[1]).join('')
                        : String(b ?? '');
                    return [{ fallbackText: text }];
                },
                patch_toText: patches =>
                    'CODESATHEE_FALLBACK:' +
                    encodeURIComponent(patches?.[0]?.fallbackText ?? ''),
                patch_fromText: text => [{
                    fallbackText: decodeURIComponent(
                        String(text).replace('CODESATHEE_FALLBACK:', '')
                    )
                }],
                patch_apply: (patches, current) => {
                    const next = patches?.[0]?.fallbackText ?? current;
                    return [next, [true]];
                }
            };
        })();
"""
)

# Do not let worker creation prevent the rest of the application from starting.
source = source.replace(
    "const pyWorker = new Worker(URL.createObjectURL(pyBlob));",
    r"""
        let pyWorker;
        try {
            const pyWorkerUrl = URL.createObjectURL(pyBlob);
            pyWorker = new Worker(pyWorkerUrl);
            pyWorker.addEventListener('error', event => {
                console.error('Python worker error:', event.message);
            });
        } catch (workerError) {
            console.error('Python worker unavailable:', workerError);
            pyWorker = {
                onmessage: null,
                postMessage() {
                    if (typeof this.onmessage === 'function') {
                        this.onmessage({
                            data: {
                                type: 'result',
                                data: 'Python runtime could not start. Check browser Worker and CDN access.'
                            }
                        });
                    }
                }
            };
        }
"""
)

# Ensure the boot overlay is removed even if an optional initialization step fails.
old_init = r"""            init: () => {
                setTimeout(() => {
                    const bootScreen = document.getElementById('boot-screen');
                    bootScreen.style.opacity = '0';
                    setTimeout(() => { bootScreen.style.display = 'none'; }, 500);
                }, 1000);

                try {
                    App.initEditor();
                    App.initExtensions();
                    App.initUsername();
                    P2P.init();
                    App.renderProjects();
                    App.changeLang(false);
                    App.renderTimeline();
                    App.updateStorageMeter();
                    App.bindPyWorker();
                } catch (err) {
                    console.error("Initialization Error:", err);
                    Utils.toast('System initialization error: ' + err.message, 'error');
                }
            },"""

new_init = r"""            init: () => {
                const hideBootScreen = () => {
                    const bootScreen = document.getElementById('boot-screen');
                    if (!bootScreen) return;
                    bootScreen.style.opacity = '0';
                    setTimeout(() => {
                        bootScreen.style.display = 'none';
                        bootScreen.setAttribute('aria-hidden', 'true');
                    }, 350);
                };

                // Never leave the user trapped behind the boot overlay.
                hideBootScreen();

                try {
                    App.initEditor();
                } catch (err) {
                    console.error('Editor initialization error:', err);
                    Utils.toast('Editor could not initialize. Check CodeMirror CDN access.', 'error');
                }

                const safeInit = (label, callback) => {
                    try {
                        callback();
                    } catch (err) {
                        console.error(label + ' initialization error:', err);
                        Utils.toast(label + ' is unavailable: ' + err.message, 'error');
                    }
                };

                safeInit('Extensions', () => App.initExtensions());
                safeInit('Username', () => App.initUsername());
                safeInit('Peer connection', () => P2P.init());
                safeInit('Projects', () => App.renderProjects());
                safeInit('Language', () => App.changeLang(false));
                safeInit('Timeline', () => App.renderTimeline());
                safeInit('Storage', () => App.updateStorageMeter());
                safeInit('Python worker', () => App.bindPyWorker());
            },"""

if old_init not in source:
    sys.exit(
        "ERROR: App.init() did not match the expected source. "
        "No updated index.html was written. Your backup is available at " + str(backup)
    )

source = source.replace(old_init, new_init)

# Keep the boot overlay from intercepting interaction after initialization.
source = source.replace(
    '<div id="boot-screen">',
    '<div id="boot-screen" role="status" aria-live="polite">'
)

# Final structural checks before writing.
if source.count("<html") != 1 or source.count("</html>") != 1:
    sys.exit("ERROR: HTML structure validation failed. Original file was not replaced.")

if "CODESATHEE_FALLBACK" not in source or "TACTICAL REFINEMENT" not in source:
    sys.exit("ERROR: Required update markers missing. Original file was not replaced.")

FILE.write_text(source, encoding="utf-8")
print("Updated index.html successfully.")
print("Original application features and event handlers were retained.")
