# 📧 Hướng Dẫn Setup Feedback Form

## CÁCH 1: FORMSPREE (Khuyên dùng - Dễ nhất)

### Bước 1: Tạo tài khoản Formspree
1. Truy cập: https://formspree.io/
2. Đăng ký tài khoản miễn phí
3. Click "New Form"

### Bước 2: Lấy Form ID
1. Sau khi tạo form, bạn sẽ được cung cấp một endpoint URL
2. URL có dạng: `https://formspree.io/f/YOUR_FORM_ID`
3. Copy phần `YOUR_FORM_ID` (ví dụ: `xpzvpqlr`)

### Bước 3: Cập nhật feedback.html
Mở file `feedback.html` và thay thế:
```html
<form id="feedbackForm" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
```

Thành:
```html
<form id="feedbackForm" action="https://formspree.io/f/xpzvpqlr" method="POST">
```
(Thay `xpzvpqlr` bằng Form ID của bạn)

### Bước 4: Xong!
- Mọi feedback sẽ được gửi đến email bạn đăng ký Formspree
- Free plan: 50 submissions/tháng
- Không cần code backend!

---

## CÁCH 2: EMAILJS (Alternative)

### Bước 1: Tạo tài khoản EmailJS
1. Truy cập: https://www.emailjs.com/
2. Đăng ký miễn phí
3. Connect email service (Gmail, Outlook, etc.)

### Bước 2: Setup
1. Tạo Email Template
2. Lấy Service ID, Template ID, Public Key
3. Thêm vào feedback.html:

```javascript
emailjs.init("YOUR_PUBLIC_KEY");

emailjs.send("YOUR_SERVICE_ID", "YOUR_TEMPLATE_ID", {
    from_name: name,
    from_email: email,
    subject: subject,
    message: message,
    feedback_type: feedbackType
});
```

Free plan: 200 emails/tháng

---

## CÁCH 3: GOOGLE SHEETS (Miễn phí vĩnh viễn)

### Sử dụng Google Apps Script để lưu vào Google Sheets

1. Tạo Google Sheet mới
2. Tools > Script Editor
3. Paste code Apps Script
4. Deploy as Web App
5. Lấy URL và thay vào feedback.html

---

## CÁCH 4: BACKEND RIÊNG

### Node.js + Express + Nodemailer
```javascript
app.post('/api/feedback', async (req, res) => {
    const { name, email, subject, message, feedbackType } = req.body;

    // Send email using Nodemailer
    await transporter.sendMail({
        from: 'noreply@zaptools.org',
        to: 'your-email@example.com',
        subject: `[${feedbackType}] ${subject}`,
        text: `From: ${name} (${email})\n\n${message}`
    });

    res.json({ success: true });
});
```

---

## 📊 XEM FEEDBACK Ở ĐÂU?

### Formspree:
- Dashboard: https://formspree.io/forms
- Email: Tự động gửi về email của bạn

### EmailJS:
- Dashboard: https://dashboard.emailjs.com/
- Email: Được forward về email

### Google Sheets:
- Mở Sheet để xem trực tiếp

### Backend riêng:
- Database của bạn
- Admin panel tự tạo

---

## 🎯 KHUYẾN NGHỊ

**Dùng FORMSPREE nếu:**
- ✅ Bạn muốn setup nhanh (5 phút)
- ✅ Không cần backend
- ✅ <= 50 feedback/tháng (free)
- ✅ Nhận qua email là đủ

**Dùng BACKEND RIÊNG nếu:**
- ✅ Cần lưu database
- ✅ Cần custom logic
- ✅ Cần admin panel
- ✅ Nhiều hơn 50 feedback/tháng

---

## 📞 HỖ TRỢ

Nếu cần giúp setup, liên hệ hoặc xem docs:
- Formspree: https://help.formspree.io/
- EmailJS: https://www.emailjs.com/docs/
