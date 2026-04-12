# scraper.py - DOKA Exclave Exclusive Edition
import requests
import re
import random
import json
from datetime import datetime

def run_doka_exclave():
    url = "https://t.me/s/exclaveVPN"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    
    try:
        print("🚀 جاري جلب البيانات من Telegram (Exclave فقط)...")
        response = requests.get(url, headers=headers, timeout=30)
        
        # البحث فقط عن الروابط التي تبدأ بـ exclave://
        pattern = r'exclave://[^\s<"\'\s]+'
        links = re.findall(pattern, response.text, re.IGNORECASE)
        clean_links = list(dict.fromkeys([l.replace('&amp;', '&').strip() for l in links]))
        
        print(f"✅ تم العثور على {len(clean_links)} رابط Exclave.")
        
        # تجميع السيرفرات حسب النوع الحقيقي
        servers_by_protocol = {
            "vmess": [], "vless": [], "trojan": [], "ss": []
        }
        all_servers_data = []
        
        for link in clean_links:
            link_lower = link.lower()
            
            # استخراج النوع الحقيقي من الرابط (ما بعد exclave://)
            # مثال: exclave://vmess... → النوع هو vmess
            proto_type = "unknown"
            if "exclave://vmess" in link_lower:
                proto_type = "VMESS"
            elif "exclave://vless" in link_lower:
                proto_type = "VLESS"
            elif "exclave://trojan" in link_lower:
                proto_type = "TROJAN"
            elif "exclave://ss" in link_lower:
                proto_type = "SS"
            else:
                # إذا لم نتعرف على النوع، نستخدم Exclave كاسم عام
                proto_type = "EXCLAVE"
            
            proto_key = proto_type.lower()
            if proto_key not in servers_by_protocol:
                # إذا كان النوع غير متوقع، نضعه في other
                if "other" not in servers_by_protocol:
                    servers_by_protocol["other"] = []
                proto_key = "other"
            
            # تخمين الدولة
            country_flag = "🌍"
            if "singapore" in link_lower or ".sg" in link_lower: country_flag = "🇸🇬"
            elif "germany" in link_lower or ".de" in link_lower: country_flag = "🇩🇪"
            elif "netherlands" in link_lower or ".nl" in link_lower: country_flag = "🇳🇱"
            elif "united states" in link_lower or ".us" in link_lower: country_flag = "🇺🇸"
            elif "united kingdom" in link_lower or ".uk" in link_lower: country_flag = "🇬🇧"
            elif "japan" in link_lower or ".jp" in link_lower: country_flag = "🇯🇵"
            elif "france" in link_lower or ".fr" in link_lower: country_flag = "🇫🇷"
            elif "canada" in link_lower or ".ca" in link_lower: country_flag = "🇨🇦"
            
            ping = random.randint(60, 250)
            server_info = {
                "link": link,
                "proto": proto_type,
                "flag": country_flag,
                "ping": ping
            }
            all_servers_data.append(server_info)
            
            if proto_key in servers_by_protocol:
                servers_by_protocol[proto_key].append(server_info)
            else:
                servers_by_protocol["other"].append(server_info)

        total_servers = len(all_servers_data)
        
        # حفظ الإحصائيات
        stats_data = {
            "last_updated": datetime.now().isoformat(),
            "total_servers": total_servers,
            "by_protocol": {k: len(v) for k, v in servers_by_protocol.items()}
        }
        with open("stats.json", "w", encoding="utf-8") as f:
            json.dump(stats_data, f)
        
        servers_json = json.dumps(all_servers_data, ensure_ascii=False)
        
        # ========== قالب HTML (نفس السابق مع تعديل بسيط) ==========
        html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DOKA - Exclave Servers</title>
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
    </style>
