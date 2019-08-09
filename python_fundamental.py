# x=4
# y=3
# z=2

# w=((x+y*z)/(x*y))**z
# print(w)

# x=int(input('silahkan masukkan angka berapapun: '))
# hasil=x**2
# print('kuadrat dari '+ str(x)+' = '+ str(hasil))

# tahun=360
# bulan=30
# minggu=7
# hari=1

# total=485
# thn=(total//tahun)
# bln=(total%tahun//bulan)
# mgg=(total%tahun%bulan//minggu)
# hri=(total%tahun%bulan%minggu)
# print('485 hari = '+ str(thn) +' tahun '+ str(bln) + ' bulan ' + str(mgg) + ' minggu '+ str(hri)+ ' hari ')

# #a+b=49
# 49-b=a
# #a=4/10 b
# 10a=4b
# #490-10b=4b
#490=14b
# b=490/14
# a=49-b
# b2=b+2
# a2=a+2
# print('umur budi: '+ str(b)+'.'+'setelah 2 tahun: '+ str(b2))
# print('umur andi: '+ str(a)+'.'+ 'setelah 2tahun: '+ str(a2))

# kata=input('tulis kata: ')
# x=input('masukkan huruf yang ingin dicari: ')
# proses=int(len(kata.split(x))-1)
# print(str((kata) + ' memiliki huruf ' + str(x) + ' sebanyak ' + str(proses)))

# angka=input('input: ')
# print(angka[1]+angka[0])

# from math import pi
# r=int(input('input radius: '))

# print('output: '+str(pi*r**2))

# in1=input('input: ')
# in2=input('input: ')
# print(in1[0]+in2[0]+in1[1]+in2[1])

# teks=input('masukkan kata: ')
# x=input('masukkan karakter yg ingin dihilangkan: ')
# print('output: '+ (teks.replace(x,'')))

# teks= input('input kata: ')
# list=teks.split()
# print('output: ' + list[1] + ' ' + list[0])

# x=int(input('masukkan angka: '))

# if (x%2==0):
#     print('angka genap')
# else:
#     print('angka ganjil')

# massa=float(input('masukkan massa: '))
# Tinggi=float(input('masukkan tinggi: '))
# Tinggi_meter=Tinggi/100
# imt=(massa/Tinggi_meter)**2

# if (imt < 18.5):
#     x='bb kurang'
# elif (imt >= 18.5 and imt <= 24.9):   
#     x='bb ideal'
# elif (imt >= 25.0 and imt <= 29.9):
#     x='bb berlebih'
# elif (imt >= 30.0 and imt <= 39.9):
#     x='bb sangat berlebih'
# elif (imt >= 39.9):
#     x='obesitas'
# print('massa' + ' ' + str(massa) + ' kg ' + ' & ' + ' tinggi ' + ' ' + str(Tinggi_meter))
# print('imt' + ' ' + str(imt) + ' ' + x)

# z=''
# for item in range(0,5):
#     for item1 in range (0,5):
#         z += ' * '
#     z +='\n'
# print(z)

# z=''
# for item in range (0,5):
#     for item1 in range (0,item+1):
#         z += ' * '
#     z +='\n'
# print(z)

# z=''
# for item in range (5,0,-1):
#     for item1 in range (0, item):
#         z +=' * '
#     z +='\n'
# print(z)

# z=''
# for x in range (5,0,-1):
#     if (x > 1):
#         for y in range (0,x):
#             z += ' * '
#         z += '\n'
#     elif (x==1):
#         for x in range (0,5):
#             for y in range (0,x+1):
#                 z +=' * '
#             z += '\n'
# print(z)

# z=''
# for x in range (0,10):
#     for y in range(0,21):
#         if y >= 10-x and y <= 10+x:
#             z +=' * '
#         else:
#             z +=' - '
#     z +='\n'
# print(z)

# z=''
# for x in range (10,-1,-1):
#     for y in range (0,21):
#         if y >=10-x and y <= 10+x:
#             z +=' * '
#         else:
#             z +='   '
#     z +='\n'
# print(z)

# z=''
# for x in range (0,10):
#     for y in range (0,21):
#         if y >=10-x and y <=10+x:
#             z +=' * '
#         else:
#             z +='   '
#     z +='\n'
# for x in range (10,-1,-1):
#     for y in range (0,21):
#         if y >=10-x and y <=10+x:
#             z +=' * '
#         else:
#             z +='   '
#     z +='\n'
# print(z)

# list=[40,100,1,5,25,10]
# def asscending(x):
#     for x in range (len(list)):
#         for y in range(x+1,(len(list))):
#             if list [x] > list [y]:
#                 list [x], list [y] = list[y], list [x]
#     return list
# print(asscending(list))

