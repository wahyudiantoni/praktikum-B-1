print('praktikum-3')
print('NAMA   : WAHYUDI ANTONI')
print('NIM    : 231031053')
print('prody  : Sistem Informasi B')
######################################
a = True
b = False

print('==========NAND==========')
hasil = not (a and a)
print(a,'nand',a,'adalah = ',hasil)
hasil = not (a and b)
print(a,'nand',b,'adalah = ',hasil)
hasil = not (b and a)
print(b,'nand',a,'adalah = ',hasil)
hasil = not (b and b)
print(b,'nand',b,'adalah = ',hasil)

print('==========NOR==========')
hasil = not (a or a)
print(a,'nor',a,'adalah = ',hasil)
hasil = not (a or b)
print(a,'nor',b,'adalah = ',hasil)
hasil = not (b or a)
print(b,'nor',a,'adalah = ',hasil)
hasil = not (b or b)
print(b,'nor',b,'adalah = ',hasil)

print('==========NXOR==========')
hasil = not (a ^ a)
print(a,'nxor',a,'adalah = ',hasil)
hasil = not (a ^ b)
print(a,'nxor',b,'adalah = ',hasil)
hasil = not (b ^ a)
print(b,'nxor',a,'adalah = ',hasil)
hasil = not (b ^ b)
print(b,'nxor',b,'adalah = ',hasil)

# INI OPRATOR MEMBERSHIP
print('\n========== IN ==========')
nama = 'wahyudi'

test = 'yu' #ISI dengan 2 huruf ada d nama
cek  = test in nama
print(test,'ada di',nama,'adalah=',cek)

test = 'uy' #ISI dengan 2 huruf ada d nama
cek  = test in nama
print(test,'ada di',nama,'adalah=',cek)

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 in nama 
print(test,'ada di',nama,'adalah=',cek)

cek = test2 in nama 
print(test,'ada di',nama,'adalah=',cek)

cek = test3 in nama 
print(test,'ada di',nama,'adalah=',cek)

cek = test4 in nama
print(test,'ada di',nama,'adalah=',cek)

cek = test5 in nama
print(test,'ada di',nama,'adalah=',cek)
# TUGAS lanjutkan kode
# dengan cara yang sama buat oprator not in

# INI oprator
print('\n')
a = 5 #Tanggal Lahir
b = 8 #Bulan Lahir
a *= 60
b *= 80

print('==========AND==========')
print('nilai',a,'biner adalah     =',format(a,'09b'))
print('nilai',b,'biner adalah     =',format(b,'09b'))
print('------------------------------------AND')      
c = a & b
print('nilai',a,'&',b,'biner adalah=',format(c,'09b'))
      
print('==========OR==========')
# Tugas buat untuk OR

print('==========XOR==========')
# Tugas buat untuk XOR

print('==========NOT==========')
# Tugas buat untuk NOT

print('\n==========AND==========')
c = ~a
print('Nilai not',a,'biner adalah     =',format(a,'09b'))
print('Nilai not',a,'biner adalah     =',format(c,'09b'))
#Tugas Lanjutkan untuk not b

print('\n==========Left Shift==========')
c = a << 2
print('Nilai not',a,'biner adalah     =',format(a,'09b'))
print('Nilai not',a,'<<biner adalah   =',format(c,'09b'))

c = b << 2
print('Nilai not',b,'biner adalah     =',format(b,'09b'))
print('Nilai not',b,'<<biner adalah   =',format(c,'09b'))

print('\n==========Right Shift==========')
c = a >> 2
print('Nilai not',a,'biner adalah     =',format(a,'09b'))
print('Nilai not',a,'>>biner adalah   =',format(c,'09b'))

c = a << 2
print('Nilai not',b,'biner adalah     =',format(b,'09b'))
print('Nilai not',b,'>>biner adalah   =',format(c,'09b'))