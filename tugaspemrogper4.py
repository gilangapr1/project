print ("PROGRAM HITUNG GAJI KARYAWAN")
namaKaryawan = input ("Nama Karyawan:")
golonganJabatan = input("Golongan Jabatan [1/2/3]:")
pendidikan = input ("Pendidikan [SMA/D1/D3/S1]:")
jumlahJamkerja = int (input ("Jumlah Jam Kerja:"))

#input perhitungan
gaji = 300000
#tunjangan karyawan
if golonganJabatan=="1" :
    tunjangan = gaji * 0.05
elif golonganJabatan=="2" :
    tunjangan = gaji * 0.1
else :
    tunjangan = gaji * 0.15
#tunjangan pendidikan
if pendidikan=="SMA" :
    tunjanganPendidikan = gaji * 0.25
elif pendidikan=="D1" :
    tunjanganPendidikan = gaji * 0.5
elif pendidikan=="D3" :
    tunjanganPendidikan = gaji * 2.0
else :
    tunjanganPendidikan = gaji * 3.0
#lembur
if  jumlahJamkerja > 8 :
    lembur = (jumlahJamkerja - 8) * 3500
else :
    lembur = 0
#output keluaran
print ("Karyawan yang bernama:"+str (namaKaryawan))
print ("Honor yang diterima")
print ("Tunjangan Jabatan Rp "+str (tunjangan))
print ("Tunjangan Pendidikan Rp "+str (tunjanganPendidikan))
print ("Honor Lembur Rp "+str(lembur))
totalGaji =gaji+tunjangan+tunjanganPendidikan+lembur
print ("Total Gaji Rp "+str (totalGaji ))