# Домашнее задание к лекции 2.2 «Regular expressions»

Иногда при знакомстве мы записываем контакты в адресную книгу кое-как с мыслью, что "когда-нибудь потом все обязательно поправим". Копируем данные из интернета или из смски. Добавляем людей в разных мессенджерах. В результате получается адресная книга, в которой совершенно невозможно кого-то нормально найти: мешает множество дублей, разная запись одних и тех же имен и телефонов.

Кейс основан на реальных данных из https://www.nalog.ru/opendata/, https://www.minfin.ru/ru/opendata/

Ваша задача: привести в порядок адресную книгу, используя регулярные выражения.  
Структура данных будет всегда такая:   
`lastname,firstname,surname,organization,position,phone,email`  

Предполагается, что:
* телефон и e-mail у одного человека может быть только один;
* если совпали одновременно Фамилия и Имя, это точно один и тот же человек (даже если не указано его отчество).

Ваша задача:
1. Поместить Фамилию, Имя и Отчество человека в поля `lastname`, `firstname` и `surname` соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О. _Подсказка: работайте со срезом списка (три первых элемента) при помощи `" ".join([:2])` и `split(" ")`, регулярки здесь НЕ НУЖНЫ_.  
2. Привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999. _Подсказка: используйте регулярки для обработки телефонов_.
3. Объединить все дублирующиеся записи о человеке в одну. _Подсказка: группируйте записи по ФИО (если будет сложно, допускается группировать только по ФИ)_.

```python
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)
```

---
Домашнее задание сдается ссылкой на репозиторий [BitBucket](https://bitbucket.org/) или [GitHub](https://github.com/)

Не сможем проверить или помочь, если вы пришлете:
* архивы;
* скриншоты кода;
* теоретический рассказ о возникших проблемах.    