# list=[40,100,1,5,25,10]
# def descending(x):
#     for x in range (len(list)):
#         for y in range(x+1, len(list)):
#             if list [x] < list [y]:
#                 list [x], list [y]= list [y], list[x]
#     return list
# print(descending(list))
# print('nilai tertinggi: ' + str(list[0]))
# print('nilai terendah: ' + str(list[5]))

# ##bikin menu array
# def asscending(arr):
#     for i in range (len(arr)):
#         for j in range (i+1,len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j]= arr[j], arr[i]
#     return arr

# def descending(arr):
#     for i in range (len(arr)):
#         for j in range (i+1,len(arr)):
#             if arr[i] < arr[j]:
#                 arr[i], arr[j]= arr[j], arr[i]
#     return arr

# def minmax(list):
#     angka_min = asscending(list)[0]
#     angka_max = descending(list)[0]
#     return print('nilai tertinggi {} dan nilai terendah {}'.format(angka_max,angka_min))

# def odd_even(list):
#     genap = 0
#     ganjil = 0
#     for i in list:
#         if i % 2 == 0:
#             genap += 1
#         else:
#             ganjil += 1
#     return print ('jumlah angka ganjil {} dan angka genap {}' .format(ganjil,genap))   

# def insert_word(list):
#     jumlah=int(input('Masukkan angka berapa kali: '))
#     for i in range (jumlah):
#         a = int(input('Masukkan angka: '))
#         list.append(a)

# def menuarray():
#     x = []
#     pilihan = 1
#     while (pilihan < 6):
#         print('Main menu \n')
#         print ('1. Isi Array' + '\n' + '2. Lihat Array' + '\n' + '3. Sort Array' + '\n' + '4. Nilai Tertinggi dan Nilai Terendah' 
#             + '\n' + '5. Jumlah Ganjil dan Genap' + '\n' + '6. Keluar')

#         pilihan = int(input('Pilih yang mana: '))

#         if (pilihan == 1):
#             jumlah = int(input('Berapa kali masukkan angka: '))
#             for i in range (jumlah):
#                 a = int(input('Masukkan angka: '))
#                 x.append(a)
        
#         if (pilihan == 2):
#             print(x)
        
#         if (pilihan == 3):
#             c=int(input('1. Asscending' + '\n' + '2. Descending'+ '\n' + 'Pilih yang mana: '))
#             if (c == 2):
#                 descending(x)
#             elif (c == 1):
#                 asscending(x)
#             else:
#                 print('invalid input, coba lagi')
#                 pilihan = 1
        
#         if (pilihan == 4):
#             minmax(x)

#         if (pilihan == 5):
#             odd_even(x)

#         if (pilihan == 6):
#             print('Terimakasih')

#         if (pilihan <=0 or pilihan > 6):
#             print('Invalid input, coba lagi')
#             pilihan = 1
# menuarray()    

# list1 = ['merdeka','Hello','Hellos','kari ayam']
# list2 = []
# inputx=str(input('input kosa kata: '))

# for a in range(len(list1)):
#     if inputx in list1[a].lower():
#         list2.append(list1[a])

# print(list2)

##soal ujian1
# def calculate_years(principal, interest, tax, desired):
#     p = principal
#     i = interest
#     t = tax 
#     d = desired
#     years = 0

#     while p < d:
#         p += (p*i)*(1-t)
#         years += 1
#         return print(years)

# calculate_years(1000.00,0.05,0.18,1100.00)
# calculate_years(1200.00,0.17,0.06,2000.00)
# calculate_years(1500.00,0.07,0.6,5000.00)

# def expanded(num):
#     y = str(num)
#     a = []
#     b = []
#     c = []
#     d = ''

#     for loop in range (len(y)):
#         a.append(y[loop])
#     for loop1 in range (len(y)-1,-1,-1):
#         b.append(10*loop1)
#     for loop2 in range (len(a)):
#         c.append(int(a[loop2])*b[loop2])
#     for loop3 in range (len(c)):
#         if c [loop3] != 0:
#             if [loop3] == 0:
#                 d += str(c[loop3])
#             else:
#                 d += ' + ' + str(c[loop3])
#     return print(d)
# expanded(12)
# expanded(42)
# expanded(70304)

# 3
# def tower_builder (n_floor, block_size):
#     w, h = block_size
#     z = ''
#     for loop1 in range (n_floor):
#         for loop2 in range(h):
#             for loop3 in range (((n_floor-1)*2)-(loop1*2)):
#                 z += ' '
#             for loop4 in range (w+(loop1*4)):
#                 z += '*'
#             z += '\n'
#     return print(z)

# tower_builder(3,(2,3))
# tower_builder(6,(2,1))


##soal coding challenge
def find_sort(s):
    y = s.split()
    panjang=[]
    for item in y :
        panjang.append(len(item))
    panjang.sort()
    return print(panjang[0])
find_sort("many people get up early in the morning")
find_sort("Every office would getting newest monitor")
find_sort("Create new file after this morning")
    
        

