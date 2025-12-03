// Feedback Widget for ZapTools
// Add this script to all pages to enable user feedback

(function() {
    // Create feedback button HTML
    const feedbackHTML = `
        <div id="zaptools-feedback-widget">
            <!-- Floating Feedback Button -->
            <button id="feedback-btn" class="feedback-floating-btn" title="Góp ý / Feedback">
                💬
            </button>

            <!-- Feedback Modal -->
            <div id="feedback-modal" class="feedback-modal" style="display:none;">
                <div class="feedback-modal-content">
                    <span class="feedback-close">&times;</span>
                    <h2 id="feedback-title">📝 Góp ý của bạn</h2>
                    <p id="feedback-subtitle">Gửi ý kiến, báo lỗi hoặc đề xuất tính năng mới!</p>

                    <form id="feedback-form">
                        <div class="feedback-group">
                            <label id="feedback-name-label">Tên của bạn (tùy chọn):</label>
                            <input type="text" id="feedback-name" placeholder="Nhập tên...">
                        </div>

                        <div class="feedback-group">
                            <label id="feedback-email-label">Email (tùy chọn):</label>
                            <input type="email" id="feedback-email" placeholder="email@example.com">
                        </div>

                        <div class="feedback-group">
                            <label id="feedback-type-label">Loại góp ý:</label>
                            <select id="feedback-type" required>
                                <option value="bug">🐛 Báo lỗi</option>
                                <option value="feature">✨ Đề xuất tính năng</option>
                                <option value="feedback">💡 Góp ý</option>
                                <option value="other">📌 Khác</option>
                            </select>
                        </div>

                        <div class="feedback-group">
                            <label id="feedback-message-label">Nội dung: <span style="color:red;">*</span></label>
                            <textarea id="feedback-message" rows="5" placeholder="Nhập góp ý của bạn..." required></textarea>
                        </div>

                        <div id="feedback-result" style="margin-bottom:10px;"></div>

                        <button type="submit" class="feedback-submit-btn" id="feedback-submit">
                            <span id="feedback-submit-text">Gửi góp ý</span>
                        </button>
                    </form>
                </div>
            </div>
        </div>

        <style>
            /* Floating Button */
            .feedback-floating-btn {
                position: fixed;
                bottom: 20px;
                right: 20px;
                width: 60px;
                height: 60px;
                border-radius: 50%;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border: none;
                font-size: 28px;
                cursor: pointer;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3);
                z-index: 9998;
                transition: transform 0.2s, box-shadow 0.2s;
            }

            .feedback-floating-btn:hover {
                transform: scale(1.1);
                box-shadow: 0 6px 16px rgba(0,0,0,0.4);
            }

            /* Modal */
            .feedback-modal {
                display: none;
                position: fixed;
                z-index: 9999;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0,0,0,0.6);
                backdrop-filter: blur(4px);
            }

            .feedback-modal-content {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 5% auto;
                padding: 30px;
                border-radius: 20px;
                max-width: 500px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.4);
                position: relative;
                color: white;
            }

            .feedback-close {
                position: absolute;
                right: 20px;
                top: 15px;
                font-size: 32px;
                font-weight: bold;
                cursor: pointer;
                color: white;
                opacity: 0.8;
                transition: opacity 0.2s;
            }

            .feedback-close:hover {
                opacity: 1;
            }

            .feedback-group {
                margin-bottom: 15px;
            }

            .feedback-group label {
                display: block;
                margin-bottom: 5px;
                font-weight: 600;
            }

            .feedback-group input,
            .feedback-group textarea,
            .feedback-group select {
                width: 100%;
                padding: 10px;
                border: none;
                border-radius: 8px;
                font-size: 14px;
                font-family: inherit;
            }

            .feedback-submit-btn {
                width: 100%;
                padding: 12px;
                background: white;
                color: #667eea;
                border: none;
                border-radius: 10px;
                font-size: 16px;
                font-weight: 600;
                cursor: pointer;
                transition: transform 0.2s;
            }

            .feedback-submit-btn:hover {
                transform: scale(1.02);
            }

            .feedback-submit-btn:disabled {
                opacity: 0.6;
                cursor: not-allowed;
            }

            @media (max-width: 600px) {
                .feedback-modal-content {
                    margin: 10% 10px;
                    padding: 20px;
                }
            }
        </style>
    `;

    // Insert HTML into page
    document.addEventListener('DOMContentLoaded', function() {
        document.body.insertAdjacentHTML('beforeend', feedbackHTML);

        // Get elements
        const feedbackBtn = document.getElementById('feedback-btn');
        const modal = document.getElementById('feedback-modal');
        const closeBtn = document.querySelector('.feedback-close');
        const form = document.getElementById('feedback-form');
        const resultDiv = document.getElementById('feedback-result');
        const submitBtn = document.getElementById('feedback-submit');

        // Language support
        const lang = localStorage.getItem('zaptools_lang') || 'vi';
        const langData = {
            vi: {
                title: '📝 Góp ý của bạn',
                subtitle: 'Gửi ý kiến, báo lỗi hoặc đề xuất tính năng mới!',
                nameLabel: 'Tên của bạn (tùy chọn):',
                emailLabel: 'Email (tùy chọn):',
                typeLabel: 'Loại góp ý:',
                messageLabel: 'Nội dung:',
                submitText: 'Gửi góp ý',
                sending: 'Đang gửi...',
                success: '✅ Cảm ơn bạn! Góp ý đã được gửi.',
                error: '❌ Có lỗi xảy ra. Vui lòng thử lại!'
            },
            en: {
                title: '📝 Your Feedback',
                subtitle: 'Send feedback, report bugs, or suggest new features!',
                nameLabel: 'Your name (optional):',
                emailLabel: 'Email (optional):',
                typeLabel: 'Feedback type:',
                messageLabel: 'Message:',
                submitText: 'Submit Feedback',
                sending: 'Sending...',
                success: '✅ Thank you! Feedback sent successfully.',
                error: '❌ An error occurred. Please try again!'
            }
        };

        // Apply language
        document.getElementById('feedback-title').textContent = langData[lang].title;
        document.getElementById('feedback-subtitle').textContent = langData[lang].subtitle;
        document.getElementById('feedback-name-label').textContent = langData[lang].nameLabel;
        document.getElementById('feedback-email-label').textContent = langData[lang].emailLabel;
        document.getElementById('feedback-type-label').textContent = langData[lang].typeLabel;
        document.getElementById('feedback-message-label').innerHTML = langData[lang].messageLabel + ' <span style="color:red;">*</span>';
        document.getElementById('feedback-submit-text').textContent = langData[lang].submitText;

        // Open modal
        feedbackBtn.onclick = function() {
            modal.style.display = 'block';
        };

        // Close modal
        closeBtn.onclick = function() {
            modal.style.display = 'none';
        };

        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = 'none';
            }
        };

        // Submit form
        form.onsubmit = async function(e) {
            e.preventDefault();

            const name = document.getElementById('feedback-name').value || 'Anonymous';
            const email = document.getElementById('feedback-email').value || 'N/A';
            const type = document.getElementById('feedback-type').value;
            const message = document.getElementById('feedback-message').value;

            // Disable submit button
            submitBtn.disabled = true;
            document.getElementById('feedback-submit-text').textContent = langData[lang].sending;

            try {
                const response = await fetch('https://zaptools-backend.as.r.appspot.com/api/feedback', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        name: name,
                        email: email,
                        type: type,
                        message: message,
                        url: window.location.href,
                        timestamp: new Date().toISOString()
                    })
                });

                if (response.ok) {
                    resultDiv.innerHTML = `<div style="color:#4ade80;font-weight:600;">${langData[lang].success}</div>`;
                    form.reset();

                    // Close modal after 2 seconds
                    setTimeout(() => {
                        modal.style.display = 'none';
                        resultDiv.innerHTML = '';
                    }, 2000);
                } else {
                    throw new Error('Server error');
                }
            } catch (error) {
                resultDiv.innerHTML = `<div style="color:#fca5a5;font-weight:600;">${langData[lang].error}</div>`;
            } finally {
                submitBtn.disabled = false;
                document.getElementById('feedback-submit-text').textContent = langData[lang].submitText;
            }
        };
    });
})();
