# 🚀 SETUP FEEDBACK - SIÊU ĐỔN GIẢN (3 phút)

## ✅ CÁCH 1: WEB3FORMS (KHÔNG CẦN VERIFY EMAIL!)

### Bước 1: Lấy Access Key (30 giây)
1. Truy cập: **https://web3forms.com**
2. Nhập email của bạn
3. Click "Create Access Key"
4. **Lấy ngay Access Key** (không cần verify!)

### Bước 2: Cập nhật feedback.html (1 phút)
Mở `feedback.html`, tìm dòng 329:
```html
<input type="hidden" name="access_key" value="YOUR_ACCESS_KEY_HERE">
```

Thay `YOUR_ACCESS_KEY_HERE` bằng Access Key vừa lấy:
```html
<input type="hidden" name="access_key" value="abc123xyz-your-real-key">
```

### Bước 3: XONG! 🎉
- Feedback tự động gửi về email
- **KHÔNG CẦN VERIFY EMAIL!**
- Free: **250 emails/tháng**
- Không cần đăng ký tài khoản

---

## ✅ CÁCH 2: GOOGLE FORMS (DỄ NHẤT!)

### Bước 1: Tạo Google Form
1. Truy cập: **https://forms.google.com**
2. Click "Blank form" hoặc "+" để tạo mới
3. Đặt tên: "ZapTools Feedback"

### Bước 2: Thêm câu hỏi
Thêm các field:
- **Name** (Short answer)
- **Email** (Short answer)
- **Feedback Type** (Multiple choice: Suggestion, Bug, Feature, Other)
- **Subject** (Short answer)
- **Message** (Paragraph)

### Bước 3: Lấy link
1. Click "Send" ở góc phải
2. Click icon "Link" 🔗
3. Click "Shorten URL"
4. Copy link (dạng: `forms.gle/abc123`)

### Bước 4: Cập nhật feedback.html
Tìm dòng 259:
```html
<a href="https://forms.gle/YOUR_GOOGLE_FORM_ID" target="_blank"
```

Thay bằng link vừa copy:
```html
<a href="https://forms.gle/abc123xyz" target="_blank"
```

### Bước 5: XONG!
- Xem feedback trong Google Sheets tự động
- **HOÀN TOÀN MIỄN PHÍ**
- Không giới hạn số lượng
- Có email notification

---

## 📊 XEM FEEDBACK Ở ĐÂU?

### Web3Forms:
- Email → Feedback gửi trực tiếp về email bạn
- Dashboard: https://web3forms.com/

### Google Forms:
- Responses tab trong Google Form
- Hoặc xem trong Google Sheets (tự động tạo)
- Email notification (bật trong Settings)

---

## 🎯 KHUYẾN NGHỊ

### Dùng WEB3FORMS nếu:
✅ Muốn form ngay trên website
✅ Nhận qua email
✅ Setup 3 phút
✅ **KHÔNG CẦN VERIFY EMAIL**

### Dùng GOOGLE FORMS nếu:
✅ Muốn dễ nhất có thể
✅ Miễn phí vĩnh viễn
✅ Không giới hạn
✅ Xem trong Sheets

---

## ⚡ QUICK START (Chọn 1 trong 2)

### Option A: Web3Forms
```bash
1. Vào web3forms.com
2. Nhập email → Get Access Key
3. Paste vào feedback.html dòng 329
4. Save → Done!
```

### Option B: Google Forms
```bash
1. Vào forms.google.com
2. Tạo form mới
3. Get link
4. Paste vào feedback.html dòng 259
5. Save → Done!
```

---

## 🆘 CẦN GIÚP?

**Web3Forms docs:** https://docs.web3forms.com/
**Google Forms help:** https://support.google.com/docs/answer/6281888

**Hoặc hỏi tôi!** 😊
