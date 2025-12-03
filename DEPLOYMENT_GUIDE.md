# ZapTools Deployment Guide

## 📋 Tổng quan
Project đã được chuẩn bị sẵn sàng để deploy:
- **Backend**: Google Cloud App Engine (Flex environment with Docker)
- **Frontend**: Netlify

---

## 🔧 Backend Deployment (Google Cloud)

### Trạng thái: ĐANG DEPLOY ⏳

Backend đang được deploy tự động đến Google Cloud App Engine:
- **Project**: zaptools-backend
- **URL**: https://zaptools-backend.as.r.appspot.com
- **Environment**: Flex (Custom Docker với poppler-utils, LibreOffice, tesseract-ocr)

### Các file cấu hình:
- `backend/Dockerfile` - Custom Docker image với full PDF processing support
- `backend/app.yaml` - Google App Engine configuration
- `backend/requirements.txt` - Python dependencies (đã sửa duplicates)

### Kiểm tra deployment:
```bash
# Xem logs
gcloud app logs tail -s default

# Xem trạng thái
gcloud app browse
```

---

## 🌐 Frontend Deployment (Netlify)

### Phương pháp 1: Netlify CLI (đang gặp lỗi với nested directories)

```bash
cd Y:\zaptools
netlify deploy --prod
```

⚠️ **Lỗi hiện tại**: Maximum call stack size exceeded (do thư mục backend nested)

### Phương pháp 2: Netlify Web Interface (KHUYẾN NGHỊ)

1. **Truy cập**: https://app.netlify.com
2. **Chọn site**: zaptools (Site ID: 39b3e889-93f4-41d7-8df9-3bcab5f1fbe1)
3. **Deploy methods**:

   **Option A: Git Integration** (Tự động)
   - Kết nối repository với Netlify
   - Mỗi lần push code sẽ tự động deploy

   **Option B: Manual Deploy** (Drag & Drop)
   - Vào tab "Deploys"
   - Kéo thả các files HTML vào (không bao gồm thư mục backend)
   - Hoặc upload zip file

### Các files cần deploy (Frontend):
```
✅ Index.html
✅ image-tool.html
✅ GiaiMaQR.html
✅ pdf-tools.html
✅ PDFtoImage.html
✅ PDFtoPowerpoint.html
✅ PDFtoWord.html
✅ PDFtoExcel.html
✅ MergePDFs.html
✅ SplitPDF.html
✅ PDFresize.html
✅ QRcode.html
✅ QRcontact.html
✅ QRevent.html
✅ QRlinkweb.html
✅ QRproduct.html
✅ QRwifi.html
✅ DanhSachTaoQR.html
✅ ImageCompress.html (MỚI)
✅ ImageResize.html (MỚI)
✅ ImageConvert.html (MỚI)
✅ netlify.toml
✅ _redirects

❌ backend/ (KHÔNG deploy - riêng biệt trên Google Cloud)
```

### Phương pháp 3: Netlify CLI với thư mục tạm

Nếu muốn dùng CLI, tạo thư mục tạm không có backend:

```bash
# Tạo thư mục deploy tạm
mkdir Y:\zaptools-deploy
cd Y:\zaptools-deploy

# Copy files cần thiết (không bao gồm backend)
xcopy Y:\zaptools\*.html .
xcopy Y:\zaptools\netlify.toml .
xcopy Y:\zaptools\_redirects .

# Deploy
netlify deploy --prod --dir .
```

---

## ✅ Kiểm tra sau khi deploy

### Backend:
1. Truy cập https://zaptools-backend.as.r.appspot.com
2. Kiểm tra API endpoints:
   - `/` - Should return "ZapTools Backend is running!"
   - `/api/pdf-to-word` (với POST request)
   - `/api/image-compress` (với POST request)

### Frontend:
1. Truy cập trang chủ Netlify của bạn
2. Test các tính năng:
   - PDF Tools (merge, split, convert)
   - Image Tools (compress, resize, convert) - MỚI!
   - QR Code generation

---

## 🔑 Backend API Endpoints

### PDF Operations:
- `POST /api/merge-pdfs` - Merge multiple PDFs
- `POST /api/split-pdf` - Split PDF pages
- `POST /api/resize-pdf` - Resize PDF dimensions
- `POST /api/pdf-to-word` - Convert PDF to DOCX
- `POST /api/pdf-to-excel` - Convert PDF to XLSX
- `POST /api/pdf-to-powerpoint` - Convert PDF to PPTX
- `POST /api/pdf-to-image` - Convert PDF to images (ZIP)

### Image Operations (MỚI):
- `POST /api/image-compress` - Compress images
- `POST /api/image-resize` - Resize images
- `POST /api/image-convert` - Convert image formats

### QR Code:
- `POST /api/qrwifi` - Generate WiFi QR code

---

## 🔒 Security Features Implemented:
- ✅ Rate limiting on all endpoints
- ✅ File size validation (max 50MB)
- ✅ File type validation
- ✅ Input sanitization
- ✅ Page count limits
- ✅ Error handling

---

## 📝 Notes:

1. **Backend deployment time**: ~10-15 phút (do cài đặt LibreOffice và dependencies)
2. **Frontend URL**: Sẽ là subdomain của netlify.app hoặc custom domain nếu đã cấu hình
3. **Backend URL**: https://zaptools-backend.as.r.appspot.com (cố định)

---

## 🐛 Troubleshooting:

### Backend không start:
```bash
# Xem logs chi tiết
gcloud app logs tail -s default --level=debug
```

### Frontend không kết nối được backend:
- Kiểm tra CORS đã enable trong backend
- Kiểm tra URL backend trong các file HTML
- Mở DevTools console để xem lỗi

---

Generated: 2025-12-03
