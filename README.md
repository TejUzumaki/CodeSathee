# CodeSathee

> **STATUS: ON HOLD / ARCHIVED**
> 
> **⚠️ WARNING: DO NOT USE THE LATEST COMMIT.** 
> The current `main` branch contains an unstable, broken build. The P2P CRDT sync and editor intelligence features are undergoing a heavy architectural rewrite and currently do not function as intended. Please do not clone or deploy this version.

### What is CodeSathee?
CodeSathee is a tactical, 100% client-side, collaborative code editor built for mobile-first developers. It was designed to use raw WebRTC (PeerJS) for real-time code syncing, voice channels, and remote cursor tracking—entirely serverless and local-first. 

### Why is it paused?
Building a flawless CRDT (Conflict-free Replicated Data Type) bridge between Yjs and CodeMirror 5 on strictly mobile browsers hit severe architectural roadblocks. The custom math required to sync text operations without data loss introduced silent failures, and the project requires a complete rewrite of its core binding logic using a different approach or framework.

### Intended Features (Concept)
*   **P2P Code Sync:** Yjs CRDT integration for real-time, conflict-free collaborative typing.
*   **WebRTC Voice:** Built-in peer-to-peer voice channels with Voice Activity Detection (VAD).
*   **Remote Presence:** Live remote cursor and mouse tracking.
*   **Local-First:** All projects and snapshots saved to `localStorage`.
*   **Tactical UI:** Strict brutalist, dark-mode interface with `clip-path` geometry and JetBrains Mono.
*   **Multi-Language:** JS, Python (via Pyodide WASM), HTML, CSS.
*   **Live Preview:** Context-aware split-screen for HTML/CSS rendering.

### Tech Stack
*   **Frontend:** Vanilla HTML/CSS/JS
*   **Editor:** CodeMirror 5
*   **P2P/WebRTC:** PeerJS
*   **CRDT:** Yjs
*   **Animations:** GSAP

### Future
I am halting active development on this project for the time being. The repository will remain public as a reference for the UI/UX design and the P2P voice implementation, but no further updates will be pushed until the architectural vision is completely solidified.

---
*Built by [TejUzumaki](https://github.com/TejUzumaki)*
