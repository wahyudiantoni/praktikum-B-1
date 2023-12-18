import os
os.system('cls')

pwd_benar = 'si23b'
a = True
i = 0
limit = 3
while a :
    i += 1
    pwd = input('Masukkan Password: ')
    if pwd == pwd_benar:
        print('Selamat Anda Login!')
        a = False
    else:
        if i == limit:
            a = False    
            print('kehabisan kesempatan')
        else:
            print('Password Salah, Coba Lagi sisa percobaan : ',limit - i)
             
