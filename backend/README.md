# 🎙️ ZapTools TTS Backend

Text-to-Speech backend using **Azure Cognitive Services** (FREE tier)

**Chi phí:** $0/tháng (5M ký tự miễn phí)

---

## ⚡ Quick Start

```bash
# 1. Install
npm install

# 2. Configure (get FREE key from portal.azure.com)
copy .env.example .env
# Edit .env với Azure key

# 3. Test
npm test

# 4. Start
npm start
```

**Server:** http://localhost:3000

---

## 📚 Documentation

- **Setup Guide:** [`../TTS-SETUP-GUIDE.md`](../TTS-SETUP-GUIDE.md)
- **Implementation:** [`../TTS-IMPLEMENTATION-SUMMARY.md`](../TTS-IMPLEMENTATION-SUMMARY.md)

---

## 🔑 Get FREE Azure Key

1. Go to: https://portal.azure.com
2. Create "Speech" resource (FREE F0 tier)
3. Copy KEY + REGION
4. Paste into `.env`

**Free tier:** 5,000,000 characters/month

---

## 📡 API Endpoints

### POST /api/tts/convert
```bash
curl -X POST http://localhost:3000/api/tts/convert \
  -H "Content-Type: application/json" \
  -d '{"text": "Xin chào", "voice": "vi-VN-HoaiMyNeural"}'
```

### GET /api/tts/voices
```bash
curl http://localhost:3000/api/tts/voices
```

### GET /api/tts/stats
```bash
curl http://localhost:3000/api/tts/stats
```

---

## 🏗️ Architecture

```
tts-api.js          ← Main server
├── azure-tts.js    ← Azure API integration
├── cache-manager.js ← File caching (70-80% hit rate)
└── rate-limiter.js  ← 10 req/hour per IP
```

---

## 💰 Cost

**FREE tier:** 5M chars/month

**With 75% cache hit rate:**
- Support: ~600 users/day
- Cost: **$0/month** ✅

**When exceed FREE tier:**
- Neural voices: $16/1M chars
- Example: 12M chars = $112/month

---

## 📊 Features

✅ Azure TTS API (Vietnamese voices)
✅ File-based caching (no Redis needed)
✅ Rate limiting (anti-abuse)
✅ Usage statistics
✅ FREE tier monitoring
✅ Auto cache cleanup

---

## 🧪 Testing

```bash
npm test
```

Expected output:
```
✅ Azure TTS works!
✅ Cache save/retrieve works!
✅ Rate limiting works!
🎉 All tests passed!
```

---

## 🚀 Deploy

### Vercel (Free)
```bash
vercel deploy
```

### Railway (Free tier)
```bash
railway up
```

### Render (Free tier)
```bash
# Connect GitHub repo
# Auto-deploy on push
```

---

## 🔧 Environment Variables

```env
AZURE_TTS_KEY=your_azure_key
AZURE_TTS_REGION=southeastasia
PORT=3000
NODE_ENV=production
ADMIN_KEY=your_admin_password
```

---

## 📞 Support

- **Issues:** Open GitHub issue
- **Email:** trieuhiencomp@gmail.com
- **Docs:** See TTS-SETUP-GUIDE.md

---

**ZapTools.org** • Lightning-Fast Free Tools
