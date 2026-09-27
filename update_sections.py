import re

html_replacement = r"""    <!-- Info Sections -->
    <div class="sections-wrapper">
        
        <!-- PRODUCT SECTION -->
        <section id="product" class="polished-section product-section">
            <div class="polished-container">
                <div class="section-label">THE PRODUCT</div>
                <h2 class="section-heading">AI-powered test design for any website.</h2>
                
                <div class="product-grid">
                    <div class="product-text">
                        <p>AI-Powered QA Test Design Agent helps QA engineers turn a website into a structured set of test scenarios.</p>
                        <p>Instead of manually exploring every page and thinking about what should be tested, the agent analyzes the website's functionality and identifies scenarios worth testing.</p>
                        <p>The user simply provides a website URL and selects the types of tests they need.</p>
                        
                        <div class="flow-visual">
                            <span>Website URL</span> <i class="fa-solid fa-arrow-right"></i>
                            <span>Website Analysis</span> <i class="fa-solid fa-arrow-right"></i>
                            <span>Functionality Detection</span> <i class="fa-solid fa-arrow-right"></i>
                            <span>AI Test Design</span> <i class="fa-solid fa-arrow-right"></i>
                            <span>Test Cases</span> <i class="fa-solid fa-arrow-right"></i>
                            <span>Automation Code</span>
                        </div>
                        <div class="workflow-statement">
                            <i class="fa-solid fa-bolt"></i> From website exploration to test design — in one workflow.
                        </div>
                    </div>
                    
                    <div class="product-visual">
                        <div class="mock-window">
                            <div class="mock-header">
                                <i class="fa-solid fa-terminal"></i> AI QA TEST DESIGN AGENT
                            </div>
                            <div class="mock-body">
                                <div class="mock-line"><span class="mock-label">Website</span> <a href="#" class="mock-link">https://example.com</a></div>
                                <div class="mock-divider"></div>
                                <div class="mock-line"><span class="mock-label">Test types</span></div>
                                <div class="mock-line"><i class="fa-solid fa-check mock-check"></i> Functional</div>
                                <div class="mock-line"><i class="fa-solid fa-check mock-check"></i> Negative</div>
                                <div class="mock-divider"></div>
                                <div class="mock-line"><span class="mock-label">AI ANALYSIS</span></div>
                                <div class="mock-line"><i class="fa-solid fa-check mock-check"></i> Forms detected</div>
                                <div class="mock-line"><i class="fa-solid fa-check mock-check"></i> Navigation detected</div>
                                <div class="mock-line"><i class="fa-solid fa-check mock-check"></i> Authentication detected</div>
                                <div class="mock-line"><i class="fa-solid fa-check mock-check"></i> Validation detected</div>
                                <div class="mock-divider"></div>
                                <div class="mock-highlight">12 TEST CASES GENERATED</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- HOW IT WORKS SECTION -->
        <section id="how-it-works" class="polished-section hiw-section">
            <div class="polished-container">
                <div class="section-label">HOW IT WORKS</div>
                <h2 class="section-heading">From URL to test cases.</h2>
                <p class="section-subtitle">The agent follows a simple workflow to understand a website and turn its functionality into testable scenarios.</p>
                
                <div class="timeline-container">
                    <div class="timeline-step">
                        <div class="step-number">01</div>
                        <div class="step-icon"><i class="fa-solid fa-link"></i></div>
                        <div class="step-content">
                            <h3>ENTER A WEBSITE</h3>
                            <p>Provide the URL of the website you want to analyze.</p>
                            <div class="step-example">https://your-website.com</div>
                        </div>
                    </div>
                    
                    <div class="timeline-connector"></div>
                    
                    <div class="timeline-step">
                        <div class="step-number">02</div>
                        <div class="step-icon"><i class="fa-solid fa-list-check"></i></div>
                        <div class="step-content">
                            <h3>CHOOSE TEST TYPES</h3>
                            <p>Select what you want the agent to generate:</p>
                            <ul class="step-list">
                                <li><i class="fa-solid fa-check"></i> Functional Tests</li>
                                <li><i class="fa-solid fa-check"></i> Negative Tests</li>
                            </ul>
                            <p class="step-note">Both options can be selected at the same time.</p>
                        </div>
                    </div>
                    
                    <div class="timeline-connector"></div>
                    
                    <div class="timeline-step">
                        <div class="step-number">03</div>
                        <div class="step-icon"><i class="fa-solid fa-magnifying-glass-chart"></i></div>
                        <div class="step-content">
                            <h3>ANALYZE THE WEBSITE</h3>
                            <p>The agent explores the website and identifies relevant functionality such as forms, buttons, links, navigation, authentication, input fields, validation, and user flows.</p>
                        </div>
                    </div>
                    
                    <div class="timeline-connector"></div>
                    
                    <div class="timeline-step">
                        <div class="step-number">04</div>
                        <div class="step-icon"><i class="fa-solid fa-microchip"></i></div>
                        <div class="step-content">
                            <h3>DESIGN TEST CASES</h3>
                            <p>The AI analyzes the discovered functionality and creates relevant test scenarios.</p>
                            <div class="step-split">
                                <div>
                                    <strong>Functional</strong>
                                    <span>login, registration, valid form submission</span>
                                </div>
                                <div>
                                    <strong>Negative</strong>
                                    <span>invalid credentials, empty required fields, invalid email, incorrect input</span>
                                </div>
                            </div>
                            <p class="step-note highlight">The agent does not simply use a fixed list of tests. It determines which scenarios make sense for the specific website.</p>
                        </div>
                    </div>
                    
                    <div class="timeline-connector"></div>
                    
                    <div class="timeline-step">
                        <div class="step-number">05</div>
                        <div class="step-icon"><i class="fa-solid fa-code"></i></div>
                        <div class="step-content">
                            <h3>GENERATE AUTOMATION CODE</h3>
                            <p>The final test cases can be transformed into automation-ready Python/Playwright code.</p>
                            <div class="code-snippet-small">
                                <div class="code-label">Example generated code</div>
                                <pre>def test_invalid_login(page):
    page.goto("https://example.com/login")
    page.fill("#email", "user@example.com")
    page.fill("#password", "wrong-password")
    page.click("button[type='submit']")
    assert page.locator(".error-message").is_visible()</pre>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- FEATURES SECTION -->
        <section id="features" class="polished-section features-section">
            <div class="polished-container">
                <div class="section-label">FEATURES</div>
                <h2 class="section-heading">Everything you need to start designing tests faster.</h2>
                <p class="section-subtitle">The agent combines website analysis, AI reasoning and structured test generation into one workflow.</p>
                
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-meta">
                            <span class="feature-num">01</span>
                            <i class="fa-solid fa-globe feature-icon"></i>
                        </div>
                        <h3>AI Website Analysis</h3>
                        <p>The agent analyzes the structure and functionality of the provided website instead of relying on predefined test scenarios.</p>
                    </div>
                    
                    <div class="feature-card alt-bg">
                        <div class="feature-meta">
                            <span class="feature-num">02</span>
                            <i class="fa-solid fa-circle-check feature-icon"></i>
                        </div>
                        <h3>Functional Test Generation</h3>
                        <p>Generate test cases for successful user flows and expected application behavior.</p>
                        <div class="feature-tags">
                            <span>Login</span> <span>Registration</span> <span>Search</span> <span>Form submission</span> <span>Navigation</span>
                        </div>
                    </div>
                    
                    <div class="feature-card">
                        <div class="feature-meta">
                            <span class="feature-num">03</span>
                            <i class="fa-solid fa-triangle-exclamation feature-icon"></i>
                        </div>
                        <h3>Negative Test Generation</h3>
                        <p>Generate scenarios that verify how the website behaves when users provide invalid or unexpected input.</p>
                        <div class="feature-tags">
                            <span>Invalid credentials</span> <span>Empty fields</span> <span>Invalid email</span> <span>Incorrect data</span> <span>Unsupported input</span>
                        </div>
                    </div>
                    
                    <div class="feature-card alt-border">
                        <div class="feature-meta">
                            <span class="feature-num">04</span>
                            <i class="fa-solid fa-layer-group feature-icon"></i>
                        </div>
                        <h3>Combined Test Design</h3>
                        <p>Functional and negative testing can be selected together. The agent generates both positive and error scenarios in the same test-generation workflow.</p>
                    </div>
                    
                    <div class="feature-card">
                        <div class="feature-meta">
                            <span class="feature-num">05</span>
                            <i class="fa-solid fa-code feature-icon"></i>
                        </div>
                        <h3>Automation-Ready Code</h3>
                        <p>Generated test cases can be represented as Python/Playwright automation code. The goal is to reduce the distance between: Test idea &rarr; Test case &rarr; Automated test.</p>
                    </div>
                    
                    <div class="feature-card highlight-card">
                        <div class="feature-meta">
                            <span class="feature-num">06</span>
                            <i class="fa-solid fa-user-check feature-icon"></i>
                        </div>
                        <h3>Human Review</h3>
                        <p>The AI generates test scenarios, but the QA engineer remains in control. Generated tests can be reviewed, modified and extended before they are used.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- EXAMPLES SECTION -->
        <section id="examples" class="polished-section examples-section">
            <div class="polished-container">
                <div class="section-label">EXAMPLES</div>
                <h2 class="section-heading">See what the agent can generate.</h2>
                <p class="section-subtitle">The same website functionality can produce different test scenarios depending on the selected test types.</p>
                
                <div class="examples-dashboard">
                    <div class="ex-sidebar">
                        <div class="ex-site-info">
                            <h4>Analyzed website</h4>
                            <a href="#">https://example.com/</a>
                            <div class="ex-status"><i class="fa-solid fa-check-circle"></i> Analysis complete</div>
                        </div>
                        <div class="ex-detected">
                            <h4>Detected functionality:</h4>
                            <ul>
                                <li><i class="fa-solid fa-caret-right"></i> Login</li>
                                <li><i class="fa-solid fa-caret-right"></i> Registration</li>
                                <li><i class="fa-solid fa-caret-right"></i> Search</li>
                                <li><i class="fa-solid fa-caret-right"></i> Contact form</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="ex-main">
                        <div class="ex-tabs">
                            <button class="ex-tab active" onclick="filterExamples('all')">ALL</button>
                            <button class="ex-tab" onclick="filterExamples('functional')">FUNCTIONAL</button>
                            <button class="ex-tab" onclick="filterExamples('negative')">NEGATIVE</button>
                        </div>
                        
                        <div class="ex-list" id="ex-list">
                            <!-- Example 1 -->
                            <div class="ex-card" data-type="functional">
                                <div class="tc-header">
                                    <span class="tc-id">TC-001</span>
                                    <div class="tc-badges">
                                        <span class="badge functional">FUNCTIONAL</span>
                                        <span class="badge high">HIGH PRIORITY</span>
                                    </div>
                                </div>
                                <div class="tc-title">Successful user login</div>
                                <div class="tc-section"><h4>Description</h4><p>Verify that a registered user can successfully authenticate using valid credentials.</p></div>
                                <div class="tc-section"><h4>Preconditions</h4><p>A registered user account exists.</p></div>
                                <div class="tc-section"><h4>Steps</h4>
                                    <ol>
                                        <li>Open the login page.</li>
                                        <li>Enter a valid email address.</li>
                                        <li>Enter a valid password.</li>
                                        <li>Click the Login button.</li>
                                    </ol>
                                </div>
                                <div class="tc-section"><h4>Expected result</h4><p>The user is authenticated and redirected to the dashboard.</p></div>
                                <div class="tc-footer">
                                    <button class="btn-code" onclick="showExCode('ex-code-1')"><i class="fa-solid fa-code"></i> View Python Code</button>
                                </div>
                            </div>
                            
                            <!-- Example 2 -->
                            <div class="ex-card" data-type="negative">
                                <div class="tc-header">
                                    <span class="tc-id">TC-002</span>
                                    <div class="tc-badges">
                                        <span class="badge negative">NEGATIVE</span>
                                        <span class="badge high">HIGH PRIORITY</span>
                                    </div>
                                </div>
                                <div class="tc-title">Login with invalid password</div>
                                <div class="tc-section"><h4>Description</h4><p>Verify that the system rejects an incorrect password.</p></div>
                                <div class="tc-section"><h4>Preconditions</h4><p>A registered user account exists.</p></div>
                                <div class="tc-section"><h4>Steps</h4>
                                    <ol>
                                        <li>Open the login page.</li>
                                        <li>Enter a valid email address.</li>
                                        <li>Enter an incorrect password.</li>
                                        <li>Click the Login button.</li>
                                    </ol>
                                </div>
                                <div class="tc-section"><h4>Expected result</h4><p>Authentication fails and an appropriate error message is displayed.</p></div>
                                <div class="tc-footer">
                                    <button class="btn-code" onclick="showExCode('ex-code-2')"><i class="fa-solid fa-code"></i> View Python Code</button>
                                </div>
                            </div>
                            
                            <!-- Example 3 -->
                            <div class="ex-card" data-type="negative">
                                <div class="tc-header">
                                    <span class="tc-id">TC-003</span>
                                    <div class="tc-badges">
                                        <span class="badge negative">NEGATIVE</span>
                                        <span class="badge medium">MEDIUM PRIORITY</span>
                                    </div>
                                </div>
                                <div class="tc-title">Submit login form with empty password</div>
                                <div class="tc-section"><h4>Steps</h4>
                                    <ol>
                                        <li>Open the login page.</li>
                                        <li>Enter a valid email address.</li>
                                        <li>Leave the password field empty.</li>
                                        <li>Click Login.</li>
                                    </ol>
                                </div>
                                <div class="tc-section"><h4>Expected result</h4><p>The application prevents submission and displays a validation message.</p></div>
                                <div class="tc-footer">
                                    <button class="btn-code" onclick="showExCode('ex-code-3')"><i class="fa-solid fa-code"></i> View Python Code</button>
                                </div>
                            </div>
                            
                            <!-- Example 4 -->
                            <div class="ex-card" data-type="functional">
                                <div class="tc-header">
                                    <span class="tc-id">TC-004</span>
                                    <div class="tc-badges">
                                        <span class="badge functional">FUNCTIONAL</span>
                                        <span class="badge medium">MEDIUM PRIORITY</span>
                                    </div>
                                </div>
                                <div class="tc-title">Successful search</div>
                                <div class="tc-section"><h4>Steps</h4>
                                    <ol>
                                        <li>Open the search interface.</li>
                                        <li>Enter a valid search query.</li>
                                        <li>Submit the search.</li>
                                    </ol>
                                </div>
                                <div class="tc-section"><h4>Expected result</h4><p>Relevant search results are displayed.</p></div>
                                <div class="tc-footer">
                                    <button class="btn-code" onclick="showExCode('ex-code-4')"><i class="fa-solid fa-code"></i> View Python Code</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
    
    <!-- EXAMPLES CODE MODAL -->
    <div id="ex-code-modal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Test Case Code</h3>
                <span class="close-btn" onclick="closeExCode()">&times;</span>
            </div>
            <div class="modal-meta">
                <span class="meta-tag"><i class="fa-brands fa-python"></i> PYTHON / PLAYWRIGHT</span>
                <span class="demo-warning-small">Example generated automation code</span>
            </div>
            <div class="code-block-wrapper">
                <button class="copy-btn" id="ex-copy-btn" onclick="copyExCode()"><i class="fa-regular fa-copy"></i> Copy Code</button>
                <pre><code id="ex-modal-code"></code></pre>
            </div>
        </div>
    </div>
    
    <script>
        const exCodeData = {
            'ex-code-1': 'def test_successful_login(page):\\n    page.goto("https://example.com/login")\\n    page.fill("#email", "user@example.com")\\n    page.fill("#password", "SecurePassword123")\\n    page.click("button[type=\\'submit\\']")\\n    assert page.url == "https://example.com/dashboard"',
            'ex-code-2': 'def test_invalid_login(page):\\n    page.goto("https://example.com/login")\\n    page.fill("#email", "user@example.com")\\n    page.fill("#password", "invalid-password")\\n    page.click("button[type=\\'submit\\']")\\n    assert page.locator(".error-message").is_visible()',
            'ex-code-3': 'def test_empty_password(page):\\n    page.goto("https://example.com/login")\\n    page.fill("#email", "user@example.com")\\n    page.fill("#password", "")\\n    page.click("button[type=\\'submit\\']")\\n    assert page.locator("#password:invalid").is_visible()',
            'ex-code-4': 'def test_successful_search(page):\\n    page.goto("https://example.com")\\n    page.fill("input[type=\\'search\\']", "test query")\\n    page.press("input[type=\\'search\\']", "Enter")\\n    assert page.locator(".search-results").is_visible()'
        };

        function filterExamples(type) {
            document.querySelectorAll('.ex-tab').forEach(t => t.classList.remove('active'));
            event.target.classList.add('active');
            
            document.querySelectorAll('.ex-card').forEach(card => {
                if (type === 'all' || card.getAttribute('data-type') === type) {
                    card.style.display = 'flex';
                    card.style.animation = 'fadeIn 0.3s ease';
                } else {
                    card.style.display = 'none';
                }
            });
        }

        function showExCode(id) {
            document.getElementById('ex-modal-code').textContent = exCodeData[id];
            document.getElementById('ex-code-modal').classList.add('show');
            const copyBtn = document.getElementById('ex-copy-btn');
            copyBtn.innerHTML = '<i class="fa-regular fa-copy"></i> Copy Code';
        }

        function closeExCode() {
            document.getElementById('ex-code-modal').classList.remove('show');
        }

        function copyExCode() {
            const code = document.getElementById('ex-modal-code').textContent;
            navigator.clipboard.writeText(code).then(() => {
                const copyBtn = document.getElementById('ex-copy-btn');
                copyBtn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
                setTimeout(() => {
                    copyBtn.innerHTML = '<i class="fa-regular fa-copy"></i> Copy Code';
                }, 2000);
            });
        }

        window.addEventListener('click', function(event) {
            const exModal = document.getElementById('ex-code-modal');
            if (event.target == exModal) {
                closeExCode();
            }
        });
    </script>
"""

