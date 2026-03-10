import requests
import re
from datetime import datetime

# اسم المشروع المطور: velss
def run_velss():
    url = "https://t.me/s/exclaveVPN"
    # تم استخدام رابطك الإعلاني المحفوظ
    my_ad_link = "https://data527.click/21330bf1d025d41336e6/57154ac610/?placementName=default"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        # استخدام Session لتحسين سرعة الطلبات
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=20)
        
        # استخراج الروابط بنمط مطور
        links = re.findall(r'(?:vless|vmess|trojan|ss|tuic|hysteria2)://[^\s<"\'\s]+', response.text)
        
        # تنظيف الروابط ومنع التكرار
        clean_links = []
        for l in links:
            c = l.replace('&amp;', '&').split('<')[0].split('"')[0].strip()
            if c not in clean_links: clean_links.append(c)
        
        now = datetime.now().strftime("%Y-%m-%d")
        
        # وحدة إعلانية بتصميم متناسق مع الواجهة الجديدة
        ad_unit_html = f'''
        <div class="flex justify-center my-10">
            <div class="relative group cursor-pointer" onclick="triggerBridge()">
                <ins style="display:inline-block;width:300px;height:250px" class="g2fb0b4c321" data-domain="//data527.click" data-affquery="/e3435b2a507722939b6f/2fb0b4c321/?placementName=default">
                    <script src="//data527.click/js/responsive.js" async></script>
                </ins>
                <div class="absolute inset-0 bg-transparent group-hover:bg-indigo-600/5 transition-colors rounded-xl"></div>
            </div>
        </div>'''

        server_cards = ""
        for i, link in enumerate(clean_links):
            proto = link.split('://')[0].upper()
            server_cards += f'''
            <div class="server-card bg-white border border-slate-100 p-6 rounded-3xl shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 mb-6 text-right" data-type="{proto}">
                <div class="flex justify-between items-center mb-4">
                    <div class="flex items-center gap-3">
                        <span class="flex h-2 w-2 rounded-full bg-green-500 shadow-[0_0_8px_rgba(34,197,94,0.6)]"></span>
                        <span class="bg-indigo-50 text-indigo-700 px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-wider border border-indigo-100">{proto} PREMIUM</span>
                    </div>
                    <button onclick="copyText('{link}')" class="text-slate-300 hover:text-indigo-600 transition-colors"><i class="far fa-copy text-lg"></i></button>
                </div>
                <div class="bg-slate-50 rounded-2xl p-3 mb-5 group relative overflow-hidden">
                    <p class="text-[9px] font-mono text-slate-500 break-all leading-relaxed line-clamp-2">{link}</p>
                </div>
                <div class="grid grid-cols-2 gap-3">
                    <button onclick="copyText('{link}')" class="py-3.5 bg-indigo-600 text-white rounded-2xl font-bold text-xs hover:bg-indigo-700 active:scale-95 transition-all shadow-lg shadow-indigo-100">نسخ الإعدادات</button>
                    <button onclick="downloadConfig('{proto}_{i}', '{link}')" class="py-3.5 bg-slate-900 text-white rounded-2xl font-bold text-xs hover:bg-black active:scale-95 transition-all shadow-lg">تحميل الملف</button>
                    <button onclick="toggleQR('q{i}', '{link}')" class="col-span-2 py-3 bg-white border-2 border-slate-100 text-slate-600 rounded-2xl text-[10px] font-bold hover:bg-gray-50 transition-all uppercase tracking-tighter">إظهار رمز الـ QR 🔳</button>
                </div>
                <div id="q{i}" class="hidden mt-5 p-5 border-2 border-dashed border-indigo-50 bg-indigo-50/20 rounded-3xl flex flex-col items-center animate-fade-in"></div>
            </div>'''
            if (i + 1) % 5 == 0: server_cards += ad_unit_html

        html_output = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>velss - Ultimate Network Nodes</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Cairo', sans-serif; background-color: #f8fafc; scroll-behavior: smooth; }}
        .gradient-brand {{ background: linear-gradient(135deg, #1e1b4b 0%, #4338ca 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .filter-btn.active {{ background-color: #4338ca; color: white; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(67, 56, 202, 0.2); }}
        #bridge-page {{ display: none; background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); z-index: 9999; }}
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        .animate-fade-in {{ animation: fadeIn 0.4s ease-out; }}
    </style>
</head>
<body class="pb-20">

    <div id="bridge-page" class="fixed inset-0 flex flex-col items-center justify-center text-center p-6">
        <div class="w-16 h-16 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin mb-6"></div>
        <h2 class="text-2xl font-black mb-2 text-slate-800 tracking-tight">جاري التحقق من الأمان...</h2>
        <p class="text-slate-500 text-sm">يرجى الانتظار للحصول على أفضل استقرار للسيرفر</p>
    </div>

    <nav class="sticky top-0 z-40 bg-white/80 backdrop-blur-md border-b border-slate-100 px-6 py-4">
        <div class="max-w-6xl mx-auto flex justify-between items-center">
            <div class="flex items-center gap-2 cursor-pointer" onclick="triggerBridge()">
                <div class="w-10 h-10 bg-indigo-600 rounded-xl flex items-center justify-center shadow-lg shadow-indigo-200">
                    <i class="fas fa-shield-bolt text-white"></i>
                </div>
                <span class="text-2xl font-black text-slate-900 uppercase tracking-tighter">velss</span>
            </div>
            <div class="bg-slate-900 px-4 py-2 rounded-2xl">
                <span id="countdown" class="text-indigo-400 font-black text-xs tabular-nums tracking-widest">00:00:00</span>
            </div>
        </div>
    </nav>

    <header class="max-w-4xl mx-auto px-6 py-16 text-center">
        <h1 class="text-5xl md:text-7xl font-black mb-6 gradient-brand tracking-tighter">سيرفرات velss الذكية</h1>
        <p class="text-slate-500 text-sm md:text-base max-w-xl mx-auto leading-relaxed">أقوى خوادم V2Ray العالمية، يتم تحديثها آلياً لضمان تخطي القيود وتوفير أقصى سرعة ممكنة.</p>
    </header>

    <div class="flex overflow-x-auto gap-3 px-6 mb-12 max-w-2xl mx-auto no-scrollbar justify-start md:justify-center">
        <button onclick="filterServers('ALL', this)" class="filter-btn active whitespace-nowrap px-8 py-3 rounded-2xl border border-slate-200 bg-white text-xs font-bold transition-all">الكل</button>
        <button onclick="filterServers('VMESS', this)" class="filter-btn whitespace-nowrap px-8 py-3 rounded-2xl border border-slate-200 bg-white text-xs font-bold transition-all">VMESS</button>
        <button onclick="filterServers('VLESS', this)" class="filter-btn whitespace-nowrap px-8 py-3 rounded-2xl border border-slate-200 bg-white text-xs font-bold transition-all">VLESS</button>
        <button onclick="filterServers('TROJAN', this)" class="filter-btn whitespace-nowrap px-8 py-3 rounded-2xl border border-slate-200 bg-white text-xs font-bold transition-all">TROJAN</button>
    </div>

    <main class="max-w-xl mx-auto px-6">
        <div class="flex items-center justify-between mb-8">
            <h2 class="font-black text-xl text-slate-800">قائمة السيرفرات اليومية</h2>
            <span class="bg-indigo-50 text-indigo-600 px-4 py-1.5 rounded-xl text-[10px] font-black border border-indigo-100 uppercase tracking-widest">{now}</span>
        </div>
        
        <div id="servers-container">{server_cards}</div>
    </main>

    <footer class="mt-20 py-12 px-6 border-t border-slate-100 bg-white">
        <div class="max-w-xl mx-auto text-right space-y-10">
            <div class="p-6 bg-slate-50 rounded-3xl">
                <h3 class="font-black text-slate-900 mb-3 flex items-center gap-2"><i class="fas fa-file-shield text-indigo-600"></i> سياسة الخصوصية</h3>
                <p class="text-[11px] text-slate-500 leading-loose">نحن في <b>velss</b> نهتم بخصوصيتك. جميع البيانات المشفرة لا يتم تخزينها على خوادمنا، ونحن نضمن لك تصفحاً آمناً بعيداً عن الرقابة.</p>
            </div>
            <div class="text-center">
                <p class="text-[10px] text-slate-400 font-bold uppercase tracking-[0.3em] mb-4">© 2026 velss. All Rights Reserved</p>
                <div class="flex justify-center gap-6 text-indigo-600 font-black text-[10px] uppercase">
                    <span class="cursor-pointer hover:text-slate-900 transition-colors" onclick="triggerBridge()">Privacy</span>
                    <span class="cursor-pointer hover:text-slate-900 transition-colors" onclick="triggerBridge()">Contact</span>
                </div>
            </div>
        </div>
    </footer>

    <div id="toast" class="fixed bottom-10 left-1/2 -translate-x-1/2 bg-slate-900 text-white px-8 py-4 rounded-3xl text-xs font-bold opacity-0 transition-all pointer-events-none z-50 shadow-2xl">تم النسخ بنجاح! ⚡</div>

    <script>
        function filterServers(type, btn) {{
            const cards = document.querySelectorAll('.server-card');
            const buttons = document.querySelectorAll('.filter-btn');
            buttons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            cards.forEach(c => {{
                if(type === 'ALL' || c.getAttribute('data-type') === type) {{
                    c.style.display = 'block';
                    c.classList.add('animate-fade-in');
                }} else {{
                    c.style.display = 'none';
                }}
            }});
        }}

        function downloadConfig(filename, text) {{
            const element = document.createElement('a');
            element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
            element.setAttribute('download', "velss_" + filename + ".txt");
            element.click();
        }}

        function triggerBridge() {{
            const bridge = document.getElementById('bridge-page');
            bridge.style.display = 'flex';
            setTimeout(() => {{ window.open('{my_ad_link}', '_blank'); bridge.style.display = 'none'; }}, 1000);
        }}

        function startCountdown() {{
            let h = 5, m = 59, s = 59;
            setInterval(() => {{
                if(s > 0) s--; else {{ s = 59; if(m > 0) m--; else {{ m = 59; h--; }} }}
                document.getElementById('countdown').innerText = String(h).padStart(2,'0')+":"+String(m).padStart(2,'0')+":"+String(s).padStart(2,'0');
            }}, 1000);
        }}
        startCountdown();

        function copyText(t) {{
            navigator.clipboard.writeText(t);
            const toast = document.getElementById('toast');
            toast.style.opacity = '1';
            toast.style.transform = 'translate(-50%, -10px)';
            setTimeout(() => {{ 
                toast.style.opacity = '0'; 
                toast.style.transform = 'translate(-50%, 0)';
            }}, 2000);
        }}

        function toggleQR(id, link) {{
            const el = document.getElementById(id);
            if (el.children.length === 0) {{
                new QRCode(el, {{ text: link, width: 180, height: 180, colorDark: "#1e1b4b" }});
            }}
            el.classList.toggle('hidden');
        }}
    </script>
</body>
</html>'''
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html_output)
        print("✅ [velss] v2.0: تم تحديث الموقع بنجاح وإعادة بناء الواجهة!")
            
    except Exception as e:
        print(f"❌ Error in velss core: {e}")

if __name__ == "__main__":
    run_velss()
