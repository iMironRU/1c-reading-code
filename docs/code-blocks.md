# Реестр блоков кода

> Файл собирается автоматически. Не править руками — правьте разметку ограждений
> в главах и пересоберите.

Каждый блок кода в книге отнесён к одной кучке. Кучка определяется **прогоном через
ядро [BSLexicon](https://github.com/iMironRU/BSLexicon)**, а не по виду листинга:
блок либо исполняется, либо нет, и причина известна точно.

| Кучка | Блоков | Что это |
|---|---:|---|
| `песочница` | 226 | исполняется в тренажёре — кнопка «Запустить», проверяется гейтом |
| `набросок` | 210 | чистый язык, но пока не исполняется: не хватает контекста или точек с запятой |
| `платформа` | 20 | запросы, клиент-сервер, справочники — тренажёр этого не умеет по замыслу |
| `шаблон` | 21 | форма конструкции с плейсхолдерами в угловых скобках |
| `ловушка` | 5 | код, показанный нарочно неверным или бесконечным |
| `текст` | 193 | не код: таблица данных, вывод программы, дерево, схема, проза |
| **всего** | **675** | |

## Что с этим делать

**`песочница`** — готово. Гейт следит, чтобы оставалось исполнимым.

**`набросок`** — резерв. Каждый такой блок может стать песочницей, если дописать
недостающее. Но это правка **текста книги**, а не разметки: где-то контекст задан
в соседнем абзаце нарочно, и дублировать его в листинге — испортить подачу.
Решение по каждому — авторское.

**`платформа`**, **`шаблон`**, **`ловушка`** — так и останутся. Машина их не
проверит: тренажёр не знает языка запросов, плейсхолдер не является кодом,
а ловушка неисправна намеренно.

**`текст`** — вообще не код.

## `песочница` — 226

| Где | Первая строка | Почему |
|---|---|---|
| [chapters/00_vvedenie/00-03_chto_takoe_programma.md:41](../chapters/00_vvedenie/00-03_chto_takoe_programma.md) | `Цена = 250` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/00_vvedenie/00-03_chto_takoe_programma.md:121](../chapters/00_vvedenie/00-03_chto_takoe_programma.md) | `Цена = 250` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/00_vvedenie/00-03_chto_takoe_programma.md:161](../chapters/00_vvedenie/00-03_chto_takoe_programma.md) | `Цена = 250` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/00_vvedenie/00-03_chto_takoe_programma.md:274](../chapters/00_vvedenie/00-03_chto_takoe_programma.md) | `А = 10` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/00_vvedenie/00-03_chto_takoe_programma.md:294](../chapters/00_vvedenie/00-03_chto_takoe_programma.md) | `Цена = 100` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/00_vvedenie/00-04_kompyuter_bukvalen.md:39](../chapters/00_vvedenie/00-04_kompyuter_bukvalen.md) | `Цена = 250` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/00_vvedenie/00-04_kompyuter_bukvalen.md:83](../chapters/00_vvedenie/00-04_kompyuter_bukvalen.md) | `Цена = 250` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/00_vvedenie/00-04_kompyuter_bukvalen.md:146](../chapters/00_vvedenie/00-04_kompyuter_bukvalen.md) | `Сумма = 1000` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/00_vvedenie/00-04_kompyuter_bukvalen.md:226](../chapters/00_vvedenie/00-04_kompyuter_bukvalen.md) | `Цена = 100` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/00_vvedenie/00-04_kompyuter_bukvalen.md:246](../chapters/00_vvedenie/00-04_kompyuter_bukvalen.md) | `Цена = 200` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/00_vvedenie/00-04_kompyuter_bukvalen.md:266](../chapters/00_vvedenie/00-04_kompyuter_bukvalen.md) | `Цена1 = 100` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-01_peremennye.md:17](../chapters/01_leksika/01-01_peremennye.md) | `Цена = 250` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-01_peremennye.md:33](../chapters/01_leksika/01-01_peremennye.md) | `Сумма = 250 * 4` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-01_peremennye.md:81](../chapters/01_leksika/01-01_peremennye.md) | `Цена = 250` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-01_peremennye.md:142](../chapters/01_leksika/01-01_peremennye.md) | `Цена = 250` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-01_peremennye.md:212](../chapters/01_leksika/01-01_peremennye.md) | `ЦенаЗаШтуку = 45` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-01_peremennye.md:270](../chapters/01_leksika/01-01_peremennye.md) | `А = 100` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-01_peremennye.md:309](../chapters/01_leksika/01-01_peremennye.md) | `СтавкаЗаЧас = 500` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-01_peremennye.md:329](../chapters/01_leksika/01-01_peremennye.md) | `Цена = 200` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-01_peremennye.md:382](../chapters/01_leksika/01-01_peremennye.md) | `ЦенаТетради = 35` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-02_vyrazheniya_i_operatory.md:87](../chapters/01_leksika/01-02_vyrazheniya_i_operatory.md) | `Сумма = 100 + 50 * 2` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-02_vyrazheniya_i_operatory.md:129](../chapters/01_leksika/01-02_vyrazheniya_i_operatory.md) | `Сумма = (100 + 50) * 2` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-02_vyrazheniya_i_operatory.md:181](../chapters/01_leksika/01-02_vyrazheniya_i_operatory.md) | `Имя = "Иван"` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-02_vyrazheniya_i_operatory.md:225](../chapters/01_leksika/01-02_vyrazheniya_i_operatory.md) | `ЦенаЗаШтуку = 35` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-02_vyrazheniya_i_operatory.md:304](../chapters/01_leksika/01-02_vyrazheniya_i_operatory.md) | `А = 10` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-03_komanda_soobschit.md:15](../chapters/01_leksika/01-03_komanda_soobschit.md) | `ЦенаЗаШтуку = 35` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-03_komanda_soobschit.md:65](../chapters/01_leksika/01-03_komanda_soobschit.md) | `Сообщить("Привет!")` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-03_komanda_soobschit.md:132](../chapters/01_leksika/01-03_komanda_soobschit.md) | `Сообщить("Здравствуйте!")` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-03_komanda_soobschit.md:158](../chapters/01_leksika/01-03_komanda_soobschit.md) | `А = 10` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-03_komanda_soobschit.md:240](../chapters/01_leksika/01-03_komanda_soobschit.md) | `ЦенаЗаШтуку = 35` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-03_komanda_soobschit.md:310](../chapters/01_leksika/01-03_komanda_soobschit.md) | `Сообщить("Раз")` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-03_komanda_soobschit.md:326](../chapters/01_leksika/01-03_komanda_soobschit.md) | `Сообщить("Раз" + " " + "Два" + " " + "Три")` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-03_komanda_soobschit.md:340](../chapters/01_leksika/01-03_komanda_soobschit.md) | `А = 5` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-03_komanda_soobschit.md:388](../chapters/01_leksika/01-03_komanda_soobschit.md) | `Имя = "Иван"` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-03_komanda_soobschit.md:464](../chapters/01_leksika/01-03_komanda_soobschit.md) | `ЦенаРучки = 25` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-04_komanda_esli.md:27](../chapters/01_leksika/01-04_komanda_esli.md) | `Найден = Истина` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-04_komanda_esli.md:123](../chapters/01_leksika/01-04_komanda_esli.md) | `Цена = 1500` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-04_komanda_esli.md:292](../chapters/01_leksika/01-04_komanda_esli.md) | `СтоимостьПокупки = 3500` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-04_komanda_esli.md:497](../chapters/01_leksika/01-04_komanda_esli.md) | `СтоимостьПокупки = 200 * 35;        // 7000` | исполняется |
| [chapters/01_leksika/01-05_chtenie_koda.md:31](../chapters/01_leksika/01-05_chtenie_koda.md) | `Цена = 250` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-05_chtenie_koda.md:108](../chapters/01_leksika/01-05_chtenie_koda.md) | `ЦенаЗаШтуку = 35` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-05_chtenie_koda.md:226](../chapters/01_leksika/01-05_chtenie_koda.md) | `Скидка = 10  // постоянным клиентам — десять процентов` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-05_chtenie_koda.md:262](../chapters/01_leksika/01-05_chtenie_koda.md) | `ПроцентСкидки = 0  // По правилам — никаких скидок на акцион` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-05_chtenie_koda.md:276](../chapters/01_leksika/01-05_chtenie_koda.md) | `ПроцентСкидки = 0  // Присваиваем ПроцентСкидки значение 0` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-05_chtenie_koda.md:294](../chapters/01_leksika/01-05_chtenie_koda.md) | `// Расчёт стоимости покупки с учётом скидки постоянного клие` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-05_chtenie_koda.md:382](../chapters/01_leksika/01-05_chtenie_koda.md) | `Сумма = 500` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-05_chtenie_koda.md:427](../chapters/01_leksika/01-05_chtenie_koda.md) | `// Цикл с присваиванием значения переменной А` | исполняется |
| [chapters/01_leksika/01-05_chtenie_koda.md:456](../chapters/01_leksika/01-05_chtenie_koda.md) | `Имя = "Анна Петрова"` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-05_chtenie_koda.md:542](../chapters/01_leksika/01-05_chtenie_koda.md) | `А = 10;  // 10 — это магическое число из спецификации, см. д` | исполняется |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:17](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `Цена = 100` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:39](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `Цена = 100` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:79](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `Цена = 200` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:99](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `Цена = 200` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:299](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `СтоимостьПокупки = 3500` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:396](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `Цена = 250` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:467](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `Цена = 250` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:498](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `А = 5` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:522](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `Возраст = 25` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:548](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `ПроцентСкидки = 10;` | исполняется |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:556](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `Сумма = 1500` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:590](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `ОстатокРучек = 7` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/02_semantika/02-01_semantika.md:11](../chapters/02_semantika/02-01_semantika.md) | `А = 5` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/02_semantika/02-01_semantika.md:39](../chapters/02_semantika/02-01_semantika.md) | `Цена = 250` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/02_semantika/02-01_semantika.md:94](../chapters/02_semantika/02-01_semantika.md) | `Цена = 250` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/02_semantika/02-01_semantika.md:226](../chapters/02_semantika/02-01_semantika.md) | `Возраст = 25` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/02_semantika/02-01_semantika.md:256](../chapters/02_semantika/02-01_semantika.md) | `ЦенаЗаКилограмм = 150` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/02_semantika/02-01_semantika.md:282](../chapters/02_semantika/02-01_semantika.md) | `СтоимостьПокупки = 3500` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:15](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `Цена = 250;` | исполняется |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:39](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `Х = 250;        // сейчас Х — число` | исполняется |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:53](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `Цена = 250;` | исполняется |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:76](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `Имя = "Иван";` | исполняется |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:96](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `Имя = "Иван";` | исполняется |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:112](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `Найден = Истина;` | исполняется |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:129](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `ЭтоПервыйЗапуск = Истина;` | исполняется |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:231](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `ДатаРождения = '19850315';               // 15 марта 1985 го` | исполняется |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:252](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `ДатаНачала = '20250101';` | исполняется |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:260](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `ДатаНачала = '20250101';` | исполняется |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:385](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `// Данные о продаже` | исполняется |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:472](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `А = 5 + 3` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:599](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `ВозрастКлиента = 25;` | исполняется |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:611](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `// Данные о продаже` | исполняется — рядом лежит вариант с точками с запятой |
| [chapters/02_semantika/02-03_vypolnit_stroku.md:134](../chapters/02_semantika/02-03_vypolnit_stroku.md) | `А = 10;` | исполняется |
| [chapters/02_semantika/02-03_vypolnit_stroku.md:239](../chapters/02_semantika/02-03_vypolnit_stroku.md) | `// Расчёт стоимости с учётом скидок и наценки за самовывоз` | исполняется |
| [chapters/02_semantika/02-03_vypolnit_stroku.md:336](../chapters/02_semantika/02-03_vypolnit_stroku.md) | `А = 5;` | исполняется |
| [chapters/02_semantika/02-03_vypolnit_stroku.md:346](../chapters/02_semantika/02-03_vypolnit_stroku.md) | `Х = 100;` | исполняется |
| [chapters/02_semantika/02-03_vypolnit_stroku.md:370](../chapters/02_semantika/02-03_vypolnit_stroku.md) | `Возраст = 25;` | исполняется |
| [chapters/02_semantika/02-03_vypolnit_stroku.md:390](../chapters/02_semantika/02-03_vypolnit_stroku.md) | `СтоимостьПокупки = 6500;` | исполняется |
| [chapters/02_semantika/02-04_perevod.md:31](../chapters/02_semantika/02-04_perevod.md) | `СтоимостьПокупки = 4500;` | исполняется |
| [chapters/02_semantika/02-04_perevod.md:90](../chapters/02_semantika/02-04_perevod.md) | `СуммаПокупки = 1500;` | исполняется |
| [chapters/02_semantika/02-04_perevod.md:166](../chapters/02_semantika/02-04_perevod.md) | `// Расчёт скидки и итога` | исполняется |
| [chapters/02_semantika/02-04_perevod.md:259](../chapters/02_semantika/02-04_perevod.md) | `Возраст = 30;` | исполняется |
| [chapters/02_semantika/02-04_perevod.md:287](../chapters/02_semantika/02-04_perevod.md) | `Температура = -5;` | исполняется |
| [chapters/02_semantika/02-04_perevod.md:326](../chapters/02_semantika/02-04_perevod.md) | `НетПросроченныхКниг = Истина;` | исполняется |
| [chapters/02_semantika/02-04_perevod.md:369](../chapters/02_semantika/02-04_perevod.md) | `ШагиЗаДень = 12500;` | исполняется |
| [chapters/03_struktura/03-01_struktura_programmy.md:35](../chapters/03_struktura/03-01_struktura_programmy.md) | `А = 10;` | исполняется |
| [chapters/03_struktura/03-01_struktura_programmy.md:72](../chapters/03_struktura/03-01_struktura_programmy.md) | `ВозрастКлиента = 25;` | исполняется |
| [chapters/03_struktura/03-01_struktura_programmy.md:176](../chapters/03_struktura/03-01_struktura_programmy.md) | `// Данные клиента` | исполняется |
| [chapters/03_struktura/03-01_struktura_programmy.md:385](../chapters/03_struktura/03-01_struktura_programmy.md) | `ТипТовара = "тетрадь";` | исполняется |
| [chapters/03_struktura/03-02_tsikl_poka.md:19](../chapters/03_struktura/03-02_tsikl_poka.md) | `Сообщить(1);` | исполняется |
| [chapters/03_struktura/03-02_tsikl_poka.md:33](../chapters/03_struktura/03-02_tsikl_poka.md) | `Номер = 1;` | исполняется |
| [chapters/03_struktura/03-02_tsikl_poka.md:101](../chapters/03_struktura/03-02_tsikl_poka.md) | `Счётчик = 1;` | исполняется |
| [chapters/03_struktura/03-02_tsikl_poka.md:153](../chapters/03_struktura/03-02_tsikl_poka.md) | `Осталось = 5;` | исполняется |
| [chapters/03_struktura/03-02_tsikl_poka.md:164](../chapters/03_struktura/03-02_tsikl_poka.md) | `Число = 1;` | исполняется |
| [chapters/03_struktura/03-02_tsikl_poka.md:239](../chapters/03_struktura/03-02_tsikl_poka.md) | `Остаток = 100;  // рублей в кассе` | исполняется |
| [chapters/03_struktura/03-02_tsikl_poka.md:286](../chapters/03_struktura/03-02_tsikl_poka.md) | `ДневнаяНорма = 700;` | исполняется |
| [chapters/03_struktura/03-02_tsikl_poka.md:343](../chapters/03_struktura/03-02_tsikl_poka.md) | `Н = 10;` | исполняется |
| [chapters/03_struktura/03-02_tsikl_poka.md:391](../chapters/03_struktura/03-02_tsikl_poka.md) | `Х = 1;` | исполняется |
| [chapters/03_struktura/03-02_tsikl_poka.md:431](../chapters/03_struktura/03-02_tsikl_poka.md) | `КоличествоТоваров = 0;` | исполняется |
| [chapters/03_struktura/03-02_tsikl_poka.md:449](../chapters/03_struktura/03-02_tsikl_poka.md) | `N = 5;` | исполняется |
| [chapters/03_struktura/03-02_tsikl_poka.md:472](../chapters/03_struktura/03-02_tsikl_poka.md) | `Запас = 50;` | исполняется |
| [chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md:31](../chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md) | `Товары = Новый Массив;` | исполняется |
| [chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md:37](../chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md) | `Товары = Новый Массив;` | исполняется |
| [chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md:91](../chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md) | `Товары = Новый Массив;` | исполняется |
| [chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md:130](../chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md) | `Цены = Новый Массив;` | исполняется |
| [chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md:204](../chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md) | `Города = Новый Массив;` | исполняется |
| [chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md:221](../chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md) | `Цены = Новый Массив;` | исполняется |
| [chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md:243](../chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md) | `Товары = Новый Массив;` | исполняется |
| [chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md:256](../chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md) | `Товары = Новый Массив;` | исполняется |
| [chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md:287](../chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md) | `Цены = Новый Массив;` | исполняется |
| [chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md:324](../chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md) | `Цены = Новый Массив;` | исполняется |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:17](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `Сообщить("--------------------");` | исполняется |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:29](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `Процедура НапечататьРазделитель()` | исполняется |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:59](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `Процедура НапечататьШапкуЧека()` | исполняется |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:93](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `Функция РассчитатьСкидку(Сумма, ПроцентСкидки)` | исполняется |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:171](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `Процедура НапечататьРазделитель()` | исполняется |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:235](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `Функция ВычислитьНДС(Сумма, СтавкаНДС)` | исполняется |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:245](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `Процедура НапечататьПриветствие(Имя)` | исполняется |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:283](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `Функция НапечататьПриветствие(Имя)` | исполняется |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:293](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `Процедура НапечататьПриветствие(Имя)` | исполняется |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:307](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `Функция МаксимумДвух(А, Б)` | исполняется |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:328](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `Процедура НапечататьСтроку(Товар, Цена)` | исполняется |
| [chapters/03_struktura/03-05_parametry_podrobno.md:34](../chapters/03_struktura/03-05_parametry_podrobno.md) | `Процедура УвеличитьНаДесять(Число)` | исполняется |
| [chapters/03_struktura/03-05_parametry_podrobno.md:58](../chapters/03_struktura/03-05_parametry_podrobno.md) | `Процедура УвеличитьНаДесять(Знач Число)` | исполняется |
| [chapters/03_struktura/03-05_parametry_podrobno.md:142](../chapters/03_struktura/03-05_parametry_podrobno.md) | `Функция Сложить(А, Б = 0)` | исполняется |
| [chapters/03_struktura/03-05_parametry_podrobno.md:223](../chapters/03_struktura/03-05_parametry_podrobno.md) | `Процедура Удвоить(Число)` | исполняется |
| [chapters/03_struktura/03-05_parametry_podrobno.md:237](../chapters/03_struktura/03-05_parametry_podrobno.md) | `Процедура Удвоить(Знач Число)` | исполняется |
| [chapters/03_struktura/03-05_parametry_podrobno.md:251](../chapters/03_struktura/03-05_parametry_podrobno.md) | `Скидка = 10;` | исполняется |
| [chapters/03_struktura/03-05_parametry_podrobno.md:303](../chapters/03_struktura/03-05_parametry_podrobno.md) | `Функция ДобавитьНалог(Знач Цена, Знач ПроцентНалога)` | исполняется |
| [chapters/03_struktura/03-06_blok_shemy.md:165](../chapters/03_struktura/03-06_blok_shemy.md) | `Процедура НапечататьСтрокуЧека(Товар, Цена)` | исполняется |
| [chapters/03_struktura/03-06_blok_shemy.md:258](../chapters/03_struktura/03-06_blok_shemy.md) | `Счётчик = 1;` | исполняется |
| [chapters/03_struktura/03-07_progonka.md:35](../chapters/03_struktura/03-07_progonka.md) | `Сумма = 0;` | исполняется |
| [chapters/03_struktura/03-07_progonka.md:73](../chapters/03_struktura/03-07_progonka.md) | `Цена = 400;` | исполняется |
| [chapters/03_struktura/03-07_progonka.md:100](../chapters/03_struktura/03-07_progonka.md) | `Функция МаксимумДвух(А, Б)` | исполняется |
| [chapters/03_struktura/03-07_progonka.md:130](../chapters/03_struktura/03-07_progonka.md) | `Функция МаксимумДвух(А, Б)` | исполняется |
| [chapters/03_struktura/03-07_progonka.md:170](../chapters/03_struktura/03-07_progonka.md) | `Товары = Новый Массив;` | исполняется |
| [chapters/03_struktura/03-07_progonka.md:221](../chapters/03_struktura/03-07_progonka.md) | `Н = 1;` | исполняется |
| [chapters/03_struktura/03-07_progonka.md:237](../chapters/03_struktura/03-07_progonka.md) | `Функция СуммаДвух(А, Б)` | исполняется |
| [chapters/03_struktura/03-07_progonka.md:252](../chapters/03_struktura/03-07_progonka.md) | `Цены = Новый Массив;` | исполняется |
| [chapters/03_struktura/03-07_progonka.md:309](../chapters/03_struktura/03-07_progonka.md) | `Функция СуммаДвух(А, Б)` | исполняется |
| [chapters/03_struktura/03-07_progonka.md:369](../chapters/03_struktura/03-07_progonka.md) | `Н = 2;` | исполняется |
| [chapters/04_patterny/04-02_poisk_elementa.md:74](../chapters/04_patterny/04-02_poisk_elementa.md) | `НайденноеИмя = Неопределено;` | исполняется |
| [chapters/04_patterny/04-02_poisk_elementa.md:93](../chapters/04_patterny/04-02_poisk_elementa.md) | `Товары = Новый Массив;` | исполняется |
| [chapters/04_patterny/04-02_poisk_elementa.md:183](../chapters/04_patterny/04-02_poisk_elementa.md) | `ДоступныеТовары = Новый Массив;` | исполняется |
| [chapters/04_patterny/04-02_poisk_elementa.md:316](../chapters/04_patterny/04-02_poisk_elementa.md) | `Товары = Новый Массив;` | исполняется |
| [chapters/04_patterny/04-03_perebor_i_obrabotka.md:149](../chapters/04_patterny/04-03_perebor_i_obrabotka.md) | `Товары = Новый Массив;` | исполняется |
| [chapters/04_patterny/04-03_perebor_i_obrabotka.md:250](../chapters/04_patterny/04-03_perebor_i_obrabotka.md) | `Цены = Новый Массив;` | исполняется |
| [chapters/04_patterny/04-03_perebor_i_obrabotka.md:276](../chapters/04_patterny/04-03_perebor_i_obrabotka.md) | `Цены = Новый Массив;` | исполняется |
| [chapters/04_patterny/04-04_agregaciya.md:185](../chapters/04_patterny/04-04_agregaciya.md) | `Цены = Новый Массив;` | исполняется |
| [chapters/04_patterny/04-04_agregaciya.md:281](../chapters/04_patterny/04-04_agregaciya.md) | `Цены = Новый Массив;` | исполняется |
| [chapters/04_patterny/04-04_agregaciya.md:330](../chapters/04_patterny/04-04_agregaciya.md) | `Цены = Новый Массив;` | исполняется |
| [chapters/04_patterny/04-05_zashchitny_kod.md:43](../chapters/04_patterny/04-05_zashchitny_kod.md) | `Функция НайтиМаксимум(Цены)` | исполняется |
| [chapters/04_patterny/04-05_zashchitny_kod.md:164](../chapters/04_patterny/04-05_zashchitny_kod.md) | `Цены = Новый Массив;` | исполняется |
| [chapters/04_patterny/04-05_zashchitny_kod.md:218](../chapters/04_patterny/04-05_zashchitny_kod.md) | `Функция СреднееЗначение(Числа)` | исполняется |
| [chapters/04_patterny/04-05_zashchitny_kod.md:250](../chapters/04_patterny/04-05_zashchitny_kod.md) | `Функция ПоказатьМаксимум(Цены)` | исполняется |
| [chapters/04_patterny/04-05_zashchitny_kod.md:276](../chapters/04_patterny/04-05_zashchitny_kod.md) | `Функция СреднееЗначение(Числа)` | исполняется |
| [chapters/04_patterny/04-05_zashchitny_kod.md:315](../chapters/04_patterny/04-05_zashchitny_kod.md) | `Процедура ПоказатьМаксимум(Цены)` | исполняется |
| [chapters/04_patterny/04-06_raspoznavanie.md:136](../chapters/04_patterny/04-06_raspoznavanie.md) | `Товары = Новый Массив;` | исполняется |
| [chapters/04_patterny/04-06_raspoznavanie.md:242](../chapters/04_patterny/04-06_raspoznavanie.md) | `ЦеныПоставщика = Новый Массив;` | исполняется |
| [chapters/04_patterny/04-06_raspoznavanie.md:311](../chapters/04_patterny/04-06_raspoznavanie.md) | `Функция НайтиСамоеДлинноеСлово(Слова)` | исполняется |
| [chapters/05_idiomy/05-01_obekty_svoystva_metody.md:104](../chapters/05_idiomy/05-01_obekty_svoystva_metody.md) | `Товары = Новый Массив;` | исполняется |
| [chapters/05_idiomy/05-01_obekty_svoystva_metody.md:120](../chapters/05_idiomy/05-01_obekty_svoystva_metody.md) | `Цены = Новый Массив;          // создать новый объект типа «` | исполняется |
| [chapters/05_idiomy/05-01_obekty_svoystva_metody.md:207](../chapters/05_idiomy/05-01_obekty_svoystva_metody.md) | `Список = Новый СписокЗначений;` | исполняется |
| [chapters/05_idiomy/05-01_obekty_svoystva_metody.md:241](../chapters/05_idiomy/05-01_obekty_svoystva_metody.md) | `Список = Новый СписокЗначений;  // создание объекта` | исполняется |
| [chapters/05_idiomy/05-01_obekty_svoystva_metody.md:276](../chapters/05_idiomy/05-01_obekty_svoystva_metody.md) | `Товары = Новый Массив;` | исполняется |
| [chapters/05_idiomy/05-05_tipichnye_oboroty.md:29](../chapters/05_idiomy/05-05_tipichnye_oboroty.md) | `Процедура ОбработатьТовар(ТоварСсылка)` | исполняется |
| [chapters/05_idiomy/05-05_tipichnye_oboroty.md:136](../chapters/05_idiomy/05-05_tipichnye_oboroty.md) | `Товары = Новый Массив;` | исполняется |
| [chapters/05_idiomy/05-05_tipichnye_oboroty.md:283](../chapters/05_idiomy/05-05_tipichnye_oboroty.md) | `Товары = Новый Массив;` | исполняется |
| [chapters/05_idiomy/05-06_pervoe_chtenie.md:30](../chapters/05_idiomy/05-06_pervoe_chtenie.md) | `Процедура ПроверитьНаличиеТовара(НаименованиеТовара)` | исполняется |
| [chapters/05_idiomy/05-06_pervoe_chtenie.md:53](../chapters/05_idiomy/05-06_pervoe_chtenie.md) | `Функция РассчитатьИтогДокумента(ДокументСсылка)` | исполняется |
| [chapters/05_idiomy/05-06_pervoe_chtenie.md:89](../chapters/05_idiomy/05-06_pervoe_chtenie.md) | `Процедура СформироватьОтчётПоПродажам(ДатаНачала, ДатаОконча` | исполняется |
| [chapters/05_idiomy/05-06_pervoe_chtenie.md:160](../chapters/05_idiomy/05-06_pervoe_chtenie.md) | `Процедура ОбновитьЦеныПоставщика(ПоставщикСсылка, НовыйПроце` | исполняется |
| [chapters/05_idiomy/05-06_pervoe_chtenie.md:186](../chapters/05_idiomy/05-06_pervoe_chtenie.md) | `Функция ПолучитьИНН(КонтрагентСсылка)` | исполняется |
| [chapters/05_idiomy/05-06_pervoe_chtenie.md:224](../chapters/05_idiomy/05-06_pervoe_chtenie.md) | `Функция ПолучитьИНН(КонтрагентСсылка)` | исполняется |
| [chapters/05_idiomy/05-06_pervoe_chtenie.md:239](../chapters/05_idiomy/05-06_pervoe_chtenie.md) | `Процедура ВывестиТоварыДешевле(ПорогЦены)` | исполняется |
| [chapters/06_kontekst/06-01_gde_zhivyot_kod.md:55](../chapters/06_kontekst/06-01_gde_zhivyot_kod.md) | `// Это обработчик события нажатия кнопки «Рассчитать» на фор` | исполняется |
| [chapters/06_kontekst/06-01_gde_zhivyot_kod.md:89](../chapters/06_kontekst/06-01_gde_zhivyot_kod.md) | `Процедура ВывестиДешёвыеТовары(ПорогЦены)` | исполняется |
| [chapters/06_kontekst/06-01_gde_zhivyot_kod.md:141](../chapters/06_kontekst/06-01_gde_zhivyot_kod.md) | `Процедура ПередЗаписью(Отказ)` | исполняется |
| [chapters/06_kontekst/06-01_gde_zhivyot_kod.md:195](../chapters/06_kontekst/06-01_gde_zhivyot_kod.md) | `Процедура ТоварыКоличествоПриИзменении(Элемент)` | исполняется |
| [chapters/07_kachestvo/07-01_chto_takoe_khoroshiy_kod.md:123](../chapters/07_kachestvo/07-01_chto_takoe_khoroshiy_kod.md) | `Процедура ОбновитьЦены()` | исполняется |
| [chapters/07_kachestvo/07-01_chto_takoe_khoroshiy_kod.md:165](../chapters/07_kachestvo/07-01_chto_takoe_khoroshiy_kod.md) | `Процедура Уд(Список)` | исполняется |
| [chapters/07_kachestvo/07-01_chto_takoe_khoroshiy_kod.md:206](../chapters/07_kachestvo/07-01_chto_takoe_khoroshiy_kod.md) | `// Пометить на удаление все переданные элементы справочника` | исполняется |
| [chapters/07_kachestvo/07-02_obrabotka_oshibok.md:28](../chapters/07_kachestvo/07-02_obrabotka_oshibok.md) | `Попытка` | исполняется |
| [chapters/07_kachestvo/07-02_obrabotka_oshibok.md:48](../chapters/07_kachestvo/07-02_obrabotka_oshibok.md) | `Попытка` | исполняется |
| [chapters/07_kachestvo/07-02_obrabotka_oshibok.md:113](../chapters/07_kachestvo/07-02_obrabotka_oshibok.md) | `// Плохо: ошибка скрывается, код продолжается молча` | исполняется |
| [chapters/07_kachestvo/07-02_obrabotka_oshibok.md:133](../chapters/07_kachestvo/07-02_obrabotka_oshibok.md) | `Процедура ПровестиПоступление(НомерДокумента)` | исполняется |
| [chapters/07_kachestvo/07-02_obrabotka_oshibok.md:145](../chapters/07_kachestvo/07-02_obrabotka_oshibok.md) | `Процедура ПровестиПоступление(НомерДокумента)` | исполняется |
| [chapters/07_kachestvo/07-02_obrabotka_oshibok.md:206](../chapters/07_kachestvo/07-02_obrabotka_oshibok.md) | `Попытка` | исполняется |
| [chapters/07_kachestvo/07-02_obrabotka_oshibok.md:269](../chapters/07_kachestvo/07-02_obrabotka_oshibok.md) | `Процедура СоздатьТовар(Наименование, Артикул)` | исполняется |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:92](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `Процедура ПередЗаписью(Отказ)` | исполняется |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:117](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `Процедура ОбработатьДокумент(Ссылка)` | исполняется |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:137](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `Процедура ОбработатьДокумент(Ссылка)` | исполняется |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:170](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `// Бесполезное сообщение` | исполняется |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:186](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `Процедура ОбработатьПоступление(НомерДокумента, СкладСсылка)` | исполняется |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:254](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `Процедура НачислитьСкидку(КонтрагентСсылка, СуммаЗаказа)` | исполняется |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:277](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `Процедура ПередЗаписью(Отказ)` | исполняется |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:308](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `Процедура НачислитьСкидку(КонтрагентСсылка, СуммаЗаказа)` | исполняется |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:334](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `Процедура ПередЗаписью(Отказ)` | исполняется |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:354](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `// Было:` | исполняется |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:366](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `Процедура ПересчитатьЦены(СписокНоменклатуры, КоэффициентПер` | исполняется |
| [chapters/07_kachestvo/07-05_chitaemost.md:17](../chapters/07_kachestvo/07-05_chitaemost.md) | `// Плохо: непонятно, что хранит` | исполняется |
| [chapters/07_kachestvo/07-05_chitaemost.md:103](../chapters/07_kachestvo/07-05_chitaemost.md) | `// Плохо: одна большая процедура` | исполняется |
| [chapters/07_kachestvo/07-05_chitaemost.md:157](../chapters/07_kachestvo/07-05_chitaemost.md) | `Процедура П(Д)` | исполняется |
| [chapters/07_kachestvo/07-05_chitaemost.md:172](../chapters/07_kachestvo/07-05_chitaemost.md) | `// Подсчитать суммарный объём проведённых поступлений за ука` | исполняется |
| [chapters/07_kachestvo/07-05_chitaemost.md:252](../chapters/07_kachestvo/07-05_chitaemost.md) | `Процедура ОбработкаЗаказа(ЗаказСсылка)` | исполняется |
| [chapters/07_kachestvo/07-05_chitaemost.md:321](../chapters/07_kachestvo/07-05_chitaemost.md) | `Функция ЗаказЯвляетсяКорректным(ЗаказСсылка)` | исполняется |
| [chapters/07_kachestvo/07-06_kriticheskoe_chtenie.md:53](../chapters/07_kachestvo/07-06_kriticheskoe_chtenie.md) | `Процедура О(Д, К)` | исполняется |
| [chapters/07_kachestvo/07-06_kriticheskoe_chtenie.md:91](../chapters/07_kachestvo/07-06_kriticheskoe_chtenie.md) | `// Суммарный объём реализации контрагенту по документам, пре` | исполняется |
| [chapters/07_kachestvo/07-06_kriticheskoe_chtenie.md:168](../chapters/07_kachestvo/07-06_kriticheskoe_chtenie.md) | `Процедура УП(Н, П)` | исполняется |
| [chapters/07_kachestvo/07-06_kriticheskoe_chtenie.md:189](../chapters/07_kachestvo/07-06_kriticheskoe_chtenie.md) | `Процедура ПроверитьОстатки()` | исполняется |
| [chapters/07_kachestvo/07-06_kriticheskoe_chtenie.md:228](../chapters/07_kachestvo/07-06_kriticheskoe_chtenie.md) | `Процедура УстановитьЦенуТовара(НаименованиеТовара, НоваяЦена` | исполняется |
| [chapters/07_kachestvo/07-06_kriticheskoe_chtenie.md:273](../chapters/07_kachestvo/07-06_kriticheskoe_chtenie.md) | `Процедура ВывестиКрупныеРеализацииЗаМесяц(ПорогСуммы)` | исполняется |
| [chapters/08_sistema/08-01_put_dannykh.md:42](../chapters/08_sistema/08-01_put_dannykh.md) | `Процедура ОбработкаПроведения(Отказ, РежимПроведения)` | исполняется |
| [chapters/08_sistema/08-01_put_dannykh.md:77](../chapters/08_sistema/08-01_put_dannykh.md) | `Процедура ОбработкаПроведения(Отказ, РежимПроведения)` | исполняется |
| [chapters/08_sistema/08-01_put_dannykh.md:135](../chapters/08_sistema/08-01_put_dannykh.md) | `Процедура ОбработкаПроведения(Отказ, РежимПроведения)` | исполняется |
| [chapters/08_sistema/08-01_put_dannykh.md:173](../chapters/08_sistema/08-01_put_dannykh.md) | `Процедура ОбработкаПроведения(Отказ, РежимПроведения)` | исполняется |
| [chapters/08_sistema/08-01_put_dannykh.md:194](../chapters/08_sistema/08-01_put_dannykh.md) | `Процедура ОбработкаПроведения(Отказ, РежимПроведения)` | исполняется |

## `набросок` — 210

| Где | Первая строка | Почему |
|---|---|---|
| [chapters/00_vvedenie/00-02_ot_dannyh_k_informacii.md:197](../chapters/00_vvedenie/00-02_ot_dannyh_k_informacii.md) | `- ставка работника (число)` | parser: Неожиданный токен «-» |
| [chapters/00_vvedenie/00-04_kompyuter_bukvalen.md:65](../chapters/00_vvedenie/00-04_kompyuter_bukvalen.md) | `Сумма = Цена * Количество` | parser: Ожидалось «;», получено «Цена» |
| [chapters/00_vvedenie/00-04_kompyuter_bukvalen.md:115](../chapters/00_vvedenie/00-04_kompyuter_bukvalen.md) | `Цена = 250` | parser: Ожидалось «;», получено «Сообщит» |
| [chapters/00_vvedenie/00-04_kompyuter_bukvalen.md:336](../chapters/00_vvedenie/00-04_kompyuter_bukvalen.md) | `Среднее = (Цена1 + Цена2 + Цена3) / 3` | parser: Ожидалось «;», получено «eof» |
| [chapters/00_vvedenie/00-05_gde_zdes_1s.md:25](../chapters/00_vvedenie/00-05_gde_zdes_1s.md) | `Платформа 1С  =  «1С: Предприятие 8.3»` | lexer: Неизвестный символ ««» |
| [chapters/00_vvedenie/00-05_gde_zdes_1s.md:144](../chapters/00_vvedenie/00-05_gde_zdes_1s.md) | `Отчёт «Остатки на складе»          (сколько чего сейчас лежи` | lexer: Неизвестный символ ««» |
| [chapters/01_leksika/01-02_vyrazheniya_i_operatory.md:9](../chapters/01_leksika/01-02_vyrazheniya_i_operatory.md) | `Цена = 250` | parser: Ожидалось «;», получено «Сумма» |
| [chapters/01_leksika/01-02_vyrazheniya_i_operatory.md:47](../chapters/01_leksika/01-02_vyrazheniya_i_operatory.md) | `Сумма = 1000` | parser: Ожидалось «;», получено «Сумма» |
| [chapters/01_leksika/01-02_vyrazheniya_i_operatory.md:64](../chapters/01_leksika/01-02_vyrazheniya_i_operatory.md) | `+    сложение         Сумма = Цена + Налог` | parser: Неожиданный токен «+» |
| [chapters/01_leksika/01-02_vyrazheniya_i_operatory.md:206](../chapters/01_leksika/01-02_vyrazheniya_i_operatory.md) | `Сообщить("Сумма покупки: " + Сумма)` | parser: Ожидалось «;», получено «eof» |
| [chapters/01_leksika/01-02_vyrazheniya_i_operatory.md:289](../chapters/01_leksika/01-02_vyrazheniya_i_operatory.md) | `а)  10 + 5 * 2` | parser: Ожидалось «;», получено «)» |
| [chapters/01_leksika/01-02_vyrazheniya_i_operatory.md:324](../chapters/01_leksika/01-02_vyrazheniya_i_operatory.md) | `а)  Результат = "Цена: " + 100` | parser: Ожидалось «;», получено «)» |
| [chapters/01_leksika/01-02_vyrazheniya_i_operatory.md:344](../chapters/01_leksika/01-02_vyrazheniya_i_operatory.md) | `Среднее = (А + Б + В + Г) / 4` | parser: Ожидалось «;», получено «eof» |
| [chapters/01_leksika/01-02_vyrazheniya_i_operatory.md:358](../chapters/01_leksika/01-02_vyrazheniya_i_operatory.md) | `а)  10 + 5 * 2 = 10 + 10 = 20` | parser: Ожидалось «;», получено «)» |
| [chapters/01_leksika/01-02_vyrazheniya_i_operatory.md:403](../chapters/01_leksika/01-02_vyrazheniya_i_operatory.md) | `ЦенаЗаШтуку = 18` | parser: Ожидалось «;», получено «Количество» |
| [chapters/01_leksika/01-03_komanda_soobschit.md:216](../chapters/01_leksika/01-03_komanda_soobschit.md) | `Сообщить(ТекстСообщения, СтатусСообщения)` | parser: Ожидалось «;», получено «eof» |
| [chapters/01_leksika/01-03_komanda_soobschit.md:364](../chapters/01_leksika/01-03_komanda_soobschit.md) | `а)  Сообщить("Привет")` | parser: Ожидалось «;», получено «)» |
| [chapters/01_leksika/01-03_komanda_soobschit.md:508](../chapters/01_leksika/01-03_komanda_soobschit.md) | `Имя + ", тебе " + ВозрастВГодах + " лет, осталось до 30 — " ` | parser: Ожидалось «;», получено «+» |
| [chapters/01_leksika/01-03_komanda_soobschit.md:522](../chapters/01_leksika/01-03_komanda_soobschit.md) | `Сообщить(Имя + ", тебе " + ВозрастВГодах + " лет, осталось д` | parser: Ожидалось «;», получено «eof» |
| [chapters/01_leksika/01-04_komanda_esli.md:74](../chapters/01_leksika/01-04_komanda_esli.md) | `ДорогойТовар = (Цена > 1000)` | parser: Ожидалось «;», получено «Сообщить» |
| [chapters/01_leksika/01-04_komanda_esli.md:217](../chapters/01_leksika/01-04_komanda_esli.md) | `Если Цена > 1000 Тогда` | чистый язык, не хватает контекста |
| [chapters/01_leksika/01-04_komanda_esli.md:259](../chapters/01_leksika/01-04_komanda_esli.md) | `Если Цена > 5000 Тогда` | чистый язык, не хватает контекста |
| [chapters/01_leksika/01-04_komanda_esli.md:386](../chapters/01_leksika/01-04_komanda_esli.md) | `Если Возраст < 7 Тогда` | чистый язык, не хватает контекста |
| [chapters/01_leksika/01-04_komanda_esli.md:400](../chapters/01_leksika/01-04_komanda_esli.md) | `а)  Если Цена > 1000 Сообщить("Дорого"); КонецЕсли;` | parser: Ожидалось «;», получено «)» |
| [chapters/01_leksika/01-05_chtenie_koda.md:50](../chapters/01_leksika/01-05_chtenie_koda.md) | `Если Цена = 250 Тогда` | parser: Ожидалось «КонецЕсли», получено «eof» |
| [chapters/01_leksika/01-05_chtenie_koda.md:58](../chapters/01_leksika/01-05_chtenie_koda.md) | `Сумма = Цена * Количество - Скидка` | parser: Ожидалось «;», получено «eof» |
| [chapters/01_leksika/01-05_chtenie_koda.md:66](../chapters/01_leksika/01-05_chtenie_koda.md) | `Сообщить("Итого: " + Сумма)` | parser: Ожидалось «;», получено «eof» |
| [chapters/01_leksika/01-05_chtenie_koda.md:74](../chapters/01_leksika/01-05_chtenie_koda.md) | `Если Цена > 1000 Тогда` | чистый язык, не хватает контекста |
| [chapters/01_leksika/01-05_chtenie_koda.md:146](../chapters/01_leksika/01-05_chtenie_koda.md) | `Если СтоимостьПокупки >= 10000 Тогда` | чистый язык, не хватает контекста |
| [chapters/01_leksika/01-05_chtenie_koda.md:240](../chapters/01_leksika/01-05_chtenie_koda.md) | `// Здесь начинается расчёт скидки` | parser: Ожидалось «;», получено «ИначеЕсли» |
| [chapters/01_leksika/01-05_chtenie_koda.md:439](../chapters/01_leksika/01-05_chtenie_koda.md) | `Скидка = 0` | parser: Ожидалось «;», получено «Если» |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:119](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `ЦенаЗаЛитр = 80` | parser: Ожидалось «;», получено «ОбъёмВЛитрах» |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:148](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `А = 10` | parser: Ожидалось «;», получено «Б» |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:166](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `А = 10` | parser: Ожидалось «;», получено «Б» |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:185](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `Цена = 1500` | parser: Ожидалось «;», получено «ПроцентСкидки» |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:198](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `Если Цена >= 1000 Тогда` | чистый язык, не хватает контекста |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:210](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `Если Возраст < 18 Тогда` | parser: Ожидалось «;», получено «eof» |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:222](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `Если Возраст < 18 Тогда` | чистый язык, не хватает контекста |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:268](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `СтоимостьПокупки = 3500` | parser: Ожидалось «;», получено «ПостоянныйКлиент» |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:414](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `А = 5` | parser: Ожидалось «;», получено «Б» |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:425](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `Возраст = 25` | parser: Ожидалось «;», получено «Если» |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:436](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `Сумма = 1500` | parser: Ожидалось «;», получено «ПроцентСкидки» |
| [chapters/01_leksika/01-06_vosstanovlenie_koda.md:450](../chapters/01_leksika/01-06_vosstanovlenie_koda.md) | `ОстатокРучек = 7` | parser: Ожидалось «;», получено «ОстатокКарандашей» |
| [chapters/02_semantika/02-01_semantika.md:376](../chapters/02_semantika/02-01_semantika.md) | `Скидка = Стоимость * ПроцентСкидки / 100` | parser: Ожидалось «;», получено «eof» |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:87](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `А = 5         (число)` | parser: Ожидалось «;», получено «(» |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:169](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `// Скидка действует только в выходные постоянным клиентам` | чистый язык, не хватает контекста |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:208](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `Если (Цена > 1000) И (Количество < 5) Тогда` | parser: Ожидалось «КонецЕсли», получено «eof» |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:216](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `А ИЛИ Б И В         // Сначала Б И В, потом ИЛИ` | parser: Ожидалось «;», получено «ИЛИ» |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:457](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `а)  100` | parser: Ожидалось «;», получено «)» |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:508](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `а)  100 + 50` | parser: Ожидалось «;», получено «)» |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:522](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `ВозрастКлиента = "25"` | parser: Ожидалось «;», получено «Если» |
| [chapters/02_semantika/02-03_vypolnit_stroku.md:17](../chapters/02_semantika/02-03_vypolnit_stroku.md) | `Сумма = Цена * Количество;` | чистый язык, не хватает контекста |
| [chapters/02_semantika/02-03_vypolnit_stroku.md:58](../chapters/02_semantika/02-03_vypolnit_stroku.md) | `А = А + 1;` | чистый язык, не хватает контекста |
| [chapters/02_semantika/02-03_vypolnit_stroku.md:87](../chapters/02_semantika/02-03_vypolnit_stroku.md) | `Итог = Цена * Количество - Скидка + Налог;` | чистый язык, не хватает контекста |
| [chapters/03_struktura/03-01_struktura_programmy.md:52](../chapters/03_struktura/03-01_struktura_programmy.md) | `Если ВозрастКлиента >= 18 Тогда` | чистый язык, не хватает контекста |
| [chapters/03_struktura/03-01_struktura_programmy.md:101](../chapters/03_struktura/03-01_struktura_programmy.md) | `Если А > 0 Тогда` | чистый язык, не хватает контекста |
| [chapters/03_struktura/03-01_struktura_programmy.md:117](../chapters/03_struktura/03-01_struktura_programmy.md) | `Если А > 0 И Б > 0 И В > 0 И Г > 0 Тогда` | чистый язык, не хватает контекста |
| [chapters/03_struktura/03-01_struktura_programmy.md:131](../chapters/03_struktura/03-01_struktura_programmy.md) | `Если ВозрастКлиента >= 18 И НаличиеПаспорта Тогда` | parser: Неожиданный токен «.» |
| [chapters/03_struktura/03-01_struktura_programmy.md:157](../chapters/03_struktura/03-01_struktura_programmy.md) | `КлиентДопущен = ВозрастКлиента >= 18 ` | parser: Неожиданный токен «.» |
| [chapters/03_struktura/03-01_struktura_programmy.md:268](../chapters/03_struktura/03-01_struktura_programmy.md) | `Если А > 0 Тогда` | чистый язык, не хватает контекста |
| [chapters/03_struktura/03-01_struktura_programmy.md:284](../chapters/03_struktura/03-01_struktura_programmy.md) | `Если НЕ ЗакрытоНаУчёт И ЕстьВНаличии ИЛИ ЭтоПодЗаказ Тогда` | чистый язык, не хватает контекста |
| [chapters/03_struktura/03-01_struktura_programmy.md:298](../chapters/03_struktura/03-01_struktura_programmy.md) | `Если ВозрастКлиента >= 18 И НаличиеПаспорта И НетПросроченны` | чистый язык, не хватает контекста |
| [chapters/03_struktura/03-01_struktura_programmy.md:324](../chapters/03_struktura/03-01_struktura_programmy.md) | `Если А > 0 И Б > 0 Тогда` | чистый язык, не хватает контекста |
| [chapters/03_struktura/03-01_struktura_programmy.md:346](../chapters/03_struktura/03-01_struktura_programmy.md) | `Если (НЕ ЗакрытоНаУчёт И ЕстьВНаличии) ИЛИ ЭтоПодЗаказ Тогда` | чистый язык, не хватает контекста |
| [chapters/03_struktura/03-01_struktura_programmy.md:366](../chapters/03_struktura/03-01_struktura_programmy.md) | `КлиентДопущен = ВозрастКлиента >= 18 ` | чистый язык, не хватает контекста |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:68](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `НапечататьШапкуЧека();` | чистый язык, не хватает контекста |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:102](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `ИтогоСкидка = РассчитатьСкидку(3500, 15);` | чистый язык, не хватает контекста |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:117](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `Функция РассчитатьСкидку(Сумма, ПроцентСкидки)` | parser: Неожиданный токен «.» |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:144](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `Встроенные               Пользовательские` | lexer: Неизвестный символ «─» |
| [chapters/03_struktura/03-05_parametry_podrobno.md:70](../chapters/03_struktura/03-05_parametry_podrobno.md) | `Без Знач (по ссылке)          С Знач (по значению)` | lexer: Неизвестный символ «─» |
| [chapters/03_struktura/03-05_parametry_podrobno.md:89](../chapters/03_struktura/03-05_parametry_podrobno.md) | `Процедура ПосчитатьЧто-нибудь()` | parser: Ожидалось «(», получено «-» |
| [chapters/03_struktura/03-05_parametry_podrobno.md:111](../chapters/03_struktura/03-05_parametry_podrobno.md) | `КурсВалюты = 92;` | чистый язык, не хватает контекста |
| [chapters/03_struktura/03-05_parametry_podrobno.md:155](../chapters/03_struktura/03-05_parametry_podrobno.md) | `// Корректно: сначала обязательные, потом необязательные` | parser: Неожиданный токен «.» |
| [chapters/03_struktura/03-05_parametry_podrobno.md:173](../chapters/03_struktura/03-05_parametry_podrobno.md) | `КурсДоставки = 150;` | чистый язык, не хватает контекста |
| [chapters/03_struktura/03-06_blok_shemy.md:238](../chapters/03_struktura/03-06_blok_shemy.md) | `Если Температура > 30 Тогда` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-01_chto_takoe_pattern.md:92](../chapters/04_patterny/04-01_chto_takoe_pattern.md) | `Итого = 0;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-01_chto_takoe_pattern.md:127](../chapters/04_patterny/04-01_chto_takoe_pattern.md) | `НайденТовар = Ложь;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-01_chto_takoe_pattern.md:139](../chapters/04_patterny/04-01_chto_takoe_pattern.md) | `Сумма = 0;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-01_chto_takoe_pattern.md:147](../chapters/04_patterny/04-01_chto_takoe_pattern.md) | `Количество = 0;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-02_poisk_elementa.md:48](../chapters/04_patterny/04-02_poisk_elementa.md) | `Для каждого Элемент Из Коллекция Цикл` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-02_poisk_elementa.md:134](../chapters/04_patterny/04-02_poisk_elementa.md) | `// Найти первый товар дороже 50 рублей` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-02_poisk_elementa.md:147](../chapters/04_patterny/04-02_poisk_elementa.md) | `// Найти товар, название которого начинается с "Кар"` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-02_poisk_elementa.md:234](../chapters/04_patterny/04-02_poisk_elementa.md) | `НайденныйТовар = Неопределено;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-02_poisk_elementa.md:254](../chapters/04_patterny/04-02_poisk_elementa.md) | `НайденнаяЦена = Неопределено;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-02_poisk_elementa.md:294](../chapters/04_patterny/04-02_poisk_elementa.md) | `НайденнаяЦена = Неопределено;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-02_poisk_elementa.md:334](../chapters/04_patterny/04-02_poisk_elementa.md) | `ДешёвыеЦены = Новый Массив;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-03_perebor_i_obrabotka.md:15](../chapters/04_patterny/04-03_perebor_i_obrabotka.md) | `Для каждого Элемент Из Коллекция Цикл` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-03_perebor_i_obrabotka.md:35](../chapters/04_patterny/04-03_perebor_i_obrabotka.md) | `Для каждого Товар Из Товары Цикл` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-03_perebor_i_obrabotka.md:43](../chapters/04_patterny/04-03_perebor_i_obrabotka.md) | `Для каждого Цена Из Цены Цикл` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-03_perebor_i_obrabotka.md:52](../chapters/04_patterny/04-03_perebor_i_obrabotka.md) | `ЦеныСоСкидкой = Новый Массив;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-03_perebor_i_obrabotka.md:79](../chapters/04_patterny/04-03_perebor_i_obrabotka.md) | `Для каждого Цена Из Цены Цикл` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-03_perebor_i_obrabotka.md:91](../chapters/04_patterny/04-03_perebor_i_obrabotka.md) | `Для каждого Цена Из Цены Цикл` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-03_perebor_i_obrabotka.md:108](../chapters/04_patterny/04-03_perebor_i_obrabotka.md) | `Для каждого Цена Из Цены Цикл` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-03_perebor_i_obrabotka.md:218](../chapters/04_patterny/04-03_perebor_i_obrabotka.md) | `Для каждого Товар Из Товары Цикл` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-04_agregaciya.md:40](../chapters/04_patterny/04-04_agregaciya.md) | `Итого = 0;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-04_agregaciya.md:69](../chapters/04_patterny/04-04_agregaciya.md) | `МаксимумНайден = Ложь;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-04_agregaciya.md:118](../chapters/04_patterny/04-04_agregaciya.md) | `Счётчик = 0;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-04_agregaciya.md:146](../chapters/04_patterny/04-04_agregaciya.md) | `Сумма = 0;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-04_agregaciya.md:169](../chapters/04_patterny/04-04_agregaciya.md) | `Задача       Инициализация   Обновление в цикле` | lexer: Неизвестный символ «─» |
| [chapters/04_patterny/04-04_agregaciya.md:259](../chapters/04_patterny/04-04_agregaciya.md) | `Максимум = 0;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-05_zashchitny_kod.md:33](../chapters/04_patterny/04-05_zashchitny_kod.md) | `Если Коллекция.Количество() = 0 Тогда` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-05_zashchitny_kod.md:76](../chapters/04_patterny/04-05_zashchitny_kod.md) | `НайденныйТовар = Неопределено;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-05_zashchitny_kod.md:105](../chapters/04_patterny/04-05_zashchitny_kod.md) | `Если Количество <> 0 Тогда` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-05_zashchitny_kod.md:143](../chapters/04_patterny/04-05_zashchitny_kod.md) | `Функция КоллекцияНеПуста(Коллекция)` | runtime: У значения типа «Неопределено» нет методов |
| [chapters/04_patterny/04-05_zashchitny_kod.md:232](../chapters/04_patterny/04-05_zashchitny_kod.md) | `Для каждого Товар Из Товары Цикл` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-05_zashchitny_kod.md:302](../chapters/04_patterny/04-05_zashchitny_kod.md) | `Если НайденнаяЦена = Неопределено Тогда` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-06_raspoznavanie.md:39](../chapters/04_patterny/04-06_raspoznavanie.md) | `Сумма = 0;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-06_raspoznavanie.md:70](../chapters/04_patterny/04-06_raspoznavanie.md) | `ПОИСК` | lexer: Неизвестный символ «─» |
| [chapters/04_patterny/04-06_raspoznavanie.md:198](../chapters/04_patterny/04-06_raspoznavanie.md) | `ПервоеЧётное = Неопределено;` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-06_raspoznavanie.md:220](../chapters/04_patterny/04-06_raspoznavanie.md) | `Если Слова.Количество() = 0 Тогда` | чистый язык, не хватает контекста |
| [chapters/04_patterny/04-06_raspoznavanie.md:291](../chapters/04_patterny/04-06_raspoznavanie.md) | `МинимумНайден = Ложь;` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-01_obekty_svoystva_metody.md:33](../chapters/05_idiomy/05-01_obekty_svoystva_metody.md) | `Сообщить(Документ.Номер);    // прочитать свойство Номер` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-01_obekty_svoystva_metody.md:40](../chapters/05_idiomy/05-01_obekty_svoystva_metody.md) | `Объект.Комментарий = "Срочно"; // записать в свойство` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-01_obekty_svoystva_metody.md:52](../chapters/05_idiomy/05-01_obekty_svoystva_metody.md) | `Объект.Записать();           // метод без аргументов` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-01_obekty_svoystva_metody.md:62](../chapters/05_idiomy/05-01_obekty_svoystva_metody.md) | `Массив.Добавить("Ручка");           // процедура: добавляет,` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-01_obekty_svoystva_metody.md:149](../chapters/05_idiomy/05-01_obekty_svoystva_metody.md) | `СтрДлина("Ручка")      // глобальная функция — НЕ метод` | parser: Ожидалось «;», получено «Ручка» |
| [chapters/05_idiomy/05-01_obekty_svoystva_metody.md:163](../chapters/05_idiomy/05-01_obekty_svoystva_metody.md) | `// Читаем свойства заказа` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-01_obekty_svoystva_metody.md:221](../chapters/05_idiomy/05-01_obekty_svoystva_metody.md) | `Сообщить(Документ.Организация.ИНН);` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-02_dostup_k_dannym.md:32](../chapters/05_idiomy/05-02_dostup_k_dannym.md) | `// Найти элемент справочника по наименованию` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-02_dostup_k_dannym.md:53](../chapters/05_idiomy/05-02_dostup_k_dannym.md) | `Ссылка = Справочники.Номенклатура.НайтиПоНаименованию("Ручка` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-02_dostup_k_dannym.md:75](../chapters/05_idiomy/05-02_dostup_k_dannym.md) | `Ссылка = Справочники.Номенклатура.НайтиПоНаименованию("Ручка` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-02_dostup_k_dannym.md:93](../chapters/05_idiomy/05-02_dostup_k_dannym.md) | `Выборка = Справочники.Номенклатура.Выбрать();` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-02_dostup_k_dannym.md:110](../chapters/05_idiomy/05-02_dostup_k_dannym.md) | `НазваниеТовара = "Тетрадь";` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-02_dostup_k_dannym.md:157](../chapters/05_idiomy/05-02_dostup_k_dannym.md) | `Выборка = Документы.РеализацияТоваров.Выбрать();` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-02_dostup_k_dannym.md:174](../chapters/05_idiomy/05-02_dostup_k_dannym.md) | `Ссылка = Справочники.Номенклатура.НайтиПоНаименованию("Линей` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-02_dostup_k_dannym.md:191](../chapters/05_idiomy/05-02_dostup_k_dannym.md) | `Ссылка = Справочники.Контрагенты.НайтиПоНаименованию("ООО Ро` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-02_dostup_k_dannym.md:218](../chapters/05_idiomy/05-02_dostup_k_dannym.md) | `Ссылка = Справочники.Номенклатура.НайтиПоНаименованию("Линей` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-03_tablychnye_chasti.md:50](../chapters/05_idiomy/05-03_tablychnye_chasti.md) | `Сообщить(Объект.Товары.Количество()); // сколько строк в таб` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-03_tablychnye_chasti.md:62](../chapters/05_idiomy/05-03_tablychnye_chasti.md) | `Для каждого Строка Из Объект.Товары Цикл` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-03_tablychnye_chasti.md:81](../chapters/05_idiomy/05-03_tablychnye_chasti.md) | `ИтогоСумма = 0;` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-03_tablychnye_chasti.md:93](../chapters/05_idiomy/05-03_tablychnye_chasti.md) | `СтрокаМаксимума = Неопределено;` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-03_tablychnye_chasti.md:118](../chapters/05_idiomy/05-03_tablychnye_chasti.md) | `Если Объект.Товары.Количество() = 0 Тогда` | parser: Неожиданный токен «.» |
| [chapters/05_idiomy/05-03_tablychnye_chasti.md:138](../chapters/05_idiomy/05-03_tablychnye_chasti.md) | `НоваяСтрока = Объект.Товары.Добавить();` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-03_tablychnye_chasti.md:154](../chapters/05_idiomy/05-03_tablychnye_chasti.md) | `// Предполагаем, что Документ уже получен (как — в § 5.4)` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-03_tablychnye_chasti.md:201](../chapters/05_idiomy/05-03_tablychnye_chasti.md) | `ПоложительныхСтрок = 0;` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-03_tablychnye_chasti.md:235](../chapters/05_idiomy/05-03_tablychnye_chasti.md) | `Для каждого Строка Из Объект.Товары Цикл` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-03_tablychnye_chasti.md:247](../chapters/05_idiomy/05-03_tablychnye_chasti.md) | `НоваяСтрока = Объект.Услуги.Добавить();` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-04_chto_takoe_ssylka.md:17](../chapters/05_idiomy/05-04_chto_takoe_ssylka.md) | `Ссылка ≠ Объект` | lexer: Неизвестный символ «≠» |
| [chapters/05_idiomy/05-04_chto_takoe_ssylka.md:61](../chapters/05_idiomy/05-04_chto_takoe_ssylka.md) | `Ссылка = Справочники.Номенклатура.НайтиПоНаименованию("Ручка` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-04_chto_takoe_ssylka.md:72](../chapters/05_idiomy/05-04_chto_takoe_ssylka.md) | `Объект = Ссылка.ПолучитьОбъект();` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-04_chto_takoe_ssylka.md:88](../chapters/05_idiomy/05-04_chto_takoe_ssylka.md) | `// Способ 1: через ЗначениеЗаполнено` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-04_chto_takoe_ssylka.md:108](../chapters/05_idiomy/05-04_chto_takoe_ssylka.md) | `// Сохранить ссылку в переменную` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-04_chto_takoe_ssylka.md:129](../chapters/05_idiomy/05-04_chto_takoe_ssylka.md) | `Ссылка = Документы.РеализацияТоваров.НайтиПоНомеру("РТ-00004` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-04_chto_takoe_ssylka.md:180](../chapters/05_idiomy/05-04_chto_takoe_ssylka.md) | `Сообщить(Документ.Склад.Ответственный.Наименование);` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-04_chto_takoe_ssylka.md:190](../chapters/05_idiomy/05-04_chto_takoe_ssylka.md) | `Ссылка = Справочники.Контрагенты.НайтиПоНаименованию("Несуще` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-04_chto_takoe_ssylka.md:228](../chapters/05_idiomy/05-04_chto_takoe_ssylka.md) | `Ссылка = Справочники.Контрагенты.НайтиПоНаименованию("Несуще` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-04_chto_takoe_ssylka.md:244](../chapters/05_idiomy/05-04_chto_takoe_ssylka.md) | `Сообщить(Ссылка.Наименование);   // чтение — ссылки достаточ` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-04_chto_takoe_ssylka.md:250](../chapters/05_idiomy/05-04_chto_takoe_ssylka.md) | `Объект = Ссылка.ПолучитьОбъект();` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-05_tipichnye_oboroty.md:17](../chapters/05_idiomy/05-05_tipichnye_oboroty.md) | `Тип              Пустое значение` | lexer: Неизвестный символ «─» |
| [chapters/05_idiomy/05-05_tipichnye_oboroty.md:47](../chapters/05_idiomy/05-05_tipichnye_oboroty.md) | `Ссылка = Справочники.Номенклатура.НайтиПоНаименованию("Ручка` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-05_tipichnye_oboroty.md:69](../chapters/05_idiomy/05-05_tipichnye_oboroty.md) | `Выборка = Справочники.Номенклатура.Выбрать();` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-05_tipichnye_oboroty.md:86](../chapters/05_idiomy/05-05_tipichnye_oboroty.md) | `// Создать новый элемент справочника` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-05_tipichnye_oboroty.md:108](../chapters/05_idiomy/05-05_tipichnye_oboroty.md) | `Если ЗначениеЗаполнено(Документ.Склад) Тогда` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-05_tipichnye_oboroty.md:124](../chapters/05_idiomy/05-05_tipichnye_oboroty.md) | `НовыйДокумент.Дата = ТекущаяДата();` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-05_tipichnye_oboroty.md:158](../chapters/05_idiomy/05-05_tipichnye_oboroty.md) | `Сообщить("Сумма: " + Формат(Итого, "ЧДЦ=2"));       // два з` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-05_tipichnye_oboroty.md:171](../chapters/05_idiomy/05-05_tipichnye_oboroty.md) | `// 1. Найти документ` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-05_tipichnye_oboroty.md:225](../chapters/05_idiomy/05-05_tipichnye_oboroty.md) | `// (а)` | чистый язык, не хватает контекста |
| [chapters/05_idiomy/05-05_tipichnye_oboroty.md:271](../chapters/05_idiomy/05-05_tipichnye_oboroty.md) | `НовыйТовар = Справочники.Номенклатура.СоздатьЭлемент();` | чистый язык, не хватает контекста |
| [chapters/06_kontekst/06-02_dokumenty_kak_sobytiya.md:78](../chapters/06_kontekst/06-02_dokumenty_kak_sobytiya.md) | `Ссылка = Документы.ПоступлениеТоваров.НайтиПоНомеру("ПТ-0000` | чистый язык, не хватает контекста |
| [chapters/06_kontekst/06-02_dokumenty_kak_sobytiya.md:150](../chapters/06_kontekst/06-02_dokumenty_kak_sobytiya.md) | `Ссылка = Документы.РеализацияТоваров.НайтиПоНомеру("РТ-00002` | чистый язык, не хватает контекста |
| [chapters/06_kontekst/06-03_zhiznennyy_tsikl_dokumenta.md:15](../chapters/06_kontekst/06-03_zhiznennyy_tsikl_dokumenta.md) | `Состояние              Что это значит` | lexer: Неизвестный символ «─» |
| [chapters/06_kontekst/06-03_zhiznennyy_tsikl_dokumenta.md:37](../chapters/06_kontekst/06-03_zhiznennyy_tsikl_dokumenta.md) | `// Просто сохранить документ (без проведения)` | чистый язык, не хватает контекста |
| [chapters/06_kontekst/06-03_zhiznennyy_tsikl_dokumenta.md:68](../chapters/06_kontekst/06-03_zhiznennyy_tsikl_dokumenta.md) | `Объект = Ссылка.ПолучитьОбъект();` | чистый язык, не хватает контекста |
| [chapters/06_kontekst/06-03_zhiznennyy_tsikl_dokumenta.md:85](../chapters/06_kontekst/06-03_zhiznennyy_tsikl_dokumenta.md) | `// Найти все документы за период и провести их` | чистый язык, не хватает контекста |
| [chapters/06_kontekst/06-03_zhiznennyy_tsikl_dokumenta.md:114](../chapters/06_kontekst/06-03_zhiznennyy_tsikl_dokumenta.md) | `// Шаг 3: запись (без проведения)` | чистый язык, не хватает контекста |
| [chapters/06_kontekst/06-03_zhiznennyy_tsikl_dokumenta.md:160](../chapters/06_kontekst/06-03_zhiznennyy_tsikl_dokumenta.md) | `Ссылка = Документы.РеализацияТоваров.НайтиПоНомеру("РТ-00000` | чистый язык, не хватает контекста |
| [chapters/06_kontekst/06-03_zhiznennyy_tsikl_dokumenta.md:199](../chapters/06_kontekst/06-03_zhiznennyy_tsikl_dokumenta.md) | `Ссылка = Документы.ПоступлениеТоваров.НайтиПоНомеру("ПТ-0000` | чистый язык, не хватает контекста |
| [chapters/06_kontekst/06-03_zhiznennyy_tsikl_dokumenta.md:222](../chapters/06_kontekst/06-03_zhiznennyy_tsikl_dokumenta.md) | `Ссылка = Документы.РеализацияТоваров.НайтиПоНомеру("РТ-00002` | чистый язык, не хватает контекста |
| [chapters/06_kontekst/06-04_registry.md:33](../chapters/06_kontekst/06-04_registry.md) | `Пример регистра «ТоварыНаСкладах»:` | lexer: Неизвестный символ ««» |
| [chapters/06_kontekst/06-05_perevod_zadacha_kod.md:61](../chapters/06_kontekst/06-05_perevod_zadacha_kod.md) | `Ссылка = Справочники.Контрагенты.НайтиПоНаименованию("ООО Ст` | чистый язык, не хватает контекста |
| [chapters/06_kontekst/06-05_perevod_zadacha_kod.md:103](../chapters/06_kontekst/06-05_perevod_zadacha_kod.md) | `// (1)` | чистый язык, не хватает контекста |
| [chapters/06_kontekst/06-05_perevod_zadacha_kod.md:245](../chapters/06_kontekst/06-05_perevod_zadacha_kod.md) | `Счётчик = 0;` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-01_chto_takoe_khoroshiy_kod.md:73](../chapters/07_kachestvo/07-01_chto_takoe_khoroshiy_kod.md) | `П = 0;` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-02_obrabotka_oshibok.md:62](../chapters/07_kachestvo/07-02_obrabotka_oshibok.md) | `Ссылка = Документы.ПоступлениеТоваров.НайтиПоНомеру("ПТ-0000` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-02_obrabotka_oshibok.md:91](../chapters/07_kachestvo/07-02_obrabotka_oshibok.md) | `// Правильно: пустую ссылку проверяем до операции` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-02_obrabotka_oshibok.md:196](../chapters/07_kachestvo/07-02_obrabotka_oshibok.md) | `Ссылка = Документы.РеализацияТоваров.НайтиПоНомеру("РТ-00009` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-02_obrabotka_oshibok.md:218](../chapters/07_kachestvo/07-02_obrabotka_oshibok.md) | `Ссылка = Справочники.Номенклатура.НайтиПоНаименованию("Ручка` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-02_obrabotka_oshibok.md:247](../chapters/07_kachestvo/07-02_obrabotka_oshibok.md) | `Ссылка = Справочники.Номенклатура.НайтиПоНаименованию("Ручка` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:27](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `Процедура СделатьЧтоТо(Параметр1, Параметр2)` | parser: Неожиданный токен «.» |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:55](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `Если НЕ ЗначениеЗаполнено(ДокументСсылка) Тогда` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:63](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `Если КоличествоДней <= 0 Тогда` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:71](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `Если НЕ ЗначениеЗаполнено(НаименованиеТовара) Тогда` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:79](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `Если Документ.Товары.Количество() = 0 Тогда` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-04_proizvoditelnost.md:27](../chapters/07_kachestvo/07-04_proizvoditelnost.md) | `// Медленно: 1000 объектов = 1000 обращений к базе` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-04_proizvoditelnost.md:38](../chapters/07_kachestvo/07-04_proizvoditelnost.md) | `// Быстро: читаем атрибуты напрямую из выборки` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-04_proizvoditelnost.md:54](../chapters/07_kachestvo/07-04_proizvoditelnost.md) | `// Медленно: каждый товар — отдельная транзакция` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-04_proizvoditelnost.md:74](../chapters/07_kachestvo/07-04_proizvoditelnost.md) | `// Медленно: перебираем все документы за все годы,` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-04_proizvoditelnost.md:87](../chapters/07_kachestvo/07-04_proizvoditelnost.md) | `// Быстрее: выборка уже ограничена периодом` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-04_proizvoditelnost.md:105](../chapters/07_kachestvo/07-04_proizvoditelnost.md) | `// Медленно: для каждого контрагента перебираем все документ` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-04_proizvoditelnost.md:140](../chapters/07_kachestvo/07-04_proizvoditelnost.md) | `Выборка = Справочники.Номенклатура.Выбрать();` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-04_proizvoditelnost.md:155](../chapters/07_kachestvo/07-04_proizvoditelnost.md) | `Выборка = Справочники.Номенклатура.Выбрать();` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-04_proizvoditelnost.md:196](../chapters/07_kachestvo/07-04_proizvoditelnost.md) | `Выборка = Документы.ПоступлениеТоваров.Выбрать();` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-04_proizvoditelnost.md:224](../chapters/07_kachestvo/07-04_proizvoditelnost.md) | `ИтогоСумма = 0;` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-04_proizvoditelnost.md:248](../chapters/07_kachestvo/07-04_proizvoditelnost.md) | `НачалоГода = НачалоГода(ТекущаяДата());` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-05_chitaemost.md:69](../chapters/07_kachestvo/07-05_chitaemost.md) | `// Плохо: очевидно и без комментария` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-05_chitaemost.md:133](../chapters/07_kachestvo/07-05_chitaemost.md) | `// Плохо: что такое 0.05? что такое 50000?` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-05_chitaemost.md:218](../chapters/07_kachestvo/07-05_chitaemost.md) | `Н = 0;` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-05_chitaemost.md:234](../chapters/07_kachestvo/07-05_chitaemost.md) | `// (а)` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-05_chitaemost.md:279](../chapters/07_kachestvo/07-05_chitaemost.md) | `Если КатегорияКлиента = "VIP" И СуммаЗаказа > 100000 Тогда` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-05_chitaemost.md:295](../chapters/07_kachestvo/07-05_chitaemost.md) | `КоличествоДорогихТоваров = 0;` | чистый язык, не хватает контекста |
| [chapters/07_kachestvo/07-05_chitaemost.md:357](../chapters/07_kachestvo/07-05_chitaemost.md) | `КатегорияVIP            = "VIP";` | чистый язык, не хватает контекста |
| [chapters/08_sistema/08-01_put_dannykh.md:231](../chapters/08_sistema/08-01_put_dannykh.md) | `Движения.ТоварыНаСкладах.Записывать = Истина;` | чистый язык, не хватает контекста |
| [chapters/08_sistema/08-02_moduli.md:54](../chapters/08_sistema/08-02_moduli.md) | `// Это вызов метода модуля менеджера документа:` | чистый язык, не хватает контекста |
| [chapters/08_sistema/08-02_moduli.md:161](../chapters/08_sistema/08-02_moduli.md) | `// Строка 1` | чистый язык, не хватает контекста |
| [chapters/08_sistema/08-02_moduli.md:207](../chapters/08_sistema/08-02_moduli.md) | `// Строка 1: НайтиПоНаименованию — метод модуля менеджера сп` | чистый язык, не хватает контекста |
| [chapters/08_sistema/08-03_karta_obyektov.md:30](../chapters/08_sistema/08-03_karta_obyektov.md) | `// Пример использования перечисления:` | parser: Неожиданный токен «.» |
| [chapters/08_sistema/08-03_karta_obyektov.md:145](../chapters/08_sistema/08-03_karta_obyektov.md) | `Курс = РегистрыСведений.КурсыВалют.ПолучитьПоследнее(Текущая` | чистый язык, не хватает контекста |
| [chapters/09_zavershenie/09-01_kontrolnaya_zadacha.md:182](../chapters/09_zavershenie/09-01_kontrolnaya_zadacha.md) | `ЕстьОшибка = Ложь;` | parser: Неожиданный токен «.» |
| [chapters/09_zavershenie/09-01_kontrolnaya_zadacha.md:197](../chapters/09_zavershenie/09-01_kontrolnaya_zadacha.md) | `Если ПроцентИзменения < -50 Тогда` | чистый язык, не хватает контекста |
| [chapters/09_zavershenie/09-04_kak_chitat.md:64](../chapters/09_zavershenie/09-04_kak_chitat.md) | `// Имя говорит всё:` | parser: Неожиданный токен «.» |

