from pathlib import Path
from shutil import copy2
from html import escape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, Preformatted, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from PIL import Image as PILImage
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'report/lab5-htmlcss-variant5.pdf'
DESKTOP=Path('/Users/maksimginchak/Desktop/Лабораторні/HTML/Лаба 5 HTML CSS варіант 5.pdf')
pdfmetrics.registerFont(TTFont('ArialUA','/Library/Fonts/Arial Unicode.ttf'))
pdfmetrics.registerFont(TTFont('ArialBold','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
pdfmetrics.registerFontFamily('ArialUA',normal='ArialUA',bold='ArialBold')
pdfmetrics.registerFont(TTFont('CourierUA','/System/Library/Fonts/Supplemental/Courier New.ttf'))
BLUE=colors.HexColor('#174a7e'); LINE=colors.HexColor('#c9d8e2'); PALE=colors.HexColor('#f2f8fb')
body=ParagraphStyle('body',fontName='ArialUA',fontSize=10.5,leading=16,spaceAfter=8)
heading=ParagraphStyle('heading',fontName='ArialBold',fontSize=13,leading=18,textColor=BLUE,spaceBefore=5,spaceAfter=9)
example=ParagraphStyle('example',parent=heading,fontSize=14,leading=19,spaceAfter=11)
small=ParagraphStyle('small',parent=body,fontSize=10,leading=14)
cell=ParagraphStyle('cell',parent=body,fontSize=9,leading=13,spaceAfter=0)
white=ParagraphStyle('white',parent=cell,fontName='ArialBold',textColor=colors.white)
code=ParagraphStyle('code',fontName='CourierUA',fontSize=8,leading=10)
WIDTH=470.5512
story=[]
def p(s,style=body): return Paragraph(s,style)
def h(s): story.append(p(s,heading))
def paragraph(s): story.append(p(s))
def screenshot(name):
 path=ROOT/'report'/name
 w,ht=PILImage.open(path).size
 story.append(Image(str(path),width=WIDTH,height=ht*WIDTH/w))
 story.append(Spacer(1,10))
def source(text):
 block=Preformatted(text.strip(),code)
 t=Table([[block]],colWidths=[WIDTH],hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('BOX',(0,0),(-1,-1),.5,LINE),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10)]))
 story.append(t);story.append(Spacer(1,10))
def page(): story.append(PageBreak())
def example_start(title):
 story.append(p(title,example))
 story.append(p('Сторінка: forms.html. Скріншот реального сайту у Chrome, ширина вікна 1280 px.',small))

