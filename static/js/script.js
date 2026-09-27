let targetUrl = '';
let generatedSuiteCode = '';
let currentTestCases = [];
let prefersReducedMotion = false;

try {
    prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
} catch (_) {
    prefersReducedMotion = false;
}

function scrollToAgent() {
    const el = document.getElementById('agent-interface');
    if (el) {
        el.scrollIntoView({
            behavior: prefersReducedMotion ? 'auto' : 'smooth',
            block: 'center'
        });
    }
}

function toggleMenu() {
    document.getElementById('mobile-menu').classList.toggle('open');
    document.getElementById('hamburger').classList.toggle('open');
}

function closeMenu() {
    document.getElementById('mobile-menu').classList.remove('open');
    document.getElementById('hamburger').classList.remove('open');
}

function updateSelectionCount() {
    const functional = document.getElementById('test-functional').checked;
    const negative = document.getElementById('test-negative').checked;
    const countSpan = document.getElementById('selection-count');
    const genBtn = document.getElementById('generate-btn');
    const combinedHint = document.getElementById('combined-hint');

    let count = 0;
    if (functional) count++;
    if (negative) count++;

    countSpan.textContent = count === 0
        ? '0 selected'
        : (count === 1 ? '1 test type selected' : '2 test types selected');

    genBtn.disabled = count === 0;
    if (combinedHint) {
        combinedHint.classList.toggle('hidden', !(functional && negative));
    }
}