## `платформа` — 20

| Где | Первая строка | Почему |
|---|---|---|
| [chapters/00_vvedenie/00-05_gde_zdes_1s.md:69](../chapters/00_vvedenie/00-05_gde_zdes_1s.md) | `Справочник «Товары»     («что» мы продаём)` | платформенные объекты |
| [chapters/00_vvedenie/00-05_gde_zdes_1s.md:104](../chapters/00_vvedenie/00-05_gde_zdes_1s.md) | `Документ «Поступление товара»  (поступать — приходить)` | платформенные объекты |
| [chapters/00_vvedenie/00-05_gde_zdes_1s.md:300](../chapters/00_vvedenie/00-05_gde_zdes_1s.md) | `Справочник «Напитки»     (капучино, эспрессо, латте, чай...)` | платформенные объекты |
| [chapters/00_vvedenie/00-05_gde_zdes_1s.md:309](../chapters/00_vvedenie/00-05_gde_zdes_1s.md) | `Документ «Чек продажи»       (одна продажа клиенту)` | платформенные объекты |
| [chapters/07_kachestvo/07-03_zashchitnyy_kod.md:288](../chapters/07_kachestvo/07-03_zashchitnyy_kod.md) | `Процедура ПровестиДокумент(Ссылка)` | платформенные объекты |
| [chapters/07_kachestvo/07-05_chitaemost.md:47](../chapters/07_kachestvo/07-05_chitaemost.md) | `// Плохо: непонятно, что делает` | платформенные объекты |
| [chapters/08_sistema/08-04_baryery.md:27](../chapters/08_sistema/08-04_baryery.md) | `Клиент (у пользователя)          Сервер (серверная часть)` | платформенные объекты |
| [chapters/08_sistema/08-04_baryery.md:116](../chapters/08_sistema/08-04_baryery.md) | `Запрос = Новый Запрос;` | платформенные объекты |
| [chapters/08_sistema/08-04_baryery.md:146](../chapters/08_sistema/08-04_baryery.md) | `&НаКлиенте` | платформенные объекты |
| [chapters/08_sistema/08-04_baryery.md:160](../chapters/08_sistema/08-04_baryery.md) | `КомпоновщикНастроек = Новый КомпоновщикНастроек;` | платформенные объекты |
| [chapters/08_sistema/08-05_direktivy.md:23](../chapters/08_sistema/08-05_direktivy.md) | `&НаКлиенте` | платформенные объекты |
| [chapters/08_sistema/08-05_direktivy.md:33](../chapters/08_sistema/08-05_direktivy.md) | `&НаСервере` | платформенные объекты |
| [chapters/08_sistema/08-05_direktivy.md:43](../chapters/08_sistema/08-05_direktivy.md) | `&НаСервереБезКонтекста` | платформенные объекты |
| [chapters/08_sistema/08-05_direktivy.md:58](../chapters/08_sistema/08-05_direktivy.md) | `&НаКлиенте` | платформенные объекты |
| [chapters/08_sistema/08-05_direktivy.md:164](../chapters/08_sistema/08-05_direktivy.md) | `&НаСервере` | платформенные объекты |
| [chapters/08_sistema/08-05_direktivy.md:185](../chapters/08_sistema/08-05_direktivy.md) | `&НаСервере` | платформенные объекты |
| [chapters/08_sistema/08-05_direktivy.md:201](../chapters/08_sistema/08-05_direktivy.md) | `&НаКлиенте` | платформенные объекты |
| [chapters/08_sistema/08-05_direktivy.md:213](../chapters/08_sistema/08-05_direktivy.md) | `#Область ОбработчикиСобытий` | платформенные объекты |
| [chapters/08_sistema/08-05_direktivy.md:258](../chapters/08_sistema/08-05_direktivy.md) | `&НаКлиенте` | платформенные объекты |
| [chapters/09_zavershenie/09-01_kontrolnaya_zadacha.md:26](../chapters/09_zavershenie/09-01_kontrolnaya_zadacha.md) | `&НаСервереБезКонтекста` | платформенные объекты |

