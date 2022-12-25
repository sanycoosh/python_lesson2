from collections import Counter
with open('file_text.txt',encoding='utf-8') as f:
    t = f.read()
t = t.replace('.','')
t = t.replace(',','')
t = t.replace(';','')
t = t.replace('—','')
t = t.replace('«','')
t = t.replace('»','')
t = t.replace('?','')
t = t.replace('(','')
t = t.replace(')','')
t = t.replace(':','')
t = t.replace('!','')
t = t.replace('\n','')
# формируем список слов
spisok = t.split(' ')
# преобразуем все слова к нижнему регистру
new_spisok = list(map(lambda x: x.lower(), spisok))
print (new_spisok)
d = Counter(new_spisok)
print(d)
result = sorted(d.items(), key=lambda t: t[1], reverse=True)
print(result[:5])
slova = ''
for k,v in result[:5]:
  slova = slova+k+','
slova = slova[:-1]
print('Вывод пяти наиболее часто встречающихся слов: '+slova)
res = 0
for key in d:
    if d[key] == 1:
        res = res + 1
print('Количество разных слов в тексте: '+str(res))