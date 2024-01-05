import random

# Fungsi untuk membaca data pengguna dari file database.txt
def baca_database():
    try:
        with open('database.txt', 'r') as file:
            data = [line.strip().split(',') for line in file.readlines()]
        return {username: password for username, password in data}
    except FileNotFoundError:
        return {}

# Fungsi untuk menulis data pengguna ke dalam file database.txt
def tulis_database(data):
    with open('database.txt', 'w') as file:
        for username, password in data.items():
            file.write(f'{username},{password}\n')

# Fungsi untuk mengecek apakah username sudah terdaftar
def cek_pengguna(username, password):
    data_pengguna = baca_database()
    return username in data_pengguna and data_pengguna[username] == password

# Fungsi untuk mendaftarkan pengguna baru
def daftar_pengguna(username, password):
    data_pengguna = baca_database()
    data_pengguna[username] = password
    tulis_database(data_pengguna)

# Fungsi untuk menghitung total bayar dengan diskon dan biaya tambahan
def hitung_total_bayar(jenis_laundry, berat, punya_voucher, metode_pengiriman):
    harga_laundry = {'cuci': 7000, 'setrika': 10000, 'cuci_setrika': 17000}
    diskon_berat = 0.02 if berat > 5 else 0
    diskon_voucher = 0.05 if punya_voucher else 0
    biaya_pengiriman = {'dalam_kota': 10000, 'luar_kota': 20000, 'ambil_sendiri': 0}

    total_bayar = harga_laundry[jenis_laundry] * berat
    total_bayar *= (1 - diskon_berat)
    total_bayar *= (1 - diskon_voucher)
    total_bayar += biaya_pengiriman[metode_pengiriman]

    return total_bayar

# Fungsi untuk mencetak bukti bayar
def cetak_bukti_bayar(username, jenis_laundry, berat, punya_voucher, metode_pengiriman, metode_pembayaran, total_bayar):
    no_transaksi = random.randint(10000, 99999)
    print("===== Bukti Bayar =====")
    print(f"No. Transaksi: {no_transaksi}")
    print(f"Username: {username}")
    print(f"Jenis Laundry: {jenis_laundry}")
    print(f"Berat Laundry: {berat} kg")
    print(f"Punya Voucher: {'Ya' if punya_voucher else 'Tidak'}")
    print(f"Metode Pengiriman: {metode_pengiriman}")
    print(f"Metode Pembayaran: {metode_pembayaran}")
    print(f"Total Bayar: Rp {total_bayar}")
    print("=======================")

# Fungsi untuk menampilkan menu utama
def menu_utama():
    print("===== Menu Utama =====")
    print("1. Cuci")
    print("2. Setrika")
    print("3. Cuci dan Setrika")
    print("=======================")

# Fungsi untuk menampilkan metode pengiriman
def pilih_metode_pengiriman():
    print("===== Metode Pengiriman =====")
    print("1. Dalam Kota (+Rp 10,000)")
    print("2. Luar Kota (+Rp 20,000)")
    print("3. Ambil Sendiri (Tanpa Biaya Tambahan)")
    print("=============================")

# Fungsi untuk menampilkan metode pembayaran
def pilih_metode_pembayaran():
    print("===== Metode Pembayaran =====")
    print("1. DANA")
    print("2. Cash")
    print("3. Transfer Bank")
    print("=============================")

# Fungsi untuk menampilkan pesan akhir
def pesan_akhir():
    print("Pesanan Anda sedang dibuat.")
    print("Terima kasih sudah mengunjungi aplikasi laundry olala.")
    print("Program selesai.")

# Fungsi utama
def main():
    data_pengguna = baca_database()

    while True:
        print("===== Selamat Datang di Laundry Olala =====")
        print("1. Login")
        print("2. Daftar")
        print("3. Keluar")
        pilihan_login = input("Pilih menu: ")

        if pilihan_login == '1':
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            if cek_pengguna(username, password):
                print("Login berhasil!")
                break
            else:
                print("Login gagal. Silakan coba lagi.")
        elif pilihan_login == '2':
            username = input("Masukkan username baru: ")
            password = input("Masukkan password baru: ")
            daftar_pengguna(username, password)
            print("Pendaftaran berhasil. Silakan login.")
        elif pilihan_login == '3':
            print("Terima kasih. Sampai jumpa!")
            return
        else:
            print("Pilihan tidak valid. Silakan pilih menu 1, 2, atau 3.")

    while True:
        menu_utama()
        pilihan_menu = input("Pilih jenis laundry (1-3): ")

        if pilihan_menu in ['1', '2', '3']:
            jenis_laundry = {'1': 'cuci', '2': 'setrika', '3': 'cuci_setrika'}[pilihan_menu]
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
            continue

        berat = float(input("Masukkan berat laundry (kg): "))
        punya_voucher = input("Apakah Anda punya voucher? (ya/tidak): ").lower() == 'ya'

        pilih_metode_pengiriman()
        pilihan_pengiriman = input("Pilih metode pengiriman (1-3): ")
        metode_pengiriman = {'1': 'dalam_kota', '2': 'luar_kota', '3': 'ambil_sendiri'}[pilihan_pengiriman]

        total_bayar = hitung_total_bayar(jenis_laundry, berat, punya_voucher, metode_pengiriman)

        pilih_metode_pembayaran()
        pilihan_pembayaran = input("Pilih metode pembayaran (1-3): ")
        metode_pembayaran = {'1': 'DANA', '2': 'Cash', '3': 'Transfer Bank'}[pilihan_pembayaran]

        cetak_bukti_bayar(username, jenis_laundry, berat, punya_voucher, metode_pengiriman, metode_pembayaran, total_bayar)

        print("\n===== Struk Pembayaran =====")
        print(f"Jenis Laundry: {jenis_laundry}")
        print(f"Berat Laundry: {berat} kg")
        print(f"Punya Voucher: {'Ya' if punya_voucher else 'Tidak'}")
        print(f"Metode Pengiriman: {metode_pengiriman}")
        print(f"Metode Pembayaran: {metode_pembayaran}")
        print(f"Total Bayar: Rp {total_bayar}")
        print("============================")

        pesan_akhir()
        break

if __name__ == "__main__":
    main()
