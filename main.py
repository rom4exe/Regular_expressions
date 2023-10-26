from itertools import groupby
from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  # pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
pattern = r"(\+7|8)\W*(\d{3})\W*(\d{3})\W?(\d{2})\W?(\d{2})\s?\(?(доб.)?\.?\s?(\d+)?\)?"
filt = r"+7(\2)\3-\4-\5 \6\7"

tel_list = []
for i in contacts_list:
    # full_name = list(filter(None, ' '.join(item[:3]).split(' ')))
    fio = ' '.join(i[:3]).split(' ')
    tel_list+= [[fio[0], fio[1], fio[2], i[3], i[4], re.sub(pattern, filt, i[5]), i[6]]]
# print (tel_list)

for line1 in tel_list:
    for line2 in tel_list:
        if line2[0] == line1[0] and line2[1] == line1[1]:
            for cell in range(len(line2)):
                    if line1[cell] == "":
                        line1[cell] = line2[cell]
                    else: line2[cell] = line1[cell]

tel_list_corr = []
for i in tel_list:
    if i not in tel_list_corr:
        tel_list_corr += [i]
print(tel_list_corr)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook_res.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(tel_list_corr)
