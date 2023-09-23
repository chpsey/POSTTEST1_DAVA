# Terdapat Comment di setiap baris untuk penjelasan program dan dibawah program terdapat alur lengkap program

# PROGRAM KONVERSI NILAI TUKAR RUPIAH KE MATA UANG USD, YEN, DAN MYR
# Informasi login pengguna
username = "dapa"         # Username adalah nama pembuat program
nim      = "2309116059"   # NIM adalah NIM pembuat program
password = "123"          # Password adalah 123 untuk mempermudah mengingat password

def login():    # Function login
                # Meminta input username dan password dari pengguna
    input_username = input("Masukkan username: ") # Input username harus Nama pembuat program (dapa)
    input_nim      = input("Masukkan NIM: ")      # Input NIM harus NIM dari pembuat program (2309116059)
    input_password = input("Masukkan password: ") # Input password harus 123 untuk mempermudah mengingat password
    

    # Memeriksa kecocokan username dan password
    if input_username == username and input_password == password and nim == input_nim:
        return True     # Ketika username dan password benar maka login berhasil dan lanjut ke program konversi
    else:
        return False    # Ketika username dan password salah maka login gagal dan langsung menuju akhir program

def idr_to_usd(idr):    # Function konversi Rupiah ke USD
    # Mengkonversi Rupiah ke USD sesuai nilai tukar Rupiah
    usd = idr / 15357   # Nilai usd to rupiah pada 23/09/2023 adalah Rp. 15.357,05 dan digenapkan menjadi Rp15.357
    return usd

def idr_to_yen(idr):    # Function konversi Rupiah ke Yen
    # Mengkonversi Rupiah ke Yen sesuai nilai tukar Rupiah
    yen = idr / 103     # Nilai Yen to rupiah pada 23/09/2023 adalah Rp. 103,56 dan digenapkan menjadi Rp103
    return yen

def idr_to_myr(idr):    # Function konversi Rupiah ke MYR
    # Mengkonversi Rupiah ke Ringgit Malaysia sesuai nilai tukar Rupiah
    myr = idr / 3273    # nilai myr to rupiah pada 23/09/2023 adalah Rp. 3.273,38 dan digenapkan menjadi Rp3.273
    return myr

# Tampilan ketika pengguna berhasil login
if login():
    print("Login berhasil!")
    print(f"Selamat Datang {username} :)")     # Ucapan selamat datang kepada pengguna sesuai data yang pengguna input
    print("Pilih opsi konversi mata uang:")    # Pengguna memilih mata uang tujuan yang ingin dikonversi dari Rupiah
    print("1. IDR ke USD")
    print("2. IDR ke Yen")
    print("3. IDR ke MYR")

    # Meminta pengguna untuk memilih opsi. Pengguna harus memilih opsi diantara 1-3, jika salah maka akan menuju akhir program.
    opsi = input("Masukkan nomor opsi (1-3): ")       # Pengguna memilih opsi untuk konversi rupiah ke mata uang lain.

    if opsi == "1":
        idr = float(input("Masukkan jumlah IDR: "))   # Pengguna menginput jumlah Rupiah yang ingin di konversi
        usd = idr_to_usd(idr)                         # Operasi konversi dari function idr_to_usd utk konversi
        print(f"Hasil konversi: {usd} $ (USD)")       # Output hasil dari konversi Rupiah ke USD


    elif opsi == "2":
        idr = float(input("Masukkan jumlah IDR: "))   # Pengguna menginput jumlah Rupiah yang ingin di konversi
        yen = idr_to_yen(idr)                         # Operasi konversi dari function idr_to_yen utk konversi
        print(f"Hasil konversi: {yen} ¥ (Yen)")       # Output hasil dari konversi Rupiah ke Yen

    elif opsi == "3":
        idr = float(input("Masukkan jumlah IDR: "))   # Pengguna menginput jumlah Rupiah yang ingin di konversi
        myr = idr_to_myr(idr)                         # Operasi konversi dari function idr_to_myr utk konversi 
        print(f"Hasil konversi: {myr} RM (MYR)")      # Output hasil dari konversi Rupiah ke MYR

    else:
        print("Opsi yang dimasukkan tidak valid!") # Ketika pengguna tidak memasukkan input opsi diantara 1-3 maka akan langsung menuju akhir dari program.

else:
    print("Login gagal! Silakan coba lagi.") # Ketika Username dan Password tidak sesuai dengan ketentuan maka pengguna akan langsung menuju akhir dari program.


"""
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
"""