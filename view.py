from modul import lingkaran, segitiga

cek = input("pilih lingkaran/segitiga (1/2)")

if cek == "1":
    valueBulat = int(input("masukan jari-jari : "))
    lingkaran(valueBulat)
elif cek== "2":
    vsegitga1 = int(input("masukan alas : "))
    vsegitga2 = int(input("masukan tinggi : "))
    segitiga(vsegitga1,vsegitga2)