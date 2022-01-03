def maior(* num):
    print('dos numeros informados ',end='')
    for n in num:
        print(f'{n} ',end='')
    if len(num)==0:
        print('O maior numero foi 0')
    else:
        print(f' o maior foi {max(num)}')


maior(3,2,4,1,4,9,2)
maior(3,2,4,1,4)
maior()