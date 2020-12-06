dataNilai= []
i = 1
while True:
    print('masukkan data ke-'+ str(i)+':', end='')
    x=int(input())
    if x == 0:
        break
    else:
        dataNilai = dataNilai + [x]
    i = i + 1

dataNilai.sort(reverse=True)
print(dataNilai)