with open("templates/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the old Info Sections with the new one
html = re.sub(
    r"    <!-- Info Sections -->.*?    <!-- Code Modal -->", 
    html_replacement + "\n    <!-- Code Modal -->", 
    html, 
    flags=re.DOTALL
)

with open("templates/index.html", "w", encoding="utf-8") as f:
    f.write(html)


css_replacement = r"""
/* ===============================
   NEW POLISHED SECTIONS 
   =============================== */
.sections-wrapper {
    background-color: var(--bg-dark);
    position: relative;
}

.polished-section {
    padding: 6rem 2rem;
    position: relative;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.polished-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 60%;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--primary), transparent);
    opacity: 0.3;
}

.polished-container {
    max-width: 1000px;
    margin: 0 auto;
}

.section-label {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    background-color: rgba(99, 102, 241, 0.1);
    color: var(--primary);
    border: 1px solid rgba(99, 102, 241, 0.2);
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 1rem;
}

.section-heading {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    font-weight: 800;
    color: #fff;
}

.section-subtitle {
    font-size: 1.1rem;
    color: var(--text-muted);
    margin-bottom: 3rem;
    max-width: 600px;
}

/* PRODUCT */
.product-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    align-items: center;
}

.product-text p {
    font-size: 1.1rem;
    color: var(--text-muted);
    margin-bottom: 1rem;
}

.flow-visual {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.5rem;
    margin: 2rem 0;
    background: rgba(255, 255, 255, 0.03);
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    font-size: 0.85rem;
    font-weight: 600;
    color: #cbd5e1;
}

.flow-visual i {
    color: var(--primary);
    font-size: 0.75rem;
}

.workflow-statement {
    font-weight: 600;
    color: var(--text-main);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.workflow-statement i {
    color: var(--warning);
}

.mock-window {
    background-color: #11141a;
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
}

.mock-header {
    background-color: #1a1d24;
    padding: 0.75rem 1rem;
    font-size: 0.8rem;
    font-weight: 700;
    color: var(--text-muted);
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.mock-body {
    padding: 1.5rem;
}

.mock-line {
    margin-bottom: 0.75rem;
    font-size: 0.9rem;
    color: #e2e8f0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.mock-label {
    color: var(--text-muted);
    font-size: 0.8rem;
    text-transform: uppercase;
}

.mock-link {
    color: var(--primary);
    text-decoration: none;
}

.mock-check {
    color: var(--functional);
}

.mock-divider {
    height: 1px;
    background-color: rgba(255, 255, 255, 0.05);
    margin: 1rem 0;
}

.mock-highlight {
    color: var(--primary);
    font-weight: 700;
    font-size: 0.85rem;
    letter-spacing: 0.5px;
}

/* HOW IT WORKS */
.hiw-section {
    background: radial-gradient(circle at right top, rgba(99, 102, 241, 0.05), transparent 50%);
}

.timeline-container {
    position: relative;
    padding-left: 2.5rem;
}

.timeline-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 2px;
    height: 100%;
    background: linear-gradient(to bottom, var(--primary), rgba(99, 102, 241, 0.1));
    border-radius: 2px;
}

.timeline-step {
    position: relative;
    padding-bottom: 3.5rem;
}

.timeline-step:last-child {
    padding-bottom: 0;
}

.step-number {
    position: absolute;
    left: -3.4rem;
    top: 0;
    background-color: var(--bg-dark);
    color: var(--primary);
    font-weight: 800;
    font-size: 1rem;
    border: 2px solid var(--primary);
    border-radius: 50%;
    width: 34px;
    height: 34px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 15px rgba(99, 102, 241, 0.3);
}

.step-icon {
    display: inline-block;
    padding: 0.5rem 0.75rem;
    background-color: rgba(99, 102, 241, 0.1);
    color: var(--primary);
    border-radius: 8px;
    margin-bottom: 1rem;
    font-size: 1.25rem;
}

.step-content h3 {
    font-size: 1.3rem;
    margin-bottom: 0.5rem;
    color: #fff;
}

.step-content p {
    color: var(--text-muted);
    margin-bottom: 0.75rem;
    font-size: 1.05rem;
}

.step-example {
    font-family: monospace;
    background: rgba(0,0,0,0.3);
    padding: 0.5rem 1rem;
    border-radius: 4px;
    color: var(--primary);
    display: inline-block;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.step-list {
    list-style: none;
    margin: 0.5rem 0;
}

.step-list li {
    color: var(--text-main);
    font-size: 1.05rem;
    margin-bottom: 0.4rem;
}

.step-list i {
    color: var(--functional);
    margin-right: 0.5rem;
}

.step-note {
    font-size: 0.9rem !important;
    font-style: italic;
    margin-top: 0.5rem;
}

.step-note.highlight {
    color: var(--warning) !important;
}

.step-split {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    background: rgba(255, 255, 255, 0.03);
    padding: 1.5rem;
    border-radius: 8px;
    margin: 1.5rem 0;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.step-split strong {
    display: block;
    color: #e2e8f0;
    margin-bottom: 0.5rem;
    font-size: 1.05rem;
}

.step-split span {
    font-size: 0.9rem;
    color: var(--text-muted);
    line-height: 1.4;
    display: block;
}

.code-snippet-small {
    background: #0d1117;
    border: 1px solid var(--border);
    border-radius: 8px;
    overflow: hidden;
    margin-top: 1.5rem;
}

.code-label {
    background: #161b22;
    padding: 0.5rem 1rem;
    font-size: 0.8rem;
    color: var(--text-muted);
    border-bottom: 1px solid var(--border);
}

.code-snippet-small pre {
    padding: 1.5rem;
    font-size: 0.9rem;
    margin: 0;
}

/* FEATURES */
.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
}

.feature-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 2.5rem 2rem;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.feature-card:hover {
    transform: translateY(-5px);
    border-color: rgba(99, 102, 241, 0.5);
    box-shadow: 0 10px 30px -10px rgba(99, 102, 241, 0.2);
}

.feature-card.alt-bg {
    background: linear-gradient(145deg, var(--bg-card), rgba(16, 185, 129, 0.03));
}

.feature-card.alt-border {
    border: 1px solid rgba(239, 68, 68, 0.2);
}

.feature-card.highlight-card {
    border-color: rgba(245, 158, 11, 0.3);
}

.feature-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
}

.feature-num {
    font-weight: 800;
    color: rgba(255, 255, 255, 0.05);
    font-size: 2rem;
    line-height: 1;
}

.feature-icon {
    font-size: 1.8rem;
    color: var(--primary);
    transition: transform 0.3s ease;
}

.feature-card:hover .feature-icon {
    transform: scale(1.1);
}

.feature-card h3 {
    font-size: 1.25rem;
    margin-bottom: 1rem;
    color: #fff;
}

.feature-card p {
    color: var(--text-muted);
    font-size: 1rem;
    margin-bottom: 1.5rem;
}

.feature-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.feature-tags span {
    background: rgba(255, 255, 255, 0.05);
    padding: 0.3rem 0.6rem;
    border-radius: 4px;
    font-size: 0.8rem;
    color: #cbd5e1;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

/* EXAMPLES */
.examples-section {
    background: radial-gradient(circle at left center, rgba(16, 185, 129, 0.03), transparent 60%);
}

.examples-dashboard {
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 2rem;
    background: #11141a;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
}

.ex-sidebar {
    padding: 1rem;
    border-right: 1px solid var(--border);
}

.ex-site-info h4, .ex-detected h4 {
    font-size: 0.8rem;
    color: var(--text-muted);
    text-transform: uppercase;
    margin-bottom: 0.75rem;
    letter-spacing: 0.5px;
}

.ex-site-info a {
    color: var(--primary);
    text-decoration: none;
    font-weight: 600;
    display: block;
    margin-bottom: 0.75rem;
    font-size: 1.05rem;
}

.ex-status {
    color: var(--functional);
    font-size: 0.9rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 2.5rem;
    font-weight: 600;
}

.ex-detected ul {
    list-style: none;
}

.ex-detected li {
    font-size: 0.95rem;
    color: #e2e8f0;
    margin-bottom: 0.6rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.ex-detected i {
    color: var(--text-muted);
    font-size: 0.7rem;
}

.ex-main {
    padding: 1rem;
}

.ex-tabs {
    display: flex;
    gap: 0.75rem;
    margin-bottom: 2rem;
    border-bottom: 1px solid var(--border);
    padding-bottom: 1.5rem;
}

.ex-tab {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--text-muted);
    padding: 0.5rem 1.25rem;
    border-radius: 4px;
    font-size: 0.85rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
}

.ex-tab.active, .ex-tab:hover {
    background: var(--bg-card);
    color: white;
    border-color: var(--primary);
}

.ex-list {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.ex-card {
    background-color: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 768px) {
    .product-grid, .examples-dashboard {
        grid-template-columns: 1fr;
    }
    .ex-sidebar {
        border-right: none;
        border-bottom: 1px solid var(--border);
        padding-bottom: 2rem;
    }
    .timeline-container {
        padding-left: 1.5rem;
    }
}
"""

with open("static/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

css = re.sub(
    r"/\* Info Sections \*/.*", 
    css_replacement, 
    css, 
    flags=re.DOTALL
)

with open("static/css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updates applied successfully.")
