import requests
import re
from datetime import datetime

def run_velss():
    url = "https://t.me/s/exclaveVPN"
    # الرابط الإعلاني الخاص بك
    my_ad_link = "https://data527.click/21330bf1d025d41336e6/57154ac610/?placementName=default"
    
    # الرؤوس المتطورة (Chrome 124) لضمان جلب البيانات بنجاح
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'Referer': 'https://www.google.com/',
        'Connection': 'keep-alive'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=25)
        
        # البحث عن كل الروابط بما فيها روابط exclave الجديدة
        pattern = r'(?:exclave|vless|vmess|trojan|ss|ssh)://[^\s<"\'\s]+'
        links = re.findall(pattern, response.text, re.IGNORECASE)
        
        clean_links = []
        for l in links:
            c = l.replace('&amp;', '&').split('<')[0].split('"')[0].strip()
            if c not in clean_links: clean_links.append(c)
        
        now = datetime.now().strftime("%Y-%m-%d")
        
        # كود الإعلان المدمج
        ad_unit_html = f'''
        <div class="flex justify-center my-8">
            <ins style="width: 300px;height:250px" data-width="300" data-height="250" class="g2fb0b4c321" data-domain="//data527.click" data-affquery="/e3435b2a507722939b6f/2fb0b4c321/?placementName=default">
                <script src="//data527.click/js/responsive.js" async></script>
            </ins>
        </div>'''

        server_cards = ""
        for i, link in enumerate(clean_links):
            # تمييز نوع السيرفر (EXCLAVE أو بروتوكول عادي)
            proto_raw = link.split('://')[0].upper()
            display_proto = f"EXCLAVE {link.split('://')[1].split('?')[0].split(':')[0].upper()}" if "EXCLAVE" in proto_raw else proto_raw
            
            server_cards += f'''
            <div class="server-card bg-white border border-gray-100 p-5 rounded-3xl shadow-sm hover:shadow-md transition-all mb-4 text-right">
                <div class="flex justify-between items-center mb-3">
                    <span class="bg-indigo-600 text-white px-4 py-1 rounded-full text-[10px] font-bold uppercase">{display_proto}</span>
                    <button onclick="copyText('{link}')" class="text-gray-400 hover:text-indigo-600"><i class="far fa-copy"></i></button>
                </div>
                <p class="text-[9px] text-gray-400 font-mono break-all mb-4 bg-gray-50 p-2 rounded">{link[:95]}...</p>
                <div class="grid grid-cols-2 gap-2">
                    <button onclick="copyText('{link}')" class="py-3 bg-indigo-600 text-white rounded-xl font-bold text-xs">نسخ الإعدادات</button>
                    <button onclick="toggleQR('q{i}', '{link}')" class="py-3 bg-slate-800 text-white rounded-xl font-bold text-xs">كود QR 🔳</button>
                </div>
                <div id="q{i}" class="hidden mt-4 p-4 bg-white rounded-2xl flex justify-center border-2 border-dashed border-indigo-50"></div>
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
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <script type="text/javascript" src="//data527.click/129ba2282fccd3392338/b1a648bd38/?placementName=default"></script>
    <style>
        body {{ font-family: 'Cairo', sans-serif; background-color: #fbfbfd; }}
        .ad-click {{ cursor: pointer; }}
        #bridge-page {{ display: none; background: rgba(255,255,255,0.98); z-index: 9999; }}
        .gradient-text {{ background: linear-gradient(135deg, #1e1b4b 0%, #4338ca 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
    </style>
</head>
<body class="pb-10">

    <div id="bridge-page" class="fixed inset-0 flex flex-col items-center justify-center text-center p-6">
        <div class="animate-spin rounded-full h-16 w-16 border-t-4 border-indigo-600 mb-4"></div>
        <h2 class="text-xl font-black">جاري المعالجة...</h2>
    </div>

    <nav class="flex justify-between items-center px-6 py-5 bg-white border-b sticky top-0 z-40">
        <div class="flex items-center gap-2 ad-click" onclick="triggerBridge()">
            <div class="w-10 h-10 bg-indigo-900 rounded-xl flex items-center justify-center shadow-lg"><i class="fas fa-bolt text-white"></i></div>
            <span class="text-2xl font-black text-slate-800 uppercase tracking-tighter">velss</span>
        </div>
        <div class="text-indigo-600 font-bold text-sm tabular-nums" id="countdown">--:--:--</div>
    </nav>

    <header class="px-6 py-12 text-center">
        <h1 class="text-4xl font-black mb-4 gradient-text">خادم velss الذكي</h1>
        <p class="text-gray-400 text-sm">أحدث العقد لروابط exclave والبروتوكولات العالمية.</p>
    </header>

    {ad_unit_html}

    <main class="max-w-xl mx-auto px-6">
        <div id="servers-container">{server_cards}</div>

        <section class="mt-20 text-right">
            <h2 class="text-2xl font-black text-slate-800 mb-8 border-r-4 border-indigo-600 pr-4">خادمنا</h2>
            
            <div class="bg-white p-6 rounded-3xl border border-gray-100 mb-6 shadow-sm">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Vultr_Logo.svg/1200px-Vultr_Logo.svg.png" class="h-8 mb-4">
                <p class="text-xs text-gray-500 leading-loose mb-4">أحد أفضل مزودي خدمات الخوادم الافتراضية الخاصة والخوادم المخصصة الذين نعتقد أنهم قادرون على توفير أفضل أداء.</p>
                <span class="text-indigo-600 font-bold text-sm">- فولتر</span>
            </div>

            <div class="bg-white p-6 rounded-3xl border border-gray-100 mb-6 shadow-sm">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/DigitalOcean_logo.svg/1200px-DigitalOcean_logo.svg.png" class="h-8 mb-4">
                <p class="text-xs text-gray-500 leading-loose mb-4">أحد أفضل مزودي خدمات الخوادم الافتراضية الخاصة والخوادم المخصصة الذين نعتقد أنهم قادرون على توفير أفضل أداء.</p>
                <span class="text-indigo-600 font-bold text-sm">- ديجيتال أوشن</span>
            </div>
        </section>

        <section class="mt-16 space-y-8 text-right opacity-80">
            <div>
                <h3 class="font-bold text-slate-800 mb-2">الشروط والأحكام</h3>
                <p class="text-[11px] text-gray-500 leading-loose">
                    تحدد هذه الشروط والأحكام قواعد استخدام موقع velss الإلكتروني، الموجود على الرابط https://jasim28v-cloud.github.io/gn/. بدخولك إلى هذا الموقع، فإننا نفترض موافقتك على هذه الشروط والأحكام. يُرجى عدم الاستمرار في استخدام velss إذا كنت لا توافق على جميع الشروط والأحكام المذكورة في هذه الصفحة... <span class="text-indigo-600 font-bold ad-click" onclick="triggerBridge()">اقرأ المزيد</span>
                </p>
            </div>

            <div>
                <h3 class="font-bold text-slate-800 mb-2">سياسة الخصوصية</h3>
                <p class="text-[11px] text-gray-500 leading-loose">
                    في موقع velss، الذي يمكن الوصول إليه عبر الرابط https://jasim28v-cloud.github.io/gn/، تُعدّ خصوصية زوارنا من أهم أولوياتنا. تحتوي وثيقة سياسة الخصوصية هذه على أنواع المعلومات التي يجمعها موقع velss ويسجلها، وكيفية استخدامنا لها.
                </p>
            </div>

            <div>
                <h3 class="font-bold text-slate-800 mb-2">ملفات السجل</h3>
                <p class="text-[11px] text-gray-500 leading-loose">
                    تتبع منصة velss إجراءً قياسيًا لاستخدام ملفات السجل. تسجل هذه الملفات زيارات المستخدمين للمواقع الإلكترونية. تتضمن المعلومات التي تجمعها ملفات السجل عناوين بروتوكول الإنترنت (IP)... <span class="text-indigo-600 font-bold ad-click" onclick="triggerBridge()">اقرأ المزيد</span>
                </p>
            </div>
        </section>
    </main>

    <footer class="mt-20 py-10 text-center border-t bg-white">
        <p class="text-gray-400 text-[10px] uppercase tracking-widest italic mb-2">© velss.com. جميع الحقوق محفوظة.</p>
    </footer>

    <div id="toast" class="fixed bottom-10 left-1/2 -translate-x-1/2 bg-slate-900 text-white px-6 py-3 rounded-2xl text-xs font-bold opacity-0 transition-all pointer-events-none z-50">تم النسخ بنجاح! ✅</div>

    <script>
        function triggerBridge() {{
            const b = document.getElementById('bridge-page');
            b.style.display = 'flex';
            setTimeout(() => {{ window.open('{my_ad_link}', '_blank'); b.style.display = 'none'; }}, 1200);
        }}

        function copyText(t) {{
            navigator.clipboard.writeText(t);
            const toast = document.getElementById('toast');
            toast.style.opacity = '1';
            setTimeout(() => toast.style.opacity = '0', 2000);
        }}

        function toggleQR(id, link) {{
            const el = document.getElementById(id);
            if (el.innerHTML === "") new QRCode(el, {{ text: link, width: 150, height: 150 }});
            el.classList.toggle('hidden');
        }}

        function startTimer() {{
            let h=5, m=59, s=59;
            setInterval(() => {{
                s--; if(s<0){{s=59; m--;}} if(m<0){{m=59; h--;}}
                document.getElementById('countdown').innerText = String(h).padStart(2,'0')+":"+String(m).padStart(2,'0')+":"+String(s).padStart(2,'0');
            }}, 1000);
        }}
        startTimer();
    </script>
</body>
</html>'''
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("✅ [velss] تم التحديث بنجاح! مبروك يا بطل.")
            
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    run_velss()