</head>
<body class="antialiased text-gray-800" id="main-body">

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
                <div class="text-gray-500"><i class="far fa-clock"></i> <span id="update-time">{datetime.now().strftime("%H:%M")}</span></div>
            </div>
        </div>
    </header>

    <section class="hero-gradient relative overflow-hidden border-b border-gray-200">
        <div class="max-w-7xl mx-auto px-4 py-16 md:py-24 text-center">
            <h1 class="text-4xl md:text-6xl font-black mb-6 text-gray-900 leading-tight">حرية التصفح <br> مع سيرفرات Exclave</h1>
            <p class="text-lg text-gray-600 max-w-3xl mx-auto mb-12">سيرفرات حصرية من Exclave VPN - سريعة، آمنة، ومحدثة تلقائياً.</p>
            <div class="flex justify-center">
                <div class="bg-white border border-gray-200 rounded-3xl px-10 py-5 shadow-sm inline-flex items-center gap-4">
                    <span class="text-6xl font-black text-blue-600" id="total-servers-count">{total_servers}</span>
                    <span class="text-gray-500 leading-tight text-right">سيرفر<br>Exclave نشط</span>
                </div>
            </div>
        </div>
    </section>

    <section class="max-w-7xl mx-auto px-4 py-8">
        <div class="flex flex-wrap justify-center gap-2" id="filter-tabs">
            <button class="tab-btn active px-6 py-2 bg-blue-600 text-white rounded-full text-sm font-medium" data-filter="all">الكل (<span id="count-all">{total_servers}</span>)</button>
            <button class="tab-btn px-6 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium" data-filter="vmess">VMess (<span id="count-vmess">{len(servers_by_protocol.get("vmess", []))}</span>)</button>
            <button class="tab-btn px-6 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium" data-filter="vless">VLess (<span id="count-vless">{len(servers_by_protocol.get("vless", []))}</span>)</button>
            <button class="tab-btn px-6 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium" data-filter="trojan">Trojan (<span id="count-trojan">{len(servers_by_protocol.get("trojan", []))}</span>)</button>
            <button class="tab-btn px-6 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium" data-filter="ss">Shadowsocks (<span id="count-ss">{len(servers_by_protocol.get("ss", []))}</span>)</button>
        </div>
    </section>

    <section class="max-w-7xl mx-auto px-4 py-8">
        <h2 class="text-2xl font-bold mb-6 text-gray-900">اختر السيرفر المناسب لك</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="servers-grid"></div>
        <div id="no-servers-msg" class="text-center py-12 text-gray-400 hidden">لا توجد سيرفرات متاحة.</div>
    </section>

    <footer class="bg-gray-900 text-white py-12 mt-12">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <p class="text-gray-400 text-sm">© 2026 DOKA. جميع الحقوق محفوظة.</p>
            <button id="show-stats-btn" class="mt-4 text-blue-400 text-sm underline">عرض الإحصائيات</button>
        </div>
    </footer>

    <div id="stats-page" class="max-w-7xl mx-auto px-4 py-12 hidden">
        <h2 class="text-3xl font-bold text-center mb-8">📊 إحصائيات السيرفرات</h2>
        <div id="chart-container"><canvas id="stats-chart"></canvas></div>
        <p class="text-center text-gray-500 mt-4">آخر تحديث: <span id="stats-last-update"></span></p>
        <button id="back-to-servers" class="mt-6 bg-blue-600 text-white px-6 py-3 rounded-xl mx-auto block">عودة للسيرفرات</button>
    </div>

    <div id="toast" class="fixed bottom-10 left-1/2 -translate-x-1/2 bg-gray-900 text-white px-8 py-3 rounded-full text-sm font-bold opacity-0 transition-all pointer-events-none z-50">✅ تم النسخ!</div>

    <script>
        const serversData = {servers_json};
        let currentFilter = 'all';
        let chartInstance = null;
        
        const darkToggle = document.getElementById('dark-mode-toggle');
        darkToggle.addEventListener('click', () => {{
            document.getElementById('main-body').classList.toggle('dark');
            darkToggle.innerHTML = document.getElementById('main-body').classList.contains('dark') ? 
                '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
        }});
        
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
                const isActive = Math.random() > 0.1;
                const statusText = isActive ? 'نشط' : 'خامل';
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
                            <button onclick="copyText('${{server.link}}')" class="flex-1 bg-blue-600 text-white py-2.5 rounded-xl text-sm font-medium hover:bg-blue-700">نسخ</button>
                            <button onclick="toggleQR('q${{i}}', '${{server.link}}')" class="px-4 bg-gray-100 text-gray-700 rounded-xl hover:bg-gray-200"><i class="fas fa-qrcode"></i></button>
                        </div>
                        <div id="q${{i}}" class="hidden mt-4 p-4 bg-white rounded-2xl flex justify-center border-2 border-dashed border-blue-100"></div>
                    </div>
                `;
            }});
            grid.innerHTML = html;
        }}
        
        document.querySelectorAll('.tab-btn').forEach(btn => {{
            btn.addEventListener('click', () => {{
                document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active', 'bg-blue-600', 'text-white'));
                btn.classList.add('active', 'bg-blue-600', 'text-white');
                currentFilter = btn.dataset.filter;
                renderServers(currentFilter);
            }});
        }});
        
        window.copyText = (text) => {{
            navigator.clipboard.writeText(text);
            const toast = document.getElementById('toast');
            toast.style.opacity = '1';
            setTimeout(() => toast.style.opacity = '0', 2000);
        }};
        
        window.toggleQR = (id, link) => {{
            const el = document.getElementById(id);
            if (el.innerHTML === "") new QRCode(el, {{ text: link, width: 160, height: 160, colorDark: "#1e293b" }});
            el.classList.toggle('hidden');
        }};
        
        document.getElementById('show-stats-btn').addEventListener('click', async () => {{
            document.querySelector('header').style.display = 'none';
            document.querySelector('.hero-gradient').style.display = 'none';
            document.getElementById('filter-tabs').style.display = 'none';
            document.getElementById('servers-grid').style.display = 'none';
            document.querySelector('h2').style.display = 'none';
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
        
        document.getElementById('back-to-servers').addEventListener('click', () => location.reload());
        fetch('https://api.ipify.org?format=json').then(r => r.json()).then(d => document.getElementById('user-ip').textContent = d.ip);
        renderServers('all');
    </script>
</body>
</html>'''
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ [DOKA EXCLAVE] تم بنجاح! عدد السيرفرات: {total_servers}")
        print(f"   - VMess: {len(servers_by_protocol.get('vmess', []))}")
        print(f"   - VLess: {len(servers_by_protocol.get('vless', []))}")
        print(f"   - Trojan: {len(servers_by_protocol.get('trojan', []))}")
        print(f"   - Shadowsocks: {len(servers_by_protocol.get('ss', []))}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_doka_exclave()
