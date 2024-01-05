import hashlib #untuk enskripsi password
import random #untuk membuat angka acak nomor pesanan
import string

# Fungsi untuk membaca data pengguna dari file database.txt
def read_user_data():
    try:
        with open('database.txt', 'r') as file:
            lines = file.readlines()
            user_data = {line.strip().split(',')[0]: line.strip().split(',')[1] for line in lines}
            return user_data
    except FileNotFoundError:
        return {}

# Fungsi untuk menulis data pengguna ke file database.txt
def write_user_data(user_data):
    with open('database.txt', 'w') as file:
        for username, password in user_data.items():
            file.write(f'{username},{password}\n')

# Fungsi untuk signup
def signup():
    print("==========================================")
    print("  silahkan buat akun terlebih dahulu (❁´◡`❁)   ")
    print("==========================================")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    user_data = read_user_data()
    if username in user_data:
        print("Username sudah digunakan. Silakan coba dengan username lain.")
    else:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user_data[username] = hashed_password
        write_user_data(user_data)
        print("Pendaftaran berhasil. Silakan login.")
        print("--------------------------------------------------")

# Fungsi untuk login
def login():
    print("==========================================")
    print("   silahkan log in terlebih dahulu (❁´◡`❁)    ")
    print("==========================================")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    user_data = read_user_data()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username in user_data and user_data[username] == hashed_password:
        print("Login berhasil. Selamat datang di warung BuPen, {}!".format(username))
        print("===================================================")
        return True
    else:
        print("Login gagal. Silakan coba lagi atau lakukan pendaftaran.")
        print("===================================================")
        return False

# Fungsi untuk generate kode transaksi
def generate_transaction_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) #merepresentasikan huruf besar ascii dan angka, dan K adalah panjang kode

# Fungsi untuk menampilkan menu utama
def show_main_menu():
    print("apakah anda ingin laundry?")
    
def laundry():
    print("\nMenu Laundry:")
    print("1. Cuci - Harga: 7000")
    print("2. setrika - Harga: 10000")
    print("3. cuci + setrika - Harga: 17000")

# Fungsi untuk menambahkan item ke keranjang Laundry
def add_to_cart(item_name, item_price, quantity):
    cart.append({'name': item_name, 'price': item_price, 'quantity': quantity})

# Fungsi untuk menampilkan keranjang Laundry
def show_cart():
    print("============================================")
    print("\nLaundry Anda:")
    total_price = 0
    for item in cart:
        subtotal = item['price'] * item['quantity']
        total_price += subtotal
        print(f"{item['name']} - {item['quantity']} x {item['price']} = {subtotal}")
    return total_price

# Fungsi untuk memproses metode pembayaran
def process_payment(total_price, delivery_fee):
    print("===============================================")
    print("\nMetode Pembayaran:")
    print("1. Cash")
    print("2. Dana")
    print("3. Transfer Bank")
    print("===============================================")

    payment_method = input("Pilih metode pembayaran (1/2/3): ")
    voucher = input("apakah anda mempunyai member?(y/n): ")
    
    if voucher == "y":
        total_price = (total_price * 0.5) - total_price
    elif voucher == "n":
        buat = input()

    if payment_method in ('1', '2', '3'):
        if total_price > 200000:
            discount = total_price * 0.05
            total_price -= discount

       
        print("\nTotal Pembayaran (termasuk biaya tambahan):", total_price + delivery_fee)
    else:
        print("---------------------------------------------------------------")
        print("Metode pembayaran tidak valid. Silakan coba lagi.")

# Fungsi utama untuk pemesanan
def main():
    global cart
    print("===================================================")
    print("Selamat datang di Angkringan BuPen!, silahkan pilih")

    while True:
        print("\nMenu:")
        print("1. Login")
        print("2. Signup")
        print("3. Keluar")
        choice = input("Pilih menu (1/2/3): ")
        print("--------------------------------------------------")

        if choice == '1':
            if login():
                break
        elif choice == '2':
            signup()
        elif choice == '3':
            print("Terima kasih telah berkunjung!")
            print("===================================================")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            print("===================================================")

    cart = []
    while True:
        show_main_menu()
        choice = input("Pilih jenis menu (1/2): ")
        print("--------------------------------------------------")

        if choice == 'y':  # Makanan
            laundry()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            print("--------------------------------------------------")
            continue

        item_id = input("Pilih nomor menu: ")
        item_quantity = int(input("Masukkan berapa Kg: "))

        if choice == '1':  # Makanan
            if item_id in ('1', '2', '3'):
                _name = menu_items[int(item_id) - 1]['name']
                _price = menu_items[int(item_id) - 1]['price']
                add_to_cart(_name, _price, item_quantity)
            else:
                print("Menu tidak valid. Silakan coba lagi.")
                continue

        add_more = input("Apakah Anda ingin menambah pesanan lagi? (y/n): ")
        print("--------------------------------------------------")
        if add_more.lower() != 'y':
            break

    delivery_option = input("Mau dimakan dimana? (1. Dine in / 2. Delivery): ")
    delivery_fee = 0

    if delivery_option == '2':  # Delivery
        location = input("Pilih lokasi pengantaran (1. Dalam kota / 2. Luar kota): ")
        print("--------------------------------------------------")
        if location == '1':
            delivery_fee = 10000
        elif location == '2':
            delivery_fee = 20000
        else:
            print("Pilihan lokasi tidak valid. Pengantaran dianggap dalam kota.")

    total_price = show_cart()
    process_payment(total_price, delivery_fee)

    order_again = input("buat pesanan? (y/n): ")
    if order_again.lower() != 'y':
        print("\nTerimakasih sudah berkunjung di aplikasi BuPen.")
        exit()

    transaction_code = generate_transaction_code()
    print("\nTerima kasih telah memesan di Angkringan BuPen!")
    print("Pesanan Anda sedang diproses. Mohon tunggu.")
    print("--- Struk Pembayaran ---")
    print("Kode Transaksi: {}".format(transaction_code))
    show_cart()
    print("Total Pembayaran: {}".format(total_price + delivery_fee))
    print("Metode Pengantaran: {}".format("Dine in" if delivery_option == '1' else "Delivery"))
    print("Terima kasih sudah memesan di Angkringan BuPen. Selamat menikmati!")

# Menjalankan program utama
if __name__ == "__main__":
    menu_items = [
        {'id': 1, 'name': 'Bubur Ayam', 'price': 6000},
        {'id': 2, 'name': 'Bubur Pentol', 'price': 6000},
        {'id': 3, 'name': 'Bubur Jamur', 'price': 7000},
        {'id': 4, 'name': 'Es Teh', 'price': 2500},
        {'id': 5, 'name': 'Es Kopi', 'price': 2500},
    ]

    cart = []
    main()