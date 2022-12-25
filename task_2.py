print('Ввод 10 цифр и подсчет количества введенных цифр 5')
k = 0
for i in range(10):
    num = int(input())
    if num == 5:
        k = k+1
print('Количество цифр 5: '+str(k))