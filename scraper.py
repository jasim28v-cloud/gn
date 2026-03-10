import requests
import re
from datetime import datetime

def run_velss():
    # المصدر والرابط الإعلاني
    url = "https://t.me/s/exclaveVPN"
    my_ad_link = "https://data527.click/21330bf1d025d41336e6/57154ac610/?placementName=default"
    
    # الرؤوس (Headers) الاحترافية - Chrome 124 (أحدث إصدار لضمان جلب البيانات)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,video/*;q=0.9,*/*;q=0.8',
        'Accept-Language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.google.com/',
        'Sec-Fetch-Dest': 'image',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Sec-Ch-Ua': '"Google Chrome";v="124", "Not:A-Brand";v="8", "Chromium";v="124"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': 'https://www.google.com',
        'Range': 'bytes=0-'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=25)
        
        # النمط المطور لاستخراج كافة الروابط (exclave والروابط التقليدية)
        pattern = r'(?:exclave|vless|vmess|trojan|ss)://[^\s<"\'\s]+'
        links = re.findall(pattern, response.text, re.IGNORECASE)
        
        clean_links = []
        for l in links:
            c = l.replace('&amp;', '&').split('<')[0].split('"')[0].strip()
            if c not in clean_links: clean_links.append(c)
        
        now = datetime.now().strftime("%Y-%m-%d")
        
        ad_unit_html = f'''
        <div class="flex justify-center my-8">
            <ins style="width: 300px;height:250px" data-width="300" data-height="250" class="g2fb0b4c321" data-domain="//data527.click" data-affquery="/e3435b2a507722939b6f/2fb0b4c321/?placementName=default">
                <script src="//data527.click/js/responsive.js" async></script>
            </ins>
        </div>'''

        server_cards = ""
        for i, link in enumerate(clean_links):
            # تحديد النوع للعرض بشكل احترافي
            proto = "EXCLAVE" if "exclave://" in link.lower() else link.split('://')[0].upper()
            
            server_cards += f'''
            <div class="server-card bg-white border border-gray-200 p-5 rounded-2xl shadow-sm hover:shadow-md transition-all mb-4 text-right" data-type="{proto}">
                <div class="flex justify-between items-center mb-3">
                    <div class="flex items-center gap-2">
                        <span class="relative flex h-3 w-3"><span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span><span class="relative inline-flex rounded-full h-3 w-3 bg-green-500"></span></span>
                        <span class="bg-indigo-600 text-white px-3 py-1 rounded-lg text-[10px] font-bold uppercase">{proto} NODE</span>
                    </div>
                    <button onclick="copyText('{link}')" class="text-gray-400 hover:text-indigo-600"><i class="far fa-copy"></i></button>
                </div>
                <p class="text-[10px] text-gray-400 font-mono break-all mb-4 bg-gray-50 p-2 rounded leading-relaxed">{link[:85]}...</p>
                <div class="grid grid-cols-2 gap-2">
                    <button onclick="copyText('{link}')" class="py-3 bg-indigo-600 text-white rounded-xl font-bold text-xs hover:bg-indigo-700 transition-all shadow-lg shadow-indigo-100">نسخ الإعدادات</button>
                    <button onclick="downloadConfig('{proto}_{i}', '{link}')" class="py-3 bg-slate-800 text-white rounded-xl font-bold text-xs hover:bg-black transition-all shadow-lg">تحميل الملف</button>
                    <button onclick="toggleQR('q{i}', '{link}')" class="col-span-2 py-2 bg-gray-100 text-gray-600 rounded-xl text-xs font-semibold hover:bg-gray-200 uppercase">إظهار الباركود 🔳</button>
                </div>
                <div id="q{i}" class="hidden mt-4 p-4 border-2 border-dashed border-indigo-50 bg-indigo-50/30 rounded-2xl flex flex-col items-center animate-fade-in"></div>
            </div>'''
            if (i + 1) % 5 == 0: server_cards += ad_unit_html

        html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>velss - Intelligent Protection</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
    <script type="text/javascript" src="//data527.click/129ba2282fccd3392338/b1a648bd38/?placementName=default"></script>
    <style>
        body {{ font-family: 'Cairo', sans-serif; background-color: #fbfbfd; overflow-x: hidden; scroll-behavior: smooth; }}
        .gradient-text {{ background: linear-gradient(135deg, #1e1b4b 0%, #4338ca 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .ad-click {{ cursor: pointer; }}
        .filter-btn.active {{ background-color: #4338ca; color: white; }}
        #bridge-page {{ display: none; background: rgba(255,255,255,0.98); z-index: 9999; }}
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        .animate-fade-in {{ animation: fadeIn 0.4s ease-out; }}
        .no-scrollbar::-webkit-scrollbar {{ display: none; }}
    </style>
</head>
<body class="pb-10">

    <div id="bridge-page" class="fixed inset-0 flex flex-col items-center justify-center text-center p-6">
        <div class="animate-spin rounded-full h-16 w-16 border-t-4 border-indigo-600 mb-4"></div>
        <h2 class="text-2xl font-black mb-2 text-slate-800">جاري تأمين الروابط...</h2>
        <p class="text-gray-500">جاري الفحص عبر محرك velss الذكي</p>
    </div>

    <nav class="flex justify-between items-center px-6 py-5 max-w-6xl mx-auto border-b border-gray-100 bg-white sticky top-0 z-40">
        <div class="flex items-center gap-3 ad-click" onclick="triggerBridge()">
            <div class="w-10 h-10 bg-indigo-900 rounded-lg flex items-center justify-center shadow-lg"><i class="fas fa-shield-halved text-white"></i></div>
            <span class="text-xl font-black text-slate-800 uppercase tracking-tighter">velss</span>
        </div>
        <div class="text-left leading-none">
            <span id="countdown" class="text-indigo-600 font-bold text-sm block tracking-widest tabular-nums">--:--:--</span>
            <span class="text-[9px] text-gray-400 uppercase">Update Sync</span>
        </div>
    </nav>

    <section class="px-6 py-12 text-center max-w-4xl mx-auto">
        <h1 class="text-4xl md:text-6xl font-black tracking-tighter mb-4 gradient-text">خادم velss المطور</h1>
        <p class="text-gray-400 text-sm mb-8 italic">استقرار كامل ودعم لكافة بروتوكولات EXCLAVE و V2Ray.</p>
        <div class="ad-click" onclick="triggerBridge()"><img src="https://cdni.iconscout.com/illustration/premium/thumb/network-infrastructure-4437294-3684813.png" class="w-48 mx-auto"></div>
    </section>

    {ad_unit_html}

    <main class="max-w-xl mx-auto px-6">
        <div class="flex flex-col mb-10">
            <div class="flex items-center justify-between mb-2">
                <h2 class="font-black text-xl text-slate-800">سيرفرات حصرية</h2>
                <span class="bg-indigo-50 text-indigo-600 px-4 py-1 rounded-full text-[10px] font-bold border border-indigo-100 uppercase">{now}</span>
            </div>
            <p class="text-[11px] text-gray-400 leading-relaxed text-right border-r-2 border-indigo-200 pr-3">
                تم جلب أحدث العقد لضمان أفضل سرعة. يتم تحديث البيانات كل 6 ساعات لضمان الفعالية.
            </p>
        </div>
        
        <div id="servers-container">{server_cards}</div>
    </main>

    <section class="max-w-xl mx-auto px-6 mt-16 text-right">
        <div class="bg-white border border-gray-100 rounded-3xl p-8 shadow-sm space-y-6">
            <div>
                <h3 class="text-lg font-black text-slate-800 mb-2 flex items-center gap-2">
                    <i class="fas fa-file-contract text-indigo-500"></i> الشروط والخصوصية
                </h3>
                <p class="text-xs text-gray-500 leading-loose">
                    هذا الموقع velss يقدم خدمة جلب الروابط التعليمية والتقنية. باستخدامك للموقع، أنت توافق على سياسة الاستخدام العادل. نحن لا نقوم بتخزين أي بيانات خاصة بالزوار.
                    <span class="text-indigo-500 font-bold ad-click" onclick="triggerBridge()">اقرأ المزيد</span>
                </p>
            </div>
        </div>
    </section>

    <footer class="bg-slate-950 mt-20 pt-16 pb-10 px-6 text-center text-white relative">
        <p class="text-gray-500 text-[10px] uppercase tracking-widest mb-4 italic">© velss System 2026. جميع الحقوق محفوظة.</p>
    </footer>

    <div id="toast" class="fixed bottom-10 left-1/2 -translate-x-1/2 bg-slate-900 text-white px-8 py-3 rounded-full text-xs font-bold opacity-0 transition-all pointer-events-none z-50 shadow-2xl">تم النسخ بنجاح! ✅</div>

    <script>
        function downloadConfig(filename, text) {{
            const element = document.createElement('a');
            element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
            element.setAttribute('download', "velss_" + filename + ".txt");
            element.click();
        }}

        function triggerBridge() {{
            const bridge = document.getElementById('bridge-page');
            bridge.style.display = 'flex';
            setTimeout(() => {{ window.open('{my_ad_link}', '_blank'); bridge.style.display = 'none'; }}, 1200);
        }}

        function startCountdown() {{
            let h = 5, m = 59, s = 59;
            setInterval(() => {{
                s--; if(s<0){{s=59; m--;}} if(m<0){{m=59; h--;}}
                document.getElementById('countdown').innerText = String(h).padStart(2,'0')+":"+String(m).padStart(2,'0')+":"+String(s).padStart(2,'0');
            }}, 1000);
        }}
        startCountdown();

        function copyText(t) {{
            navigator.clipboard.writeText(t);
            const toast = document.getElementById('toast');
            toast.style.opacity = '1';
            setTimeout(() => toast.style.opacity = '0', 2000);
        }}

        function toggleQR(id, link) {{
            const el = document.getElementById(id);
            if (el.children.length === 0) {{
                new QRCode(el, {{ text: link, width: 160, height: 160, colorDark: "#1e1b4b" }});
            }}
            el.classList.toggle('hidden');
        }}
    </script>
</body>
</html>'''
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("✅ [velss] تم التحديث بنجاح باستخدام أحدث إصدار!")
            
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    run_velss()
