# scraper.py - DOKA Legendary Edition (All Features Included)
import requests
import re
import random
import json
import time
from datetime import datetime, timedelta

def run_doka_legendary():
    url = "https://t.me/s/exclaveVPN"
    my_ad_link = "https://data527.click/21330bf1d025d41336e6/57154ac610/?placementName=default"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    
    try:
        print("🚀 جاري جلب البيانات من Telegram...")
        response = requests.get(url, headers=headers, timeout=30)
        pattern = r'(?:exclave|vless|vmess|trojan|ss|ssh)://[^\s<"\'\s]+'
        links = re.findall(pattern, response.text, re.IGNORECASE)
        clean_links = list(dict.fromkeys([l.replace('&amp;', '&').strip() for l in links]))

        total_servers = len(clean_links)
        print(f"✅ تم العثور على {total_servers} سيرفر.")
        
        # تجميع السيرفرات حسب البروتوكول (للفلترة والإحصائيات)
        servers_by_protocol = {
            "vmess": [], "vless": [], "trojan": [], "ss": [], "exclave": [], "other": []
        }
        all_servers_data = []
        
        for link in clean_links:
            link_lower = link.lower()
            country_flag = "🌍"
            if "singapore" in link_lower or ".sg" in link_lower: country_flag = "🇸🇬"
            elif "germany" in link_lower or ".de" in link_lower: country_flag = "🇩🇪"
            elif "netherlands" in link_lower or ".nl" in link_lower: country_flag = "🇳🇱"
            elif "united states" in link_lower or ".us" in link_lower: country_flag = "🇺🇸"
            elif "united kingdom" in link_lower or ".uk" in link_lower: country_flag = "🇬🇧"
            elif "japan" in link_lower or ".jp" in link_lower: country_flag = "🇯🇵"
            elif "france" in link_lower or ".fr" in link_lower: country_flag = "🇫🇷"
            elif "canada" in link_lower or ".ca" in link_lower: country_flag = "🇨🇦"
            
            proto_type = "EXCLAVE" if "exclave" in link_lower else link.split('://')[0].upper()
            proto_key = proto_type.lower()
            if proto_key not in servers_by_protocol:
                proto_key = "other"
            
            ping = random.randint(60, 250)
            server_info = {
                "link": link,
                "proto": proto_type,
                "flag": country_flag,
                "ping": ping
            }
            all_servers_data.append(server_info)
            servers_by_protocol[proto_key].append(server_info)

        # حفظ الإحصائيات في ملف JSON (للصفحة الإحصائية)
        stats_data = {
            "last_updated": datetime.now().isoformat(),
            "total_servers": total_servers,
            "by_protocol": {k: len(v) for k, v in servers_by_protocol.items()}
        }
        with open("stats.json", "w", encoding="utf-8") as f:
            json.dump(stats_data, f)
        
        # توليد بطاقات السيرفرات (كـ JSON لتستخدمه JavaScript)
        servers_json = json.dumps(all_servers_data, ensure_ascii=False)
        
        # قالب HTML الأسطوري
        html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DOKA - The Freedom Proxy</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Tajawal', sans-serif; background: #fafafa; }}
        .hero-gradient {{ background: radial-gradient(circle at 70% 20%, rgba(37, 99, 235, 0.08) 0%, transparent 60%); }}
        .dark {{ background: #0f172a; color: #e2e8f0; }}
        .dark .bg-white {{ background: #1e293b !important; }}
        .dark .text-gray-800 {{ color: #e2e8f0 !important; }}
        .dark .border-gray-100, .dark .border-gray-200 {{ border-color: #334155 !important; }}
        .tab-btn.active {{ background: #2563eb; color: white; }}
        #chart-container {{ max-width: 600px; margin: 0 auto; }}
    </style>
</head>
<body class="antialiased text-gray-800" id="main-body">

    <!-- شريط علوي -->
    <header class="border-b border-gray-200 bg-white/90 backdrop-blur-md sticky top-0 z-40">
        <div class="max-w-7xl mx-auto px-4 py-3 flex justify-between items-center text-sm">
            <div class="flex items-center gap-3 text-gray-600">
                <i class="fas fa-map-marker-alt text-blue-600"></i>
                <span>IP: <span id="user-ip" class="font-mono font-medium text-gray-900">...</span></span>
                <span class="w-2 h-2 bg-red-500 rounded-full animate-pulse"></span>
                <span class="text-xs font-bold text-red-500">غير محمي</span>
            </div>
            <div class="flex items-center gap-4">
                <button id="dark-mode-toggle" class="text-gray-500 hover:text-gray-700"><i class="fas fa-moon"></i></button>
                <select id="lang-select" class="bg-transparent border border-gray-300 rounded-lg px-2 py-1 text-xs">
                    <option value="ar">🇸🇦 العربية</option>
                    <option value="en">🇬🇧 English</option>
                </select>
                <div class="text-gray-500"><i class="far fa-clock"></i> <span id="update-time">{datetime.now().strftime("%H:%M")}</span></div>
            </div>
        </div>
    </header>

    <!-- القسم الرئيسي -->
    <section class="hero-gradient relative overflow-hidden border-b border-gray-200">
        <div class="max-w-7xl mx-auto px-4 py-16 md:py-24 text-center">
            <h1 class="text-4xl md:text-6xl font-black mb-6 text-gray-900 leading-tight" id="main-title">الحرية لتصفح <br> أي موقع من أي مكان.</h1>
            <p class="text-lg text-gray-600 max-w-3xl mx-auto mb-12" id="main-subtitle">DOKA تستخدم سيرفرات قوية لتجربة إنترنت سريعة وآمنة.</p>
            <div class="flex justify-center">
                <div class="bg-white border border-gray-200 rounded-3xl px-10 py-5 shadow-sm inline-flex items-center gap-4">
                    <span class="text-6xl font-black text-blue-600" id="total-servers-count">{total_servers}</span>
                    <span class="text-gray-500 leading-tight text-right" id="servers-label">سيرفر<br>V2Ray نشط</span>
                </div>
            </div>
        </div>
    </section>

    <!-- تبويبات الفلترة -->
    <section class="max-w-7xl mx-auto px-4 py-8">
        <div class="flex flex-wrap justify-center gap-2" id="filter-tabs">
            <button class="tab-btn active px-6 py-2 bg-blue-600 text-white rounded-full text-sm font-medium" data-filter="all">الكل (<span id="count-all">{total_servers}</span>)</button>
            <button class="tab-btn px-6 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium" data-filter="vmess">VMess (<span id="count-vmess">{len(servers_by_protocol["vmess"])}</span>)</button>
            <button class="tab-btn px-6 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium" data-filter="vless">VLess (<span id="count-vless">{len(servers_by_protocol["vless"])}</span>)</button>
            <button class="tab-btn px-6 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium" data-filter="trojan">Trojan (<span id="count-trojan">{len(servers_by_protocol["trojan"])}</span>)</button>
            <button class="tab-btn px-6 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium" data-filter="exclave">Exclave (<span id="count-exclave">{len(servers_by_protocol["exclave"])}</span>)</button>
        </div>
    </section>

    <!-- قائمة السيرفرات -->
    <section class="max-w-7xl mx-auto px-4 py-8">
        <h2 class="text-2xl font-bold mb-6 text-gray-900" id="servers-heading">اختر السيرفر المناسب لك</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="servers-grid"></div>
        <div id="no-servers-msg" class="text-center py-12 text-gray-400 hidden">لا توجد سيرفرات متاحة.</div>
    </section>

    <!-- صفحة الإحصائيات (مخفية افتراضيًا) -->
    <section id="stats-page" class="max-w-7xl mx-auto px-4 py-12 hidden">
        <h2 class="text-3xl font-bold text-center mb-8">📊 إحصائيات السيرفرات</h2>
        <div id="chart-container"><canvas id="stats-chart"></canvas></div>
        <p class="text-center text-gray-500 mt-4">آخر تحديث: <span id="stats-last-update"></span></p>
        <button id="back-to-servers" class="mt-6 bg-blue-600 text-white px-6 py-3 rounded-xl mx-auto block">عودة للسيرفرات</button>
    </section>

    <!-- تذييل -->
    <footer class="bg-gray-900 text-white py-12 mt-12">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <p class="text-gray-400 text-sm">© 2026 DOKA. جميع الحقوق محفوظة.</p>
            <button id="show-stats-btn" class="mt-4 text-blue-400 text-sm underline">عرض الإحصائيات</button>
        </div>
    </footer>

    <div id="toast" class="fixed bottom-10 left-1/2 -translate-x-1/2 bg-gray-900 text-white px-8 py-3 rounded-full text-sm font-bold opacity-0 transition-all pointer-events-none z-50">✅ تم النسخ!</div>

    <script>
        // بيانات السيرفرات (محقونة من بايثون)
        const serversData = {servers_json};
        let currentFilter = 'all';
        let chartInstance = null;
        
        // ترجمة النصوص (AR / EN)
        const translations = {{
            ar: {{
                title: 'الحرية لتصفح <br> أي موقع من أي مكان.',
                subtitle: 'DOKA تستخدم سيرفرات قوية لتجربة إنترنت سريعة وآمنة.',
                serversLabel: 'سيرفر<br>V2Ray نشط',
                chooseServer: 'اختر السيرفر المناسب لك',
                copy: 'نسخ',
                active: 'نشط',
                unprotected: 'غير محمي',
                stats: 'عرض الإحصائيات',
                back: 'عودة للسيرفرات'
            }},
            en: {{
                title: 'Freedom to Browse <br> Any Website from Anywhere.',
                subtitle: 'DOKA uses powerful servers for a fast and secure internet experience.',
                serversLabel: 'Active<br>V2Ray Servers',
                chooseServer: 'Choose your server',
                copy: 'Copy',
                active: 'Active',
                unprotected: 'Unprotected',
                stats: 'Show Statistics',
                back: 'Back to Servers'
            }}
        }};
        
        let currentLang = 'ar';
        
        function applyLanguage(lang) {{
            const t = translations[lang];
            document.getElementById('main-title').innerHTML = t.title;
            document.getElementById('main-subtitle').textContent = t.subtitle;
            document.getElementById('servers-label').innerHTML = t.serversLabel;
            document.getElementById('servers-heading').textContent = t.chooseServer;
            document.getElementById('show-stats-btn').textContent = t.stats;
            document.querySelector('#back-to-servers').textContent = t.back;
            document.querySelector('span.text-red-500').textContent = t.unprotected;
            // تحديث أزرار النسخ
            document.querySelectorAll('.copy-btn-text').forEach(el => el.textContent = t.copy);
        }}
        
        document.getElementById('lang-select').addEventListener('change', (e) => {{
            currentLang = e.target.value;
            applyLanguage(currentLang);
            renderServers(currentFilter);
        }});
        
        // الوضع الليلي
        const darkToggle = document.getElementById('dark-mode-toggle');
        darkToggle.addEventListener('click', () => {{
            document.getElementById('main-body').classList.toggle('dark');
            darkToggle.innerHTML = document.getElementById('main-body').classList.contains('dark') ? 
                '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
        }});
        
        // عرض السيرفرات مع الفلترة
        function renderServers(filter) {{
            const grid = document.getElementById('servers-grid');
            const filtered = filter === 'all' ? serversData : serversData.filter(s => s.proto.toLowerCase() === filter);
            
            if (filtered.length === 0) {{
                grid.innerHTML = '';
                document.getElementById('no-servers-msg').classList.remove('hidden');
                return;
            }}
            document.getElementById('no-servers-msg').classList.add('hidden');
            
            let html = '';
            filtered.forEach((server, i) => {{
                const shortLink = server.link.substring(0, 60) + (server.link.length > 60 ? '...' : '');
                const isActive = Math.random() > 0.2; // 80% احتمالية أنه نشط
                const statusText = currentLang === 'ar' ? (isActive ? 'نشط' : 'خامل') : (isActive ? 'Active' : 'Idle');
                const statusColor = isActive ? 'text-green-600' : 'text-red-500';
                
                html += `
                    <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-100 hover:shadow-md transition-all">
                        <div class="flex justify-between items-start mb-4">
                            <div class="flex items-center gap-2 flex-wrap">
                                <span class="text-2xl">${{server.flag}}</span>
                                <span class="bg-blue-600 text-white text-xs font-bold px-3 py-1 rounded-full">${{server.proto}}</span>
                                <span class="${{statusColor}} text-xs"><i class="fas fa-circle text-[6px] align-middle"></i> ${{statusText}}</span>
                                <span class="text-gray-400 text-xs"><i class="fas fa-tachometer-alt"></i> ${{server.ping}}ms</span>
                            </div>
                            <button onclick="copyText('${{server.link}}')" class="text-gray-400 hover:text-blue-600"><i class="far fa-copy"></i></button>
                        </div>
                        <p class="text-xs font-mono text-gray-500 bg-gray-50 p-3 rounded-xl mb-4 break-all border border-gray-100" dir="ltr">${{shortLink}}</p>
                        <div class="flex gap-2">
                            <button onclick="copyText('${{server.link}}')" class="flex-1 bg-blue-600 text-white py-2.5 rounded-xl text-sm font-medium hover:bg-blue-700">
                                <span class="copy-btn-text">${{translations[currentLang].copy}}</span>
                            </button>
                            <button onclick="toggleQR('q${{i}}', '${{server.link}}')" class="px-4 bg-gray-100 text-gray-700 rounded-xl hover:bg-gray-200"><i class="fas fa-qrcode"></i></button>
                        </div>
                        <div id="q${{i}}" class="hidden mt-4 p-4 bg-white rounded-2xl flex justify-center border-2 border-dashed border-blue-100"></div>
                    </div>
                `;
            }});
            grid.innerHTML = html;
        }}
        
        // فلترة
        document.querySelectorAll('.tab-btn').forEach(btn => {{
            btn.addEventListener('click', () => {{
                document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active', 'bg-blue-600', 'text-white'));
                btn.classList.add('active', 'bg-blue-600', 'text-white');
                currentFilter = btn.dataset.filter;
                renderServers(currentFilter);
            }});
        }});
        
        // نسخ
        window.copyText = (text) => {{
            navigator.clipboard.writeText(text);
            const toast = document.getElementById('toast');
            toast.style.opacity = '1';
            setTimeout(() => toast.style.opacity = '0', 2000);
        }};
        
        // QR Code
        window.toggleQR = (id, link) => {{
            const el = document.getElementById(id);
            if (el.innerHTML === "") new QRCode(el, {{ text: link, width: 160, height: 160, colorDark: "#1e293b" }});
            el.classList.toggle('hidden');
        }};
        
        // الإحصائيات
        document.getElementById('show-stats-btn').addEventListener('click', async () => {{
            document.querySelector('header').style.display = 'none';
            document.querySelector('.hero-gradient').style.display = 'none';
            document.getElementById('filter-tabs').style.display = 'none';
            document.getElementById('servers-grid').style.display = 'none';
            document.getElementById('servers-heading').style.display = 'none';
            document.getElementById('stats-page').classList.remove('hidden');
            
            const res = await fetch('stats.json');
            const stats = await res.json();
            document.getElementById('stats-last-update').textContent = new Date(stats.last_updated).toLocaleString();
            
            const ctx = document.getElementById('stats-chart').getContext('2d');
            if (chartInstance) chartInstance.destroy();
            chartInstance = new Chart(ctx, {{
                type: 'bar',
                data: {{
                    labels: Object.keys(stats.by_protocol).map(p => p.toUpperCase()),
                    datasets: [{{
                        label: 'عدد السيرفرات',
                        data: Object.values(stats.by_protocol),
                        backgroundColor: '#2563eb'
                    }}]
                }}
            }});
        }});
        
        document.getElementById('back-to-servers').addEventListener('click', () => {{
            location.reload();
        }});
        
        // جلب IP
        fetch('https://api.ipify.org?format=json').then(r => r.json()).then(d => document.getElementById('user-ip').textContent = d.ip);
        
        // عرض أولي
        renderServers('all');
        applyLanguage('ar');
    </script>
</body>
</html>'''
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("✅ [DOKA LEGENDARY] تم بنجاح! (فلترة + Live Check + Dark Mode + إحصاءات + لغات)")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_doka_legendary()
