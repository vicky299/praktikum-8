buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

while True:
    y = input('Nama buah yang dibeli:')
    x = input('Berapa Kg :')
    t =int(input('masukkan bilangan bulat:'))
    print('lagi (y/n)?:')
    print('Data buah:')
    print('-	Apel (Harga Rp 5000')
    print('-	Jeruk (Harga Rp 8500')
    print('-	Mangga (Harga Rp 7800')
    print('-	Duku (Harga 6500')
    print('-	XXXX (Harga Rp XXX)')
    del buah['jeruk'] 
    if jawab == 'y':
        y = input('Nama buah yang dibeli:')
        x = input('Berapa Kg :')
        t =int(input('masukkan bilangan bulat:'))
        print('lagi (y/n)?:')
    if jawab =='n':
        print('-----------------------------------------')
        z = print('Total harga:')
        break
