# 🚀 Cloudflare Pages Deployment Guide

## Step 1: Sign up Cloudflare Pages

1. **Truy cập:** https://pages.cloudflare.com/
2. **Click:** "Sign up" (hoặc "Log in" nếu đã có account)
3. **Verify email:** Check email và verify

✅ **Free forever - No credit card needed!**

---

## Step 2: Connect GitHub

1. **Click:** "Create a project"
2. **Click:** "Connect to Git"
3. **Choose:** GitHub
4. **Authorize:** Cloudflare Pages to access GitHub
5. **Select repository:** `trieuhiencomp-dev/zaptools`

---

## Step 3: Configure Build Settings

```yaml
Project name: zaptools
Production branch: main

Build settings:
  Framework preset: None (Static HTML)
  Build command: (leave empty)
  Build output directory: /
  Root directory: (leave empty)

Environment variables: (none needed)
```

**Important:**
- NO build command needed (already built)
- Output directory is `/` (root)
- Framework preset: **None**

---

## Step 4: Deploy!

1. **Click:** "Save and Deploy"
2. **Wait:** ~30 seconds
3. **Done!** ✅

Your site will be live at:
```
https://zaptools.pages.dev
```

---

## Step 5: Custom Domain (zaptools.org)

### Add Custom Domain:

1. Go to: **Pages → zaptools → Custom domains**
2. Click: **"Set up a custom domain"**
3. Enter: `zaptools.org`
4. Click: **"Continue"**

### Two Options:

#### Option A: Cloudflare manages your domain (RECOMMENDED)
```
1. Transfer nameservers to Cloudflare
2. Cloudflare will show you 2 nameservers:
   - Example: emma.ns.cloudflare.com
   - Example: walt.ns.cloudflare.com
3. Go to your domain registrar
4. Update nameservers
5. Wait 24-48 hours for propagation
```

#### Option B: Add CNAME record
```
1. Go to your DNS provider
2. Add CNAME record:
   Name: @
   Target: zaptools.pages.dev
3. Add CNAME for www:
   Name: www
   Target: zaptools.pages.dev
```

---

## Step 6: Enable HTTPS (Auto)

Cloudflare automatically provisions SSL certificate:
- ✅ Free SSL/TLS
- ✅ Auto-renew
- ✅ Full encryption

Wait 10-15 minutes after domain setup.

---

## Step 7: Optimize Settings

### Enable in Cloudflare Dashboard:

1. **Auto Minify:**
   - Speed → Optimization → Auto Minify
   - ✅ JavaScript
   - ✅ CSS
   - ✅ HTML

2. **Brotli Compression:**
   - Speed → Optimization → Brotli
   - ✅ Enable

3. **Rocket Loader:**
   - Speed → Optimization → Rocket Loader
   - ✅ Enable (optional, test first)

4. **HTTP/3:**
   - Network → HTTP/3
   - ✅ Enable

5. **Caching:**
   - Caching → Configuration
   - Caching Level: **Standard**
   - Browser Cache TTL: **4 hours**

---

## ✅ Verification Checklist

After deployment, test these:

- [ ] Homepage loads: https://zaptools.org
- [ ] All 8 new tools work
- [ ] OG images load
- [ ] Mobile responsive
- [ ] HTTPS works
- [ ] Google Analytics tracks
- [ ] No console errors

---

## 🎯 Expected Results

**Before (Netlify):**
- ❌ Bandwidth: 100 GB/month (exceeded)
- ❌ Site paused
- ⏱️ Load time: ~1.2s

**After (Cloudflare Pages):**
- ✅ Bandwidth: UNLIMITED
- ✅ Site always online
- ⚡ Load time: ~0.4s (3x faster!)
- ✅ Global CDN
- ✅ DDoS protection

---

## 🔥 Pro Tips

### 1. Enable "Always Online"
```
Caching → Configuration → Always Online
→ Serves cached version if origin is down
```

### 2. Setup Page Rules (Free: 3 rules)
```
Rule 1: Cache Everything
- URL: zaptools.org/*
- Cache Level: Cache Everything

Rule 2: Force HTTPS
- URL: http://zaptools.org/*
- Always Use HTTPS

Rule 3: Optimize Images
- URL: zaptools.org/og-images/*
- Polish: Lossless
```

### 3. Enable Web Analytics
```
Analytics → Web Analytics
→ Free, privacy-friendly analytics
→ Alternative to Google Analytics
```

### 4. Setup Email Routing (Free)
```
Email → Email Routing
→ Forward hello@zaptools.org to your email
→ Professional email for free!
```

---

## 🚨 Troubleshooting

### Issue: "Build failed"
**Solution:**
- Set build command to: (empty)
- Set output directory to: /
- Framework: None

### Issue: "Domain not working"
**Solution:**
- Wait 24 hours for DNS propagation
- Clear browser cache
- Try incognito mode
- Check DNS with: https://dnschecker.org

### Issue: "SSL certificate pending"
**Solution:**
- Wait 15 minutes
- Disable proxy (orange cloud) temporarily
- Re-enable after certificate issued

### Issue: "404 errors"
**Solution:**
- Check build output directory is `/`
- Make sure all files are in root
- Verify Git repository structure

---

## 📞 Support

**Cloudflare Docs:** https://developers.cloudflare.com/pages/
**Community:** https://community.cloudflare.com/
**Status:** https://www.cloudflarestatus.com/

---

## 🎉 Success!

Once deployed, your site will have:
- ✅ Unlimited bandwidth
- ✅ Unlimited requests
- ✅ Global CDN (275+ cities)
- ✅ DDoS protection
- ✅ SSL/TLS automatic
- ✅ 99.99% uptime
- ✅ Zero cost

**Welcome to Cloudflare Pages! 🚀**

---

*Last updated: December 4, 2024*