story.append(Spacer(1,680));page()
h('Завдання')
paragraph('Розробити для вебпроєкту сторінку введення інформації про товари за допомогою форм. Задати action="#" і виконувати перевірку введених даних без надсилання на сервер. Використати обов’язкові теги, атрибути та CSS-властивості варіанта №5.')
h('Варіант №5')
paragraph('Вебпроєкт ByteMarket присвячено комп’ютерним комплектуючим та аксесуарам. Додано форму замовлення: контакти покупця, вибір моделі й кількості, отримання та побажання. У каталозі 8 вигаданих моделей у 4 категоріях; ціни та залишки узгоджено з лабораторною №4.')
paragraph('Обов’язкові типи input: submit, checkbox, week, month, email, search, url, tel. Також використано text, number та image. Атрибути полів: style, maxlength, autofocus, step, minlength, autocomplete, checked, alt, min, formtarget, multiple, value. Form містить autocomplete, action, class, dir, style, lang.')
paragraph('Використано textarea (disabled, dirname, lang, title, required, class, style), button (form, type, name, disabled), legend (lang, title, dir), optgroup (style, class, id), label (id, form, title), summary (title, class, id), progress (max, id, lang), meter (class, title, max, min, high), keygen (id, dir, form, style, lang). Атрибути розподілено між елементами відповідного тегу.')
h('Розв’язування')
paragraph('Створено окремий проєкт на основі лабораторної №4. Додано forms.html, assets/css/forms.css і assets/js/forms.js; на всіх семи сторінках є пункт «Форми». Поля об’єднано через fieldset і legend, підписи пов’язано через label та for. Пошук фільтрує товари, вибір моделі змінює граничну кількість, ціну й індикатор запасу. Progress показує заповнення 7 обов’язкових полів.')
paragraph('Задано шрифти sans-serif, Lucida Sans Unicode, Lucida Sans Regular, Geneva, Arial Narrow; вагу 900 і lighter, small-caps, font: icon, normal, semi-condensed, extra-expanded. Використано text-indent у відсотках, underline, capitalize, letter-spacing і white-space: pre. Правила друку задають size: auto, marks: cross, розриви сторінок, widows та orphans.')
paragraph('Застарілий keygen наведено як прихований навчальний елемент. Звукові правила CSS2 винесено в @media speech; звичайний браузер їх не озвучує. Приклади містяться в розкривному розділі. Працездатність форми не залежить від підтримки цих застарілих засобів.')
page()
h('Тестові приклади')
rows=[['№','Перевірка','Отриманий результат'],['1','Надіслати порожню форму','Підсумок не з’являється; обов’язкові поля блокують надсилання.'],['2','Помилкові email, телефон, URL','Некоректний формат відхилено. Дві коректні email-адреси через кому прийнято.'],['3','Кількість 0, 1.5 або 13 для Vision','Відхилено: min=1, step=1, залишок моделі — 12 шт.'],['4','Пошук Vision і запиту без збігів','Доступні 2 моделі Vision; за відсутності збігів показано повідомлення.'],['5','Правильні дані, Vision, 2 шт.','Підсумок: 17 800 грн. Progress: 7 із 7. Запити з даними форми не виконуються.'],['6','Побажання лише з пробілів','Відхилено. Крайні пробіли не враховуються в мінімальній довжині.'],['7','Кнопка «Очистити»','Контакти й підсумок очищено, пакування увімкнено, прогрес повернувся до 1 із 7.'],['8','Екран 390 px, кнопка-зображення','Одноколонкова форма без горизонтального виходу; перевірка працює.'],['9','Вимкнений JavaScript','Обидві кнопки надсилання вимкнені, тому дані не потрапляють у URL.']]
t=Table([[p(escape(s),white if i==0 else cell) for s in row] for i,row in enumerate(rows)],colWidths=[28,166,WIDTH-194],hAlign='LEFT')
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),BLUE),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),('GRID',(0,0),(-1,-1),.5,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
story.append(t);story.append(Spacer(1,10))
h('Висновки')
paragraph('Реалізовано сторінку форм ByteMarket за варіантом №5. HTML-обмеження та JavaScript перевіряють формат і допустимі значення; результат виводиться локально. Перевірено пошук, розрахунок вартості, індикатори, скидання та мобільний вигляд у Chrome. У цій роботі новою є сторінка форм, а таблиця варіанта №5 з попередньої роботи збережена.')
h('Репозиторій')
paragraph('<link href="https://github.com/MaksHinchak/html-lab-05-variant-5" color="#174a7e">https://github.com/MaksHinchak/html-lab-05-variant-5</link>')
page()
example_start('Приклад 1. Контактні поля та їх перевірка')
screenshot('contact-fields.png')
paragraph('Відповідні блоки forms.html')
source('''<form id="order-form" autocomplete="on" action="#"
      class="order-form" dir="ltr" lang="uk"
      style="font-style: normal;">
  <input id="customer" type="text" required
         minlength="2" maxlength="80" autocomplete="name">
  <input id="email" type="email" multiple required>
  <input id="phone" type="tel" required
         pattern="(\\+380|0)[0-9]{9}">
  <input id="website" type="url">
</form>''')
paragraph('Наведено скорочений фрагмент. required позначає обов’язкові поля; type="email" та type="url" перевіряють формат. multiple дозволяє перелік email-адрес через кому. Телефон має починатися з 0 або +380 і містити 9 наступних цифр. minlength і maxlength обмежують довжину імені; JavaScript додатково відхиляє текст лише з пробілів.')
paragraph('Кожне поле має підпис label. Контактні поля розміщено у fieldset із заголовком legend. CSS Grid виводить дві колонки на широкому екрані й одну на телефоні. Обов’язкові поля позначено зірочкою, а допустимі формати пояснено біля полів.')
page()
example_start('Приклад 2. Каталог, вартість та індикатор запасу')
screenshot('product-fields.png')
paragraph('Відповідні блоки assets/js/forms.js')
source('''const selected = product.selectedOptions[0];
const stock = Number(selected?.dataset.stock || 30);
const price = Number(selected?.dataset.price || 0);
quantity.max = String(stock);
const count = Number(quantity.value);
const validCount = quantity.validity.valid
  && Number.isInteger(count);
document.getElementById("total").value =
  money(validCount ? price * count : 0);
meter.max = stock;
meter.high = Math.ceil(stock * .8);''')
paragraph('Товари згруповано за допомогою optgroup. Ціни та залишки зберігаються в data-price і data-stock. Після вибору моделі max обмежує кількість фактичним запасом; min="1" і step="1" не допускають нульових та дробових значень. Для 2 відеокарт BM Vision 8G отримано 8 900 × 2 = 17 800 грн.')
paragraph('Meter показує, яку частину запасу займає вибрана кількість. Progress окремо показує кількість правильно заповнених обов’язкових полів. Поле search фільтрує доступні варіанти без завантаження даних із мережі.')
page()
example_start('Приклад 3. Локальний підсумок замовлення')
screenshot('order-result.png')
paragraph('Відповідні блоки assets/js/forms.js')
source('''form.addEventListener("submit", event => {
  event.preventDefault();
  refresh();
  if (!form.reportValidity()) return;
  // Далі формується локальний підсумок через textContent.
});''')
paragraph('preventDefault зупиняє стандартне надсилання форми. reportValidity перевіряє всі поля. Підсумок формується через textContent: введений текст не виконується як HTML. Кнопки submit та image запускають однакову перевірку; кнопка reset очищує форму й приховує результат.')
paragraph('Додаткові приклади шрифтів містяться в розділі «Шрифти та додаткові елементи варіанта 5». Keygen є застарілим елементом; звукові правила CSS2 наведено як навчальні декларації. Підтримка цих властивостей залежить від пристрою. Джерела: <link href="https://html.spec.whatwg.org/multipage/obsolete.html" color="#174a7e">WHATWG HTML</link>, <link href="https://www.w3.org/TR/CSS2/aural.html" color="#174a7e">W3C CSS2: Aural style sheets</link>.')

def decorate(c,doc):
 c.setFont('ArialUA',9); c.setFillColor(colors.HexColor('#587083'))
 c.drawRightString(538.9134,34,str(doc.page))
 if doc.page==1:
  c.setFillColor(colors.black);c.setFont('ArialUA',12)
  for y,line in [(688.89,'Чернівецький національний університет'),(669.89,'імені Юрія Федьковича'),(650.89,'Навчально-науковий інститут фізико-технічних'),(631.89,'та комп’ютерних наук')]: c.drawCentredString(A4[0]/2,y,line)
  c.setFont('ArialUA',17)
  for y,line in [(495.89,'ЗВІТ'),(470.89,'про виконання лабораторної роботи №5'),(445.89,'з дисципліни «Веб-програмування»')]: c.drawCentredString(A4[0]/2,y,line)
  c.setFont('ArialUA',12);c.drawCentredString(A4[0]/2,423.89,'Тема: Проєктування вебдокументів. Сторінка форм')
  author_lines=[(303.39,'Виконав: студент групи 241-А'),(284.39,'Гінчак Максим Богданович'),(265.39,'Перевірив:'),(246.39,'Нестеренко Володимир Васильович')]
  for y,line in author_lines: c.drawRightString(538.9134,y,line)
  c.drawCentredString(A4[0]/2,48,'Чернівці · 2026')

SimpleDocTemplate(str(OUT),pagesize=A4,leftMargin=62.3622,rightMargin=50.3622,topMargin=56,bottomMargin=46,title='Лабораторна робота №5. HTML CSS. Варіант 5',author='Гінчак Максим Богданович').build(story,onFirstPage=decorate,onLaterPages=decorate)
r=PdfReader(OUT)
assert len(r.pages)==6,len(r.pages)
for index,page_obj in enumerate(r.pages):
 assert len(page_obj.extract_text())>50
 assert abs(float(page_obj.mediabox.width)-A4[0])<1
links=[a.get_object().get('/A',{}).get('/URI') for pg in r.pages for a in pg.get('/Annots',[])]
assert 'https://github.com/MaksHinchak/html-lab-05-variant-5' in links
copy2(OUT,DESKTOP)
assert OUT.read_bytes()==DESKTOP.read_bytes()
print('Created matching 6-page A4 report:',DESKTOP)
