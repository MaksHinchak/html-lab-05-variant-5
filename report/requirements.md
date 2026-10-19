# Відповідність варіанту 5

| Тег | Обов’язкові атрибути | Перевірка |
| --- | --- | --- |
| `form` | `autocomplete`, `action`, `class`, `dir`, `style`, `lang` | Є в розмітці |
| `input` | `style`, `maxlength`, `autofocus`, `step`, `minlength`, `autocomplete`, `checked`, `alt`, `min`, `formtarget`, `multiple`, `value` | Є в розмітці |
| `textarea` | `disabled`, `dirname`, `lang`, `title`, `required`, `class`, `style` | Є в розмітці |
| `button` | `form`, `type`, `name`, `disabled` | Є в розмітці |
| `legend` | `lang`, `title`, `dir` | Є в розмітці |
| `optgroup` | `style`, `class`, `id` | Є в розмітці |
| `label` | `id`, `form`, `title` | Є в розмітці |
| `summary` | `title`, `class`, `id` | Є в розмітці |
| `progress` | `max`, `id`, `lang` | Є в розмітці |
| `meter` | `class`, `title`, `max`, `min`, `high` | Є в розмітці |
| `keygen` | `id`, `dir`, `form`, `style`, `lang` | Є в розмітці |

Типи input: checkbox, email, image, month, number, search, submit, tel, text, url, week.

CSS для шрифтів і тексту наведено в `assets/css/forms.css`; правила друку — у `@media print` і `@page`, старі звукові властивості — у `@media speech`. Застарілий `keygen` включено за умовою, але генерація ключів через нього не виконується. Повторені атрибути та значення з методички враховано один раз.

У `forms.html` `keygen` явно закрито. Дві локальні інструкції `suppress` пояснюють PyCharm винятки методички: застарілий `keygen` та непідтримуваний у сучасному HTML атрибут `form` для `label`. Інші HTML-перевірки залишаються увімкненими; зв’язок підпису з полем забезпечують `for` і `id`.
