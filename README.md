# POSTTEST1_DAVA
POST TEST 1 (PRAKTIKUM) MUHAMMAD ARIFIN DAVA 2309116059- SISTEM INFORMASI-B 23

Muhammad Arifin Dava
2309116059
Sistem Informasi-B
Flowchart dari program :
![image](https://github.com/chpsey/POSTTEST1_DAVA/assets/144978229/07198246-6648-415b-8053-b71be70a026a)

Screenshot output dari program :
![image](https://github.com/chpsey/POSTTEST1_DAVA/assets/144978229/b843dbca-f5d6-461f-abf0-a82e5c855d5b)

note : comment pada program sudah sangat lengkap di tiap baris disertai penjelasan tentang fungsi dari setiap baris didalam program

PENJELASAN LENGKAP PROGRAM :
Program Python dengan fitur login dan konversi nilai tukar mata uang dari Rupiah ke Mata Uang USD, Yen, dan MYR. 
Berikut penjelasan program:

1. Program dimulai dengan definisi informasi login pengguna, termasuk username, password, dan nim.

2. Fungsi login() digunakan untuk memeriksa login pengguna. Pengguna diminta untuk memasukkan username, password, dan nim. Fungsi ini memeriksa apakah input pengguna cocok dengan data yang telah ditentukan. Jika cocok, fungsi mengembalikan True dan pengguna diizinkan untuk mengakses fitur konversi mata uang. Jika tidak cocok, maka akan mengembalikan False dan program akan berakhir.

3. Terdapat tiga fungsi konversi mata uang: idr_to_usd(), idr_to_yen(), dan idr_to_myr(). Setiap fungsi ini mengambil jumlah Rupiah sebagai parameter dan mengembalikan hasil konversi ke mata uang asing (USD, Yen, atau MYR).

4. Jika login berhasil, program mencetak pesan "Login berhasil!" dan menyambut pengguna dengan nama yang sesuai dengan username. Selanjutnya, program meminta pengguna untuk memilih opsi konversi mata uang.

5. Pengguna memilih opsi dengan memasukkan nomor (1, 2, atau 3) yang sesuai dengan mata uang yang ingin dikonversi.

6. Berdasarkan pilihan pengguna, program akan meminta pengguna memasukkan jumlah Rupiah yang ingin dikonversi.

7. Setelah input jumlah Rupiah, program memanggil salah satu fungsi konversi mata uang yang sesuai, yaitu idr_to_usd(), idr_to_yen(), atau idr_to_myr(), dan mencetak hasil konversi ke mata uang yang dipilih oleh pengguna.

8. Jika pengguna memasukkan opsi yang tidak valid, program mencetak pesan "Opsi yang dimasukkan tidak valid!".

9. Jika login gagal (username, password, atau nim tidak cocok), program mencetak pesan "Login gagal! Silakan coba lagi." dan berakhir.

Program ini memberikan pengguna kemampuan untuk melakukan login, memilih mata uang tujuan, dan melakukan konversi nilai tukar dari Rupiah ke mata uang lainnya. Setiap bagian program memiliki comment sebagai penjelasan yang rinci untuk membantu pengguna memahami alur kerja program


PENJELASAN LENGKAP OUTPUT :
![image](https://github.com/chpsey/POSTTEST1_DAVA/assets/144978229/1d13b003-b7a1-4361-bb9f-ec0b5f881cd6)
ketika user menginput data nama nim atauapun password dengan salah, maka akan muncul output "Login gagal! Silakan coba lagi."... dan langsung mengarahkan user ke akhir program

![image](https://github.com/chpsey/POSTTEST1_DAVA/assets/144978229/edfa32be-b526-43e1-a580-46011fc75d85)
Ketika user menginput data nama nim password dengan benar, maka akan muncul output print "Login berhasil!", "selamat datang" (username).. dan juga output print untuk meminta user memilih opsi konservi mata uang yang akan dituju
user dapat memilih angka (1/2/3) sesuai petunjuk
untuk angka 1 dari IDR ke USD
untuk angka 2 dari IDR ke Yen
untuk angka 3 dari IDR ke MYR
kemudian program meminta user untuk memasukkan jumlah IDR dalam rupiah
selanjutnya akan tampil output hasil konversi yang sesuai dengan mata uang pilihan.

note : ketika user memilih angka selain 1/2/3 ataupun menginput yang tidak sesuai, akan tampil "opsi yang dimasukkan tidak valid" seperti contoh berikut :
![image](https://github.com/chpsey/POSTTEST1_DAVA/assets/144978229/d1ab8827-9160-4162-b00a-d072e887ddb8)

berikut contoh program yang berhasil berjalan dari IDR to USD
![image](https://github.com/chpsey/POSTTEST1_DAVA/assets/144978229/a07b4f36-024c-4b59-8f33-7b971a993f43)

berikut contoh program yang berhasil berjalan dari IDR to Yen
![image](https://github.com/chpsey/POSTTEST1_DAVA/assets/144978229/2750388a-368d-450d-b5b3-e85db0fe683c)

berikut contoh program yang berhasil berjalan dari IDR to MYR
![image](https://github.com/chpsey/POSTTEST1_DAVA/assets/144978229/3b9d43ef-641c-4838-ab4e-959b78a5bb6a)

Nilai mata uang yang dikonversi pada program ini mengikuti waktu saya saat membuat program yaitu 23/09/2023... nilai mata uang pasti berubah sewaktu-waktu sehingga perlu adanya update berkala jika ingin digunakan untuk seterusnya.








