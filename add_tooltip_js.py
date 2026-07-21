import sys
import os

path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace block where marked.parse is called
target_content = """        // Post-process HTML for GitHub style alert boxes
        postProcessAlerts(bodyContainer);"""

new_content = """        // Post-process HTML for GitHub style alert boxes
        postProcessAlerts(bodyContainer);

        // Process tooltips
        postProcessTooltips(bodyContainer);"""

content = content.replace(target_content, new_content)

# Add the function at the end of the file
tooltip_function = """

function postProcessTooltips(container) {
    const terms = [
        { regex: /\\b(Evrenakı)\\b/g, tooltip: 'Sürtünmesiz, uzayı dolduran, sıkıştırılabilen süper-akışkan ortam.' },
        { regex: /\\b(Zerre)\\b/g, tooltip: 'Işığı oluşturan, fiziksel hacmi ve kütlesi olan damlacık.' },
        { regex: /\\b(Kütle-İtimi|Kütle-İtim)\\b/gi, tooltip: 'Çekim yerine, akışkan basınç farkından doğan itme kuvveti.' },
        { regex: /\\b(Esir)\\b/gi, tooltip: 'Tarihte ışığın yayıldığı varsayılan ortam. (Evrenakı\\'nın ilkel fikri)' }
    ];

    const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, null, false);
    let node;
    const nodesToReplace = [];

    while (node = walker.nextNode()) {
        if (node.parentNode && (node.parentNode.tagName === 'A' || node.parentNode.tagName === 'CODE' || node.parentNode.tagName === 'PRE' || node.parentNode.tagName === 'H1' || node.parentNode.tagName === 'H2' || node.parentNode.tagName === 'H3' || node.parentNode.classList.contains('evrenaki-tooltip') || node.parentNode.tagName === 'SCRIPT')) {
            continue;
        }
        nodesToReplace.push(node);
    }

    nodesToReplace.forEach(textNode => {
        let text = textNode.nodeValue;
        let replaced = false;

        terms.forEach(term => {
            if (term.regex.test(text)) {
                text = text.replace(term.regex, `<span class="evrenaki-tooltip" data-tooltip="${term.tooltip}">$&</span>`);
                replaced = true;
            }
        });

        if (replaced) {
            const span = document.createElement('span');
            span.innerHTML = text;
            while(span.firstChild) {
                textNode.parentNode.insertBefore(span.firstChild, textNode);
            }
            textNode.parentNode.removeChild(textNode);
        }
    });
}
"""

content += tooltip_function

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('app.js güncellendi.')
