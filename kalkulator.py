# kalkulator sederhana
import os

def header():
    '''header'''
    os.system("cls")    
    print("-"*40)
    print(f"{'KALKULATOR':^40}")
    print(f"{'SEDERHANA':^40}")
    print("-"*40)

def looping(list_operasi):
    '''perulangan'''
    for operasi in list_operasi:
        print(f"{operasi}")
isi = ["1.tambahan\t[+]","2.kurangan\t[-]","3.kalian\t[*]","4.bagian\t[/]"]

def input_user():
    '''inpur user'''
    bilangan1 = int(input("masukan angka1 : "))
    bilangan2 = int(input("masukan angka2 : "))
    return bilangan1,bilangan2

def tambahan(bilangan1,bilangan2):
    '''tambahan'''
    return bilangan1 + bilangan2

def kurang(bilangan1,bilangan2):
    '''kurangan'''
    return bilangan1 - bilangan2

def kali(bilangan1,bilangan2):
    '''kalian'''
    return bilangan1 * bilangan2

def bagi(bilangan1,bilangan2):
    '''bagian'''
    return bilangan1 / bilangan2

while True:
    header()
    looping(isi)
    print("-"*40)
    ANGKA1,ANGKA2 = input_user()
    print("-"*40)
    opsi = int(input("pilih operasi yang mau dijalankan (1/2/3/4) : "))
    if opsi == 1:
        TAMBAH = tambahan(ANGKA1,ANGKA2)
        print(F"kamu memilih tambahan, hasilnya = {TAMBAH}")
    elif opsi == 2:
        KURANG = kurang(ANGKA1,ANGKA2)
        print(f"kamu memilih kurangan, hasilnya = {KURANG}")
    elif opsi == 3:
        KALI = kali(ANGKA1,ANGKA2)
        print(f"kamu memilih kalian, hasilnya = {KALI}")
    elif opsi == 4:
        BAGI = bagi(ANGKA1,ANGKA2)
        print(f"kamu memilih bagian, hasilnya {BAGI}")
    
    isContinue = input("apakah mau dilanjutin (y/n) ? ")
    if isContinue == "n":
        break

    print("-"*40)
print("-"*40)
print("PROGRAM BERAKHIR")
print("-"*40)