## `шаблон` — 21

| Где | Первая строка | Почему |
|---|---|---|
| [chapters/01_leksika/01-02_vyrazheniya_i_operatory.md:336](../chapters/01_leksika/01-02_vyrazheniya_i_operatory.md) | `Ручки: 25 шт. по 18 руб., итого с НДС: <сумма> руб.` | плейсхолдеры в угловых скобках |
| [chapters/01_leksika/01-04_komanda_esli.md:49](../chapters/01_leksika/01-04_komanda_esli.md) | `=    равно                  Цена = 100        →  Истина, есл` | плейсхолдеры в угловых скобках |
| [chapters/01_leksika/01-04_komanda_esli.md:62](../chapters/01_leksika/01-04_komanda_esli.md) | `Сравнение      Что вычислится` | плейсхолдеры в угловых скобках |
| [chapters/01_leksika/01-04_komanda_esli.md:111](../chapters/01_leksika/01-04_komanda_esli.md) | `Если <условие> Тогда` | плейсхолдеры в угловых скобках |
| [chapters/01_leksika/01-04_komanda_esli.md:205](../chapters/01_leksika/01-04_komanda_esli.md) | `Если <условие> Тогда` | плейсхолдеры в угловых скобках |
| [chapters/01_leksika/01-04_komanda_esli.md:243](../chapters/01_leksika/01-04_komanda_esli.md) | `Если <условие 1> Тогда` | плейсхолдеры в угловых скобках |
| [chapters/01_leksika/01-04_komanda_esli.md:375](../chapters/01_leksika/01-04_komanda_esli.md) | `А = 5 < 7` | плейсхолдеры в угловых скобках |
| [chapters/01_leksika/01-04_komanda_esli.md:437](../chapters/01_leksika/01-04_komanda_esli.md) | `А = 5 < 7              →  Истина  (5 действительно меньше 7)` | плейсхолдеры в угловых скобках |
| [chapters/02_semantika/02-02_tipy_znacheniy.md:190](../chapters/02_semantika/02-02_tipy_znacheniy.md) | `1. Арифметические: *, /, +, -    (сначала)` | плейсхолдеры в угловых скобках |
| [chapters/03_struktura/03-02_tsikl_poka.md:49](../chapters/03_struktura/03-02_tsikl_poka.md) | `Пока <Условие> Цикл` | плейсхолдеры в угловых скобках |
| [chapters/03_struktura/03-02_tsikl_poka.md:141](../chapters/03_struktura/03-02_tsikl_poka.md) | `Счётчик = <начало>;` | плейсхолдеры в угловых скобках |
| [chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md:55](../chapters/03_struktura/03-03_tsikl_dlya_kazhdogo.md) | `Для Каждого <Переменная> Из <Коллекция> Цикл` | плейсхолдеры в угловых скобках |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:51](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `Процедура <Имя>(<Параметры>)` | плейсхолдеры в угловых скобках |
| [chapters/03_struktura/03-04_procedury_i_funkcii.md:82](../chapters/03_struktura/03-04_procedury_i_funkcii.md) | `Функция <Имя>(<Параметры>)` | плейсхолдеры в угловых скобках |
| [chapters/04_patterny/04-02_poisk_elementa.md:17](../chapters/04_patterny/04-02_poisk_elementa.md) | `НайденныйЭлемент = Неопределено;` | плейсхолдеры в угловых скобках |
| [chapters/04_patterny/04-02_poisk_elementa.md:166](../chapters/04_patterny/04-02_poisk_elementa.md) | `НайденныеТовары = Новый Массив;` | плейсхолдеры в угловых скобках |
| [chapters/04_patterny/04-03_perebor_i_obrabotka.md:67](../chapters/04_patterny/04-03_perebor_i_obrabotka.md) | `Для каждого Элемент Из Коллекция Цикл` | плейсхолдеры в угловых скобках |
| [chapters/04_patterny/04-04_agregaciya.md:17](../chapters/04_patterny/04-04_agregaciya.md) | `Результат = <начальное значение>;` | плейсхолдеры в угловых скобках |
| [chapters/04_patterny/04-04_agregaciya.md:105](../chapters/04_patterny/04-04_agregaciya.md) | `Счётчик = 0;` | плейсхолдеры в угловых скобках |
| [chapters/06_kontekst/06-05_perevod_zadacha_kod.md:182](../chapters/06_kontekst/06-05_perevod_zadacha_kod.md) | `НачалоМес = НачалоМесяца(ТекущаяДата());` | плейсхолдеры в угловых скобках |
| [chapters/07_kachestvo/07-01_chto_takoe_khoroshiy_kod.md:88](../chapters/07_kachestvo/07-01_chto_takoe_khoroshiy_kod.md) | `// Подсчёт суммы проведённых поступлений за текущий месяц` | плейсхолдеры в угловых скобках |

## `ловушка` — 5

| Где | Первая строка | Почему |
|---|---|---|
| [chapters/03_struktura/03-02_tsikl_poka.md:180](../chapters/03_struktura/03-02_tsikl_poka.md) | `Счётчик = 1;` | бесконечный цикл — показан нарочно |
| [chapters/03_struktura/03-02_tsikl_poka.md:196](../chapters/03_struktura/03-02_tsikl_poka.md) | `НужнаОплата = Истина;` | бесконечный цикл — показан нарочно |
| [chapters/03_struktura/03-02_tsikl_poka.md:208](../chapters/03_struktura/03-02_tsikl_poka.md) | `// Ошибка: счётчик уменьшается, а условие требует <= 10` | бесконечный цикл — показан нарочно |
| [chapters/03_struktura/03-02_tsikl_poka.md:358](../chapters/03_struktura/03-02_tsikl_poka.md) | `КоличествоТоваров = 0;` | бесконечный цикл — показан нарочно |
| [chapters/03_struktura/03-02_tsikl_poka.md:381](../chapters/03_struktura/03-02_tsikl_poka.md) | `Х = 1;` | бесконечный цикл — показан нарочно |

## `текст` — 193

_Списком не приводится: это не код._

