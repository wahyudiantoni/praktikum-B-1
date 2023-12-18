import os
os.system('cls')

a = True

while a :
    jawab = input('Apakah Ingin Melanjutkan? (y/n)')
    if jawab == 'y':
        os.system('cls')
        print('Selamat Datang Lagi')
        a = True
    elif jawab == 'n':
        print('Sampai Ketemu Lagi :D')
        a = False
    else:

        os.system('cls')
        print('jangan aneh aneh deh :.)')
        a = True
        
    
