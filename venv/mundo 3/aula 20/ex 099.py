def maior(* num):
    c=num
    b=len(num)
    if b==0:
        print(f'Dos numeros {c}')
        print(f'o maior numero foi: {0}')
    else:
        print(f'Dos numeros {c}')
        print(f'o maior numero foi: {max(c)}')
        print('-='*20)


maior(3,2,4,1,4,9,2)
maior(3,2,4,1,4)
maior()