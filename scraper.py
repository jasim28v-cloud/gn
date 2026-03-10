import requests
import re
from datetime import datetime

def run_freevmess_2026():
    # الرابط المصدر للسحب
    url = "https://t.me/s/exclaveVPN"
    # الرابط الإعلاني الخاص بك
    my_ad_link = "https://data527.click/21330bf1d025d41336e6/57154ac610/?placementName=default"
    
    # الرؤوس (Headers) الحديثة لضمان جلب البيانات بنجاح وتخطي الحماية
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Referer': 'https://www.google.com/',
        'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        
        # كود ذكي لقراءة كافة روابط exclave (vless, vmess, trojan, ssh)
        pattern = r'(?:exclave|vless|vmess|trojan|ss|ssh)://[^\s<"\'\s]+'
        links = re.findall(pattern, response.text, re.IGNORECASE)
        
        # تنظيف الروابط ومنع التكرار
        clean_links = list(dict.fromkeys([l.replace('&amp;', '&').strip() for l in links]))

        server_cards = ""
        for i, link in enumerate(clean_links):
            # تمييز نوع السيرفر
            proto_type = "EXCLAVE" if "exclave" in link.lower() else link.split('://')[0].upper()
            
            server_cards += f'''
            <div class="server-card bg-white border border-gray-100 p-6 rounded-[2.5rem] shadow-sm hover:shadow-xl transition-all mb-6 text-right">
                <div class="flex justify-between items-center mb-4">
                    <span class="bg-blue-600 text-white text-[10px] font-bold px-4 py-1 rounded-full uppercase italic tracking-tighter">{proto_type} PREMIUM</span>
                    <button onclick="copyText('{link}')" class="text-gray-300 hover:text-blue-600 transition-colors"><i class="far fa-copy text-lg"></i></button>
                </div>
                <div class="bg-slate-50 p-4 rounded-2xl mb-6 border border-gray-50">
                    <p class="text-[10px] font-mono text-slate-400 break-all leading-relaxed line-clamp-2">{link}</p>
                </div>
                <div class="grid grid-cols-2 gap-3">
                    <button onclick="copyText('{link}')" class="py-4 bg-blue-600 text-white rounded-2xl font-bold text-xs shadow-lg shadow-blue-100 active:scale-95 transition-all">نسخ الإعدادات</button>
                    <button onclick="toggleQR('q{i}', '{link}')" class="py-4 bg-slate-900 text-white rounded-2xl font-bold text-xs active:scale-95 transition-all">QR CODE 🔳</button>
                </div>
                <div id="q{i}" class="hidden mt-5 p-5 bg-white rounded-3xl flex justify-center border-2 border-dashed border-blue-50 animate-fade-in"></div>
            </div>'''
            
            # حقن الإعلان بعد كل 5 سيرفرات
            if (i + 1) % 5 == 0:
                server_cards += f'<div class="flex justify-center my-8"><ins class="g2fb0b4c321 rounded-3xl overflow-hidden" data-domain="//data527.click" data-affquery="/e3435b2a507722939b6f/2fb0b4c321/?placementName=default" style="display:inline-block;width:300px;height:250px"><script src="//data527.click/js/responsive.js" async></script></ins></div>'

        html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>freevmess - نظام التشفير العالمي</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Cairo', sans-serif; background-color: #f8fafc; color: #1e293b; }}
        .nav-glass {{ background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(12px); }}
        .animate-fade-in {{ animation: fadeIn 0.3s ease-in; }}
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    </style>
</head>
<body class="antialiased pb-20">

    <nav class="nav-glass border-b border-gray-100 sticky top-0 z-50 px-6 py-4 flex justify-between items-center">
        <div class="flex items-center gap-3 cursor-pointer" onclick="window.open('{my_ad_link}')">
            <div class="w-10 h-10 bg-blue-600 rounded-2xl flex items-center justify-center shadow-lg shadow-blue-200"><i class="fas fa-shield-halved text-white"></i></div>
            <span class="text-2xl font-black text-slate-900 uppercase tracking-tighter">freevmess</span>
        </div>
        <div id="timer" class="text-blue-600 font-bold text-xs bg-blue-50 px-4 py-2 rounded-xl border border-blue-100">00:00:00</div>
    </nav>

    <header class="max-w-2xl mx-auto px-6 py-16 text-center">
        <h1 class="text-5xl font-black text-slate-900 mb-4 tracking-tight">خوادم <span class="text-blue-600">Freevmess</span></h1>
        <p class="text-slate-400 text-sm leading-relaxed italic">تحديث تلقائي لأحدث روابط exclave المشفرة بخصوصية مطلقة.</p>
    </header>

    <main class="max-w-xl mx-auto px-6">
        <div id="servers-list">{server_cards}</div>

        <div class="mt-24 space-y-12 bg-white p-10 rounded-[3rem] border border-gray-100 shadow-sm text-right transition-all hover:shadow-md">
            
            <section>
                <h2 class="text-2xl font-black text-slate-900 mb-8 border-r-4 border-blue-600 pr-4">خادمنا</h2>
                <div class="space-y-8">
                    <div class="p-6 bg-blue-50/30 rounded-3xl border border-blue-50">
                        <p class="text-sm text-slate-600 leading-loose">أحد أفضل مزودي خدمات الخوادم الافتراضية الخاصة والخوادم المخصصة الذين نعتقد أنهم قادرون على توفير أفضل أداء.</p>
                        <p class="font-black text-blue-600 mt-3 text-lg">- فولتر</p>
                    </div>
                    <div class="p-6 bg-sky-50/30 rounded-3xl border border-sky-50">
                        <p class="text-sm text-slate-600 leading-loose">أحد أفضل مزودي خدمات الخوادم الافتراضية الخاصة والخوادم المخصصة الذين نعتقد أنهم قادرون على توفير أفضل أداء.</p>
                        <p class="font-black text-blue-600 mt-3 text-lg">- ديجيتال أوشن</p>
                    </div>
                </div>
            </section>

            <section class="pt-10 border-t border-slate-50 space-y-12">
                <div>
                    <h3 class="text-xl font-black text-slate-900 mb-5">الشروط والأحكام</h3>
                    <p class="text-xs text-slate-400 leading-loose text-justify">
                        تحدد هذه الشروط والأحكام قواعد استخدام موقع freevmess الإلكتروني، الموجود على الرابط <strong>https://jasim28v-cloud.github.io/gn/</strong> . بدخولك إلى هذا الموقع، فإننا نفترض موافقتك على هذه الشروط والأحكام. يُرجى عدم الاستمرار في استخدام freevmess إذا كنت لا توافق على جميع الشروط والأحكام المذكورة في هذه الصفحة. تنطبق المصطلحات التالية على هذه الشروط والأحكام، وبيان الخصوصية، وإشعار إخلاء المسؤولية، وجميع الاتفاقيات: "العميل"، "أنت"، و"خاصتك" تشير إليك، الشخص الذي يدخل إلى هذا الموقع ويوافق على شروط وأحكام الشركة... <span class="text-blue-600 font-bold cursor-pointer underline" onclick="window.open('{my_ad_link}')">اقرأ المزيد</span>
                    </p>
                </div>

                <div>
                    <h3 class="text-xl font-black text-slate-900 mb-5">سياسة الخصوصية</h3>
                    <p class="text-xs text-slate-400 leading-loose text-justify">
                        في موقع freevmess، الذي يمكن الوصول إليه عبر الرابط <strong>https://jasim28v-cloud.github.io/gn/</strong> ، تُعدّ خصوصية زوارنا من أهم أولوياتنا. تحتوي وثيقة سياسة الخصوصية هذه على أنواع المعلومات التي يجمعها موقع freevmess ويسجلها، وكيفية استخدامنا لها. إذا كانت لديكم أي أسئلة إضافية أو كنتم بحاجة إلى مزيد من المعلومات حول سياسة الخصوصية الخاصة بنا، فلا تترددوا في الاتصال بنا.
                    </p>
                </div>

                <div>
                    <h3 class="text-xl font-black text-slate-900 mb-5 uppercase">ملفات السجل</h3>
                    <p class="text-xs text-slate-400 leading-loose text-justify">
                        تتبع منصة Freevmess إجراءً قياسيًا لاستخدام ملفات السجل. تسجل هذه الملفات زيارات المستخدمين للمواقع الإلكترونية. هذا إجراء شائع لدى جميع شركات الاستضافة، وهو جزء من تحليلات خدمات الاستضافة. تتضمن المعلومات التي تجمعها ملفات السجل عناوين بروتوكول الإنترنت (IP)... <span class="text-blue-600 font-bold cursor-pointer underline" onclick="window.open('{my_ad_link}')">اقرأ المزيد</span>
                    </p>
                </div>
            </section>
        </div>
    </main>

    <footer class="mt-24 py-12 text-center border-t border-gray-100 bg-white shadow-inner">
        <p class="text-slate-400 text-[10px] uppercase font-black tracking-[0.4em] italic mb-2">© Freevmess.com. جميع الحقوق محفوظة.</p>
        <div class="flex justify-center gap-6 text-slate-300 mt-4">
            <i class="fab fa-telegram hover:text-blue-600 cursor-pointer transition-colors"></i>
            <i class="fas fa-lock hover:text-blue-600 cursor-pointer transition-colors"></i>
        </div>
    </footer>

    <div id="toast" class="fixed bottom-10 left-1/2 -translate-x-1/2 bg-slate-900 text-white px-10 py-4 rounded-3xl text-sm font-bold opacity-0 transition-all pointer-events-none z-[100] shadow-2xl border border-slate-800">تم نسخ السيرفر بنجاح! ✨</div>

    <script>
        function copyText(t) {{
            navigator.clipboard.writeText(t);
            const toast = document.getElementById('toast');
            toast.style.opacity = '1';
            toast.style.transform = 'translate(-50%, -10px)';
            setTimeout(() => {{ toast.style.opacity = '0'; toast.style.transform = 'translate(-50%, 0)'; }}, 2500);
        }}
        function toggleQR(id, link) {{
            const el = document.getElementById(id);
            if (el.innerHTML === "") new QRCode(el, {{ text: link, width: 180, height: 180, colorDark: "#1e293b" }});
            el.classList.toggle('hidden');
        }}
        function startTimer() {{
            let h=5, m=59, s=59;
            setInterval(() => {{
                s--; if(s<0){{s=59; m--;}} if(m<0){{m=59; h--;}}
                document.getElementById('timer').innerText = String(h).padStart(2,'0')+":"+String(m).padStart(2,'0')+":"+String(s).padStart(2,'0');
            }}, 1000);
        }}
        startTimer();
    </script>
</body>
</html>'''
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("✅ [Freevmess 2026] تم التحديث بنجاح: الرؤوس جاهزة، الاسم صحيح، والنصوص كاملة!")
            
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    run_freevmess_2026()
