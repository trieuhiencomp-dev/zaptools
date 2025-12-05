# 🎙️ TTS Backend Setup Guide - 100% MIỄN PHÍ

Hướng dẫn setup TTS backend sử dụng Azure Free Tier (5M ký tự/tháng = $0)

---

## 📋 Yêu Cầu

- ✅ Node.js 14+ (Download: https://nodejs.org)
- ✅ Tài khoản Microsoft/Azure (FREE)
- ✅ 15 phút setup

---

## 🔑 BƯỚC 1: Lấy Azure TTS Key MIỄN PHÍ

### 1.1. Tạo Azure Account

1. Truy cập: https://portal.azure.com
2. Click **"Start Free"** hoặc **"Bắt đầu miễn phí"**
3. Đăng nhập bằng:
   - Microsoft account (Outlook/Hotmail)
   - Hoặc tạo mới

**Lưu ý:**
- ✅ KHÔNG cần thẻ tín dụng cho Free tier
- ✅ Hoàn toàn miễn phí mãi mãi (không hết hạn)
- ✅ 5 triệu ký tự/tháng

### 1.2. Tạo Speech Resource (FREE)

1. Sau khi đăng nhập Azure Portal
2. Click **"+ Create a resource"** (góc trái trên)
3. Search: **"Speech"**
4. Click **"Speech"** → **"Create"**

5. **Điền thông tin:**
   ```
   Subscription: Free Trial (hoặc Pay-As-You-Go)
   Resource group: Tạo mới "zaptools-rg"
   Region: Southeast Asia (gần Việt Nam nhất)
   Name: zaptools-tts
   Pricing tier: FREE F0 ⭐ (QUAN TRỌNG - Chọn FREE!)
   ```

6. Click **"Review + Create"**
7. Click **"Create"**
8. Đợi 1-2 phút deploy xong

### 1.3. Copy Key & Region

1. Vào resource vừa tạo: **"zaptools-tts"**
2. Bên trái, click **"Keys and Endpoint"**
3. Copy:
   - **KEY 1** (hoặc KEY 2): `abc123xyz...`
   - **Location/Region**: `southeastasia`

**Ảnh chụp màn hình:**
```
Keys and Endpoint
├─ KEY 1: ••••••••••••••••••••••••••••  [Show] [Copy]
├─ KEY 2: ••••••••••••••••••••••••••••  [Show] [Copy]
└─ Location/Region: southeastasia
```

**👉 Lưu lại KEY và REGION này!**

---

## 🛠️ BƯỚC 2: Setup Backend

### 2.1. Install Dependencies

```bash
cd Y:\zaptools\backend

# Install packages
npm install

# Hoặc nếu chưa có node_modules
npm install express cors node-fetch dotenv
```

### 2.2. Tạo file .env

```bash
# Copy file mẫu
copy .env.example .env

# Hoặc tạo mới file .env
notepad .env
```

**Nội dung file `.env`:**
```env
AZURE_TTS_KEY=paste_key_từ_bước_1.3_vào_đây
AZURE_TTS_REGION=southeastasia
PORT=3000
NODE_ENV=development
ADMIN_KEY=zaptools_admin_2025
```

**Ví dụ thực tế:**
```env
AZURE_TTS_KEY=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
AZURE_TTS_REGION=southeastasia
PORT=3000
NODE_ENV=development
ADMIN_KEY=my_secret_password_123
```

### 2.3. Tạo Cache Folder

```bash
mkdir cache
mkdir cache\tts
```

Hoặc tự động tạo khi chạy lần đầu.

---

## ✅ BƯỚC 3: Test Backend

### 3.1. Run Test Script

```bash
cd Y:\zaptools\backend
npm test
```

**Kết quả mong đợi:**
```
╔════════════════════════════════════════╗
║   ZapTools TTS Backend Tests          ║
╚════════════════════════════════════════╝

🧪 Testing Azure TTS...
📝 Converting text: Xin chào, đây là test giọng đọc tiếng Việt.
✅ Azure TTS works!
   Audio size: 45632 bytes
   Characters: 44

🧪 Testing Cache Manager...
✅ Cache save works!
✅ Cache retrieve works!
✅ Cache stats: { hit: 1, miss: 0, ... }

🧪 Testing Rate Limiter...
✅ First request allowed: true
✅ Second request allowed: true
   Remaining (hourly): 8

╔════════════════════════════════════════╗
║   Test Results                         ║
╠════════════════════════════════════════╣
║ Azure TTS:       ✅ PASS               ║
║ Cache Manager:   ✅ PASS               ║
║ Rate Limiter:    ✅ PASS               ║
╚════════════════════════════════════════╝

🎉 All tests passed! Backend ready to use.
```

**Nếu lỗi:**
- ❌ **"Invalid subscription key"**: Sai AZURE_TTS_KEY → Check lại
- ❌ **"Invalid region"**: Sai AZURE_TTS_REGION → Phải là `southeastasia`
- ❌ **"ENOENT"**: Chưa tạo folder cache

---

## 🚀 BƯỚC 4: Start Server

```bash
npm start
```

**Kết quả:**
```
╔════════════════════════════════════════╗
║   ZapTools TTS API - FREE TIER        ║
║   🎙️  Azure Cognitive Services        ║
║   💾  File-based caching              ║
║   🛡️  Rate limiting enabled            ║
╚════════════════════════════════════════╝

✅ Server running on http://localhost:3000
✅ FREE tier: 5M chars/month
✅ Cache hit rate target: 70-80%

Endpoints:
  POST   /api/tts/convert        - Convert text to speech
  GET    /api/tts/voices         - Get available voices
  GET    /api/tts/stats          - Get usage stats
  GET    /health                 - Health check
```

---

## 🧪 BƯỚC 5: Test API

### 5.1. Test với Postman hoặc Curl

**Request:**
```bash
curl -X POST http://localhost:3000/api/tts/convert \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"Xin chào ZapTools\", \"voice\": \"vi-VN-HoaiMyNeural\"}"
```

**Response:**
```json
{
  "success": true,
  "fromCache": false,
  "audioUrl": "/cache/tts/a1b2c3d4e5f6.mp3",
  "charCount": 18,
  "remaining": {
    "hourly": 9,
    "daily": 49
  },
  "message": "Converted successfully"
}
```

### 5.2. Test trong Browser

1. Mở: http://localhost:3000/health
2. Thấy: `{"status": "ok", ...}`
3. Mở: http://localhost:3000/api/tts/voices
4. Thấy danh sách giọng đọc

---

## 📊 BƯỚC 6: Monitor Usage (FREE Tier)

### 6.1. Check Stats

```bash
curl http://localhost:3000/api/tts/stats
```

**Response:**
```json
{
  "success": true,
  "cache": {
    "hit": 150,
    "miss": 50,
    "hitRate": "75.00%",
    "charsSaved": 45000,
    "charsUsed": 15000,
    "freeTier": {
      "limit": 5000000,
      "used": 15000,
      "remaining": 4985000,
      "percentUsed": "0.30%",
      "status": "✅ FREE"
    }
  },
  "rateLimit": {
    "totalIPs": 25,
    "activeUsersLastHour": 10,
    "totalRequests": 200
  }
}
```

### 6.2. Azure Portal Dashboard

1. Vào: https://portal.azure.com
2. Mở resource: **"zaptools-tts"**
3. Bên trái: **"Metrics"**
4. Xem:
   - Total Calls
   - Characters Processed
   - Errors

**Theo dõi:**
- ✅ < 5M chars/tháng = FREE
- ⚠️ > 5M chars/tháng = Bị charge tiền

---

## 💰 DỰ TOÁN SỬ DỤNG

### FREE Tier Limit: 5,000,000 chars/tháng

**Kịch bản 1: 500 users/ngày**
```
500 users/day × 2 conversions × 500 chars = 500k chars/day
= 15M chars/month
→ Vượt FREE tier!
```

**Giải pháp: Caching 75%**
```
15M chars/month × 25% (only miss) = 3.75M chars/month
→ Vẫn FREE! ✅
```

**Kịch bản 2: 2000 users/ngày (sau 1 năm)**
```
2000 users/day × 2 conversions × 500 chars = 2M chars/day
= 60M chars/month
→ Cần caching 92% để FREE!
```

**Với caching tốt (80%):**
```
60M × 20% = 12M chars/month
→ Chi phí: $112/month (Neural voices $16/1M chars)
```

**👉 Kết luận:** Tháng 1-6 hoàn toàn FREE với caching tốt!

---

## 🔧 TROUBLESHOOTING

### Lỗi 1: "Module not found"
```bash
npm install
```

### Lỗi 2: "Invalid subscription key"
```
→ Check file .env
→ AZURE_TTS_KEY phải đúng (copy từ Azure Portal)
```

### Lỗi 3: "ENOENT: no such file or directory, open cache"
```bash
mkdir cache
mkdir cache\tts
```

### Lỗi 4: "Port 3000 already in use"
```
→ Đổi PORT trong .env
→ Hoặc kill process đang dùng port 3000
```

### Lỗi 5: Cache không hoạt động
```bash
# Clear cache và test lại
rm -rf cache/tts/*
npm test
```

---

## 🎯 NEXT STEPS

1. ✅ Integrate frontend (tts-tool.html)
2. ✅ Deploy backend lên cloud:
   - Vercel (free)
   - Railway (free tier)
   - Render (free tier)
3. ✅ Monitor usage daily
4. ✅ Optimize caching (target 80%+ hit rate)

---

## 📞 Support

Nếu gặp vấn đề:
1. Check console logs
2. Run `npm test` để verify
3. Check Azure Portal → Metrics
4. Email: trieuhiencomp@gmail.com

---

**Chúc bạn setup thành công! 🎉**

*ZapTools.org • 2025 • Lightning-Fast Free Tools*
