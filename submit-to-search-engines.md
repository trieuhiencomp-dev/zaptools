# Submit ZapTools.org to Search Engines

## Google Search Console
1. Truy cập: https://search.google.com/search-console
2. Add property: `https://zaptools.org`
3. Verify ownership
4. Submit sitemap: `https://zaptools.org/sitemap.xml`
5. Request indexing cho homepage

## Bing Webmaster Tools
1. Truy cập: https://www.bing.com/webmasters
2. Add site: `https://zaptools.org`
3. Submit sitemap: `https://zaptools.org/sitemap.xml`

## IndexNow (Submit nhanh)
```bash
curl -X POST "https://www.bing.com/indexnow" \
  -H "Content-Type: application/json" \
  -d '{
    "host": "zaptools.org",
    "key": "your-key-here",
    "urlList": ["https://zaptools.org/"]
  }'
```

## Yandex Webmaster
1. Truy cập: https://webmaster.yandex.com
2. Add site: `https://zaptools.org`

## Submit Directory Listings (Free backlinks + faster indexing)
- https://www.producthunt.com
- https://alternativeto.net
- https://www.saashub.com
- https://tools.guru
- https://free-online-tools.com

## Social Signals (Help Google discover)
- Share trên Twitter/X
- Share trên Facebook
- Share trên Reddit (r/SideProject, r/webdev)
- Share trên LinkedIn

## Timeline mong đợi:
- 1-3 ngày: Google bot bắt đầu crawl
- 3-7 ngày: Trang đầu tiên được index
- 2-4 tuần: Đa số trang được index
- 1-2 tháng: Index đầy đủ và ranking tốt
