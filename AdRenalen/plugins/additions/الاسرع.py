from AdRenalen import app
from pyrogram import Client, filters
import random


words= ['كتاب', 'مدرسة', 'شمس', 'قمر', 'ماء', 'بيت', 'سماء', 'مخمر', 'حاسوب', 'برمجة', 'إنترنت', 'تاريخ', 'شبكة', 'سيارة', 'طائرة', 'أرض', 'بحر', 'جو', 'جوال', 'ساعة', 'صحة', 'حزن', 'فرح', 'عائلة', 'طاقة', 'عمل', 'دفاع', 'عدد', 'عدل', 'علم', 'غداء', 'فندق', 'قلم', 'مدير', 'نافذة', 'يمني', 'مصري', 'تونسي', 'فلسطيني', 'جزائري', 'مغربي', 'عراقي', 'لبناني', 'سوري', 'ايراني', 'سعودي', 'إماراتي', 'قطري', 'كويتي', 'عماني', 'بحريني', 'حجاب', 'عمران', 'حجرة', 'كهنة', 'بثينة', 'إنعام', 'لامار', 'نانسي', 'أمير', 'ناصر', 'صبري', 'بسام', 'هادي', 'خالد', 'كيري', 'معمر', 'ابراهيم', 'يوسف', 'حسن', 'شيرين', 'ظافر', 'نيرمين', 'محمد', 'نفيسة', 'كريم', 'ريم', 'سامر', 'سيلين', 'سلمي', 'يزن', 'كارلا', 'عبدالرحمن', 'منال', 'عوض', 'وفاء', 'فريد', 'أحمد', 'شادي', 'بلال', 'وائل', 'ديمة', 'حمزة', 'خليل', 'معتصم', 'باسم', 'عادل', 'بيار', 'التخلي', 'القدرة', 'الغياب', 'الوفرة', 'القبول', 'الوصول', 'الإنجاز', 'الدقة', 'التحقيق', 'العمل', 'التكيف', 'الإدمان', 'الإعجاب', 'المصاعب', 'المغامرة', 'المودة', 'العدوانية', 'الخفة', 'الموافقة', 'اليقظة', 'الطموح', 'المرح', ' التحليل ', 'الغضب', 'الحيوية', 'القلق', 'الاعتذار', 'التقدير', 'الموافقة', 'الوصول', 'الفنية', 'الصعود', 'التحليل', 'الطموح', 'تأكيد', 'المساعدة', 'ضمانات', 'الاهتمام', 'جذب', 'جرأة', 'سلطة', 'توافر', 'وعي', 'توازن', 'جمال', 'سلوك', 'إيمان', 'إحسان', 'منح', 'سعادة', 'جرأة', 'شجاعة', 'اختصار', 'بريق', 'هدوء', 'الألفة', 'صراحة', 'القدرة', 'الحذر', 'العناية', 'الاحتفال', 'التحدي', ' التغيرات', 'الكاريزما', 'سحر', 'البهجة', 'الخيارات', 'وضوح', 'أناقة', 'نظافة', 'وضوح العقل', 'ذكاء', 'اتساق', 'مريح', 'التزام', 'الاتصال', 'التعاطف', 'الكفاءة', 'إكمال', 'هدوء', 'التركيز', 'الثقة', 'المطابقة', 'الاتصال', 'وعي', 'اتساق', 'رضى', 'استمرارية', 'المساهمة', 'التحكم', 'إيمان', 'التعاون', 'شجاعة', 'أدب', 'إبداع', 'مصداقية', 'فضول', 'جرأة', 'تفانٍ', 'عمق']
@app.on_message(filters.regex("الاسرع"))
def send(client, message):
    pc_word = random.choice(words)
    jum_word = ''.join(random.sample(pc_word, len(pc_word)))
    ju = " ".join(jum_word)
    message.reply(f"""
** اعد ترتيب هذة الكلمة **
-> {ju}
    """)

@app.on_message(filters.text)
def check(client, message):
    word = message.text
    for w in words:
        if word == w:
        	message.reply("صح")
