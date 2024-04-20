pembeli = input ("Input Nama Pembeli :")
no_hp = input ("Input No. HP :")
jurusan = input ("Input Jurusan [SBY/BL/LMP] : ")

if jurusan=="SBY" :
    namajurusan = "Surabaya"
    harga = 300000
elif jurusan=="BL" :
    namajurusan = "Bali"
    harga = 350000
else :
    namajurusan="Lampung"
    harga = 500000
jumlah=int (input("Masukan Jumlah Beli :"))
if jumlah>=3 :
    potongan=(jumlah*harga)*0.1
else:
    potongan=0
total=(jumlah*harga)-potongan
#output
print ("----------------------------------------")
print ("         ""PENJUALAN TIKET BUS")
print ("                ""XYZ")
print ("----------------------------------------")
print ("Nama Pembeli"            ": "+str (pembeli))
print ("No. Handphone "          ":"+str(no_hp))
print ("Kode Jurusan yang dipilih :"+str(jurusan))
print ("Nama Kota Tujuan "       ":"+str (namajurusan))
print ("harga"                   ":"+str(harga))
print ("Jumlah Beli"             ":"+str(jumlah))
print ("-----------------------------------------")
print ("Potongan yang didapat :"+str(potongan))
print ("Total Bayar :"+str(total))
ubay = int(input("Masukan Uang Bayar :"))
uangkembali = ubay-total
print ("Uang Kembali :",+uangkembali)