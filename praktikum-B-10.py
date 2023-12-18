import os

def judul() :
    os.system('cls')
    print('program memnghitung volume dan luas permukaan'.center(45))
    print('bangun ruang balok'.center(45))
    print()
def inputan():
    p = float(input('masukkan panjang '))
    l = float(input('masukkan lebar '))
    t = float(input('masukkan tinggi '))
    return p,l,t
def hitung(p,l,t):
    vol = p*l*t
    luas_surf = 2*(p*1 + p*t + p*l)
    luas_non_tutup = luas_surf - p*1
    return vol,luas_surf,luas_non_tutup
def tampilan(pesan,nilai):
    print(f'nilai {pesan} : {nilai}')
def pilihan():
    pilih = input('apakah lamjutkan ? [yes/no] ')
    if pilih == 'y':
        a = True
    else :
        a = False
        print('terima kasih')
    return a
def main():
    judul()                                      # judul   
    p,l,t = inputan()                            # inputan                                                # hitung
    vol,luas_surf,luas_non_tutup = hitung(p,l,t) # hitung
    #tampilan
    tampilan('volume',vol)
    tampilan('luas permukaan',luas_surf)
    tampilan('luas permukaan tanpa tutup',luas_non_tutup)
    a = pilihan()                                # pilihan
    return a

a = True
while a : 
    a = main()


