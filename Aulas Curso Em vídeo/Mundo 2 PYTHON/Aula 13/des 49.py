num= int(input('Digite 1 número para ver a sua tabuada: '))
cal= 0
for c in range(1,11):
    cal= c * num
    print('{} x {} = {}'.format(num,c,cal))