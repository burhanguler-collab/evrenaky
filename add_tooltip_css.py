import sys
import os

path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\index.css'

css_to_add = """
/* --- Evrenaki Tooltip System --- */
.evrenaki-tooltip {
    position: relative;
    display: inline-block;
    cursor: help;
    border-bottom: 1px dotted var(--neon-blue);
    color: var(--neon-blue);
    font-weight: 500;
}

.evrenaki-tooltip::after {
    content: attr(data-tooltip);
    position: absolute;
    bottom: 125%;
    left: 50%;
    transform: translateX(-50%);
    background-color: var(--card-bg);
    border: 1px solid var(--border-color);
    color: var(--text-primary);
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 0.85rem;
    font-weight: normal;
    white-space: nowrap;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.2s, visibility 0.2s;
    z-index: 100;
    box-shadow: 0 4px 15px rgba(0,255,255,0.1);
    pointer-events: none;
}

.evrenaki-tooltip:hover::after {
    opacity: 1;
    visibility: visible;
}
"""

with open(path, 'a', encoding='utf-8') as f:
    f.write(css_to_add)

print('Tooltip CSS eklendi.')