function hostnameFromUrl(url) {
    try {
        return new URL(url).hostname || url;
    } catch (_) {
        return url.replace(/^https?:\/\//, '').split('/')[0] || url;
    }
}

function setBusy(isBusy) {
    const btn = document.getElementById('generate-btn');
    const label = document.getElementById('generate-btn-label');
    const icon = document.getElementById('generate-btn-icon');
    const status = document.getElementById('agent-status');
    const statusText = document.getElementById('agent-status-text');
    const idle = document.getElementById('agent-idle-copy');

    if (isBusy) {
        btn.disabled = true;
        label.textContent = 'Generating…';
        icon.className = 'fa-solid fa-circle-notch spinner';
        status.classList.remove('hidden');
        statusText.textContent = 'Processing your request…';
        if (idle) idle.classList.add('hidden');
    } else {
        label.textContent = 'Generate Automation Tests';
        icon.className = 'fa-solid fa-arrow-right';
        status.classList.add('hidden');
        if (idle) idle.classList.remove('hidden');
        updateSelectionCount();
    }
}

function showEmptyCodeState() {
    generatedSuiteCode = '';
    document.getElementById('code-empty').classList.remove('hidden');
    document.getElementById('line-numbers').classList.add('hidden');
    document.querySelector('#editor-body .code-content').classList.add('hidden');
    document.getElementById('editor-code').textContent = '';
    document.getElementById('line-numbers').textContent = '';
    document.getElementById('copy-btn').disabled = true;
    document.getElementById('download-btn').disabled = true;
}

function showCode(code, filename) {
    generatedSuiteCode = code || '';
    const empty = document.getElementById('code-empty');
    const linesEl = document.getElementById('line-numbers');
    const codeWrap = document.querySelector('#editor-body .code-content');
    const codeEl = document.getElementById('editor-code');

    if (!generatedSuiteCode) {
        showEmptyCodeState();
        return;
    }

    empty.classList.add('hidden');
    linesEl.classList.remove('hidden');
    codeWrap.classList.remove('hidden');
    codeEl.textContent = generatedSuiteCode;

    const lineCount = generatedSuiteCode.split('\n').length;
    linesEl.textContent = Array.from({ length: lineCount }, (_, i) => i + 1).join('\n');

    document.getElementById('copy-btn').disabled = false;
    document.getElementById('download-btn').disabled = false;

    const tabs = document.getElementById('file-tabs');
    tabs.innerHTML = `<span class="file-tab active"><i class="fa-brands fa-python"></i> ${filename || 'generated_tests.py'}</span>`;
}

function renderTests(tests) {
    const grid = document.getElementById('test-cases-grid');
    currentTestCases = Array.isArray(tests) ? tests : [];

    if (!currentTestCases.length) {
        grid.innerHTML = '<p class="empty-state" id="tests-empty">Generated tests will appear here.</p>';
        return;
    }

    grid.innerHTML = '';
    currentTestCases.forEach((tc) => {
        const card = document.createElement('div');
        card.className = 'tc-card';
        const type = (tc.type || '').toLowerCase();
        const typeBadge = type === 'negative'
            ? '<span class="badge negative">NEGATIVE</span>'
            : '<span class="badge functional">FUNCTIONAL</span>';

        const steps = Array.isArray(tc.steps)
            ? `<ol>${tc.steps.map((s) => `<li>${escapeHtml(s)}</li>`).join('')}</ol>`
            : '';

        card.innerHTML = `
            <div class="tc-header">
                <span class="tc-id">${escapeHtml(tc.id || '')}</span>
                <div class="tc-badges">${typeBadge}</div>
            </div>
            <div class="tc-title">${escapeHtml(tc.title || 'Untitled test')}</div>
            ${tc.description ? `<div class="tc-section"><h4>Description</h4><p>${escapeHtml(tc.description)}</p></div>` : ''}
            ${steps ? `<div class="tc-section"><h4>Steps</h4>${steps}</div>` : ''}
            ${tc.expected ? `<div class="tc-section"><h4>Expected</h4><p>${escapeHtml(tc.expected)}</p></div>` : ''}
        `;
        grid.appendChild(card);
    });
}

function escapeHtml(str) {
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');
}

function showResultsShell(functional, negative) {
    const host = hostnameFromUrl(targetUrl);
    document.getElementById('meta-target').textContent = host;

    const typesEl = document.getElementById('meta-types');
    const badges = [];
    if (functional) badges.push('<span class="pill functional">Functional</span>');
    if (negative) badges.push('<span class="pill negative">Negative</span>');
    typesEl.innerHTML = badges.join('') || '—';

    showEmptyCodeState();
    renderTests([]);

    const results = document.getElementById('results-section');
    results.classList.remove('hidden');
    results.scrollIntoView({
        behavior: prefersReducedMotion ? 'auto' : 'smooth',
        block: 'start'
    });
}

/**
 * Apply real agent/API payload when available.
 * Expected optional shape: { code, filename, tests }
 */
function applyGenerationResult(payload) {
    if (!payload || typeof payload !== 'object') {
        showEmptyCodeState();
        renderTests([]);
        return;
    }

    if (payload.code) {
        showCode(payload.code, payload.filename);
    } else {
        showEmptyCodeState();
    }

    renderTests(payload.tests || []);
}

async function startGeneration() {
    const urlInput = document.getElementById('website-url').value.trim();
    if (!urlInput) {
        alert('Please enter a website URL.');
        return;
    }

    const wantsFunctional = document.getElementById('test-functional').checked;
    const wantsNegative = document.getElementById('test-negative').checked;
    if (!wantsFunctional && !wantsNegative) return;

    targetUrl = urlInput;
    document.getElementById('results-section').classList.add('hidden');
    setBusy(true);

    try {
        // No generation API in this project yet — show request context only.
        // When a backend endpoint exists, call it here and pass the response to applyGenerationResult().
        await new Promise((r) => setTimeout(r, prefersReducedMotion ? 0 : 400));

        showResultsShell(wantsFunctional, wantsNegative);
        applyGenerationResult(null);
    } finally {
        setBusy(false);
    }
}

function copyEditorCode() {
    if (!generatedSuiteCode) return;
    navigator.clipboard.writeText(generatedSuiteCode).then(() => {
        const btn = document.getElementById('copy-btn');
        const original = btn.innerHTML;
        btn.innerHTML = '<i class="fa-solid fa-check"></i> Copied';
        setTimeout(() => { btn.innerHTML = original; }, 2000);
    });
}

function downloadCode() {
    if (!generatedSuiteCode) return;
    const blob = new Blob([generatedSuiteCode], { type: 'text/x-python' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'generated_tests.py';
    a.click();
    URL.revokeObjectURL(a.href);
}

function initReveal() {
    const els = document.querySelectorAll('.reveal');
    if (prefersReducedMotion) {
        els.forEach((el) => el.classList.add('visible'));
        return;
    }
    const io = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                io.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach((el) => io.observe(el));
}

function initNavScroll() {
    const nav = document.getElementById('navbar');
    const onScroll = () => {
        nav.classList.toggle('scrolled', window.scrollY > 12);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
}

document.addEventListener('DOMContentLoaded', () => {
    updateSelectionCount();
    initReveal();
    initNavScroll();

    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
        anchor.addEventListener('click', (e) => {
            const id = anchor.getAttribute('href');
            if (id.length > 1) {
                const target = document.querySelector(id);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: prefersReducedMotion ? 'auto' : 'smooth' });
                    closeMenu();
                }
            }
        });
    });
});
