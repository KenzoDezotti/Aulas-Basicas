def crescente():
    for i in range(1,4):
        yield(i)

for i in crescente():
    print(i)
