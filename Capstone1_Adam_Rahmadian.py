from tabulate import tabulate
import maskpass
import sys
from datetime import datetime

## 0: Nama - 1: Stock - 2: Harga - 3: Merek
smartphones = [
    ["Iphone 13 Pro Sierra Blue", 3, 15000000, "Apple"],
    ["Iphone 13 Pro Graphite", 5, 15000000, "Apple"],
    ["Samsung Galaxy S21 Phantom Gray", 7, 12000000, "Samsung"],
    ["Iphone 11 Black", 10, 8000000, "Apple"],
    ["Samsung Galaxy S23 Lavender", 8, 2300000, "Samsung"],
    ["Samsung Flip 6 Green", 5, 7000000, "Samsung"],
    ["Iphone 15 Pro Max Space Black", 5, 25000000, "Apple"],
    ["Iphone XR Coral", 11, 3500000, "Apple"],
    ["Google Pixel 7 Pro Hazel", 6, 9000000, "Google"],
    ["Google Pixel 6a Sage", 8, 5500000, "Google"],
    ["Xiaomi 12 Pro Gray", 9, 11000000, "Xiaomi"],
    ["Xiaomi Redmi Note 12 Blue", 15, 4000000, "Xiaomi"]
]

def tampilkan_smartphone():
    print("\nBerikut Merupakan Daftar Smartphone yang Tersedia: ")
    headers=["Nomor", "Nama", "Stok", "Harga", "Merek"]
    data = []
    for i in range(len(smartphones)):
        smartphone = smartphones[i]
        data.append([i + 1, smartphone[0], smartphone[1], f"Rp.{smartphone[2]:,}", smartphone[3]])
    print(tabulate(data, headers, tablefmt="simple_grid", colalign=("center", "left", "center", "left", "left")))

def lihat_detail_smartphones():
    tampilkan_smartphone()
    while True:
        nama_detail = input("Masukkan nama smartphone yang ingin dilihat detail: ").strip().lower()
        if not nama_detail:
            print("\nNama tidak boleh kosong. Silakan masukkan nama yang valid.")
            continue

        index_update = None
        for i in range(len(smartphones)):
            if smartphones[i][0].lower() == nama_detail:
                index_update = i
                break

        if index_update is not None: 
            break
        else:
            print("\nNama smartphone tidak ditemukan. Silakan masukkan nama yang sesuai.")
            
    smartphone = smartphones[index_update]
    headers = ["Nomor", "Nama", "Stok", "Harga", "Merek"]
    data = [[index_update + 1, smartphone[0], smartphone[1], f"Rp.{smartphone[2]:,}", smartphone[3]]]  # Menambahkan +1 untuk nomor
    print(tabulate(data, headers, tablefmt="simple_grid", colalign=("center", "left", "center", "right", "left")))

    back()

def tambah_smartphone():
    print('\nApakah Anda Yakin Ingin Menambah?')
    while True:
        konfirmasi_awal = input('\nMasukkan Angka (1) untuk ya, (2) untuk tidak: ')
        if konfirmasi_awal == '1':  
            break
        elif konfirmasi_awal == '2': 
            print("\nKembali ke menu utama.")
            return
        else:
            print("\nInput tidak valid. Silakan masukkan angka (1/2).")

    while True:
        nama_baru = input("\nMasukkan nama smartphone: ").strip()
        if not nama_baru:
            print("Nama tidak boleh kosong. Silakan masukkan nama yang valid.")
        elif any(i[0].lower() == nama_baru.lower() for i in smartphones):
            print("Nama yang Anda masukkan sudah ada di daftar. Coba masukkan nama yang berbeda!")
        elif not all(c.isalnum() or c.isspace() for c in nama_baru):
            print("Nama tidak boleh mengandung karakter khusus!")
        else:
            break

    while True:
        try:
            stock_baru = int(input("\nMasukkan stok smartphone: ").strip())
            if stock_baru <= 0:
                print("Stok harus lebih besar dari 0.")
            else:
                break
        except ValueError:
            print("Input tidak valid! Stok harus berupa angka.")

    while True:
        try:
            harga_baru = int(input("\nMasukkan harga smartphone: ").strip())
            if harga_baru <= 0:
                print("Harga harus lebih besar dari 0.")
            else:
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang benar.")


    while True:
        merek_baru = input("\nMasukkan merek smartphone: ").strip()
        if not merek_baru:
            print("Merek tidak boleh kosong. Silakan masukkan merek yang valid.")
        else:
            break

    while True:
        konfirmasi_akhir = input(f"\nApakah Anda yakin ingin menambahkan {nama_baru} ke daftar smartphone? (ya/tidak): ").strip().lower()
        if konfirmasi_akhir == 'ya':
            smartphones.append([nama_baru, stock_baru, harga_baru, merek_baru])
            print(f"\n{nama_baru} berhasil ditambahkan ke daftar smartphone.")
            tampilkan_smartphone()
            return 
        elif konfirmasi_akhir == 'tidak':
            print("\nPenambahan pada daftar smartphone dibatalkan. Kembali ke menu utama.")
            return
        else:
            print("Input salah. Harap masukkan 'ya' atau 'tidak'.")
    
def hapus_smartphone():
    print('\nApakah Anda Yakin Ingin Menghapus?')
    while True:
        konfirmasi_awal = input('\nMasukkan Angka (1) untuk ya, (2) untuk tidak: ')
        if konfirmasi_awal == '1': 
            tampilkan_smartphone()
            while True:
                nama_hapus = input("\nMasukkan nama smartphone yang ingin dihapus (atau ketik 'batal' untuk kembali ke menu utama): ").strip().lower()
        
                if nama_hapus == 'batal':
                    print("\nPenghapusan dibatalkan. Kembali ke menu utama.")
                    return  

                index_hapus = None
                for i in range(len(smartphones)):
                    if smartphones[i][0].lower() == nama_hapus:
                        index_hapus = i
                        break
                if index_hapus is None:
                    print("\nNama smartphone tidak ditemukan. Silakan masukkan nama yang sesuai atau ketik 'batal'.")
                else:
                    while True:
                        konfirmasi = input(f"\nApakah Anda yakin ingin menghapus {smartphones[index_hapus][0]}? (ya/tidak): ").strip().lower()
                        if konfirmasi == 'ya':
                            del smartphones[index_hapus]
                            print("\nSmartphone berhasil dihapus dari daftar.")
                            tampilkan_smartphone() 
                            return  
                        elif konfirmasi == 'tidak':
                            print("\nPenghapusan dibatalkan. Kembali ke menu utama.")
                            return  
                        else:
                            print("\nInput tidak valid. Harap masukkan 'ya' atau 'tidak'.")

        elif konfirmasi_awal == '2':  
            print("\nKembali ke menu utama.")
            return
        else:
            print("\nInput tidak valid. Silakan masukkan angka (1/2).")

def update_smartphone():
    print('\nApakah Anda Yakin Ingin Update?')
    while True:
        konfirmasi_awal = input('\nMasukkan Angka (1) untuk ya, (2) untuk tidak: ')
        if konfirmasi_awal == '1':  
            break
        elif konfirmasi_awal == '2': 
            print("\nKembali ke menu utama.")
            return
        else:
            print("\nInput tidak valid. Silakan masukkan angka (1/2).")

    # Tampilkan daftar smartphone untuk memudahkan pengguna
    tampilkan_smartphone()

    # Pilih smartphone berdasarkan nama
    while True:
        nama_update = input("\nMasukkan nama smartphone yang ingin diupdate (atau ketik 'batal' untuk kembali): ").strip().lower()
        if nama_update == 'batal':
            print("\nUpdate dibatalkan. Kembali ke menu utama.")
            return

        index_update = None
        for i in range(len(smartphones)):
            if smartphones[i][0].lower() == nama_update:
                index_update = i
                break

        if index_update is not None:
            break
        else:
            print("\nNama smartphone tidak ditemukan. Silakan masukkan nama yang sesuai atau ketik 'batal'.")

    # Pilih kolom yang akan di-update
    while True:
        pilih_update = input("\nPilih Kolom yang ingin Anda Update (nama/stok/harga/merek): ").lower()
        if pilih_update not in ['nama', 'stok', 'harga', 'merek']:
            print("\nInput salah! Harap pilih kolom yang benar (nama, stok, harga, merek).")
            continue

        try:
            if pilih_update == 'nama':
                while True:
                    nama_baru = input("\nMasukkan nama baru: ").strip()
                    if not nama_baru:
                        print("Nama tidak boleh kosong. Silakan masukkan nama yang valid.")
                    elif any(i[0].lower() == nama_baru.lower() for i in smartphones):
                        print("Nama sudah ada di daftar. Coba nama lain.")
                    else:
                        konfirmasi = input(f"Apakah Anda yakin ingin mengubah nama menjadi '{nama_baru}'? (ya/tidak): ").lower()
                        if konfirmasi == 'ya':
                            smartphones[index_update][0] = nama_baru
                            print("\nNama smartphone berhasil diperbarui.")
                            tampilkan_smartphone()
                            return
                        elif konfirmasi == 'tidak':
                            print("\nUpdate nama dibatalkan.")
                            return
                        else:
                            print("Input salah. Masukkan 'ya' atau 'tidak'.")
            elif pilih_update == 'stok':
                while True:
                    try:
                        stok_baru = int(input("\nMasukkan stok baru: ").strip())
                        if stok_baru <= 0:
                            print("Stok harus lebih besar dari 0.")
                        else:
                            konfirmasi = input(f"Apakah Anda yakin ingin mengubah stok menjadi {stok_baru}? (ya/tidak): ").lower()
                            if konfirmasi == 'ya':
                                smartphones[index_update][1] = stok_baru
                                print("\nStok smartphone berhasil diperbarui.")
                                tampilkan_smartphone()
                                return
                            elif konfirmasi == 'tidak':
                                print("\nUpdate stok dibatalkan.")
                                return
                            else:
                                print("Input salah. Masukkan 'ya' atau 'tidak'.")
                    except ValueError:
                        print("Input tidak valid! Stok harus berupa angka.")
            elif pilih_update == 'harga':
                while True:
                    try:
                        harga_baru = int(input("\nMasukkan harga baru: ").strip())
                        if harga_baru <= 0:
                            print("Harga harus lebih besar dari 0.")
                        else:
                            konfirmasi = input(f"Apakah Anda yakin ingin mengubah harga menjadi Rp.{harga_baru:,}? (ya/tidak): ").lower()
                            if konfirmasi == 'ya':
                                smartphones[index_update][2] = harga_baru
                                print("\nHarga smartphone berhasil diperbarui.")
                                tampilkan_smartphone()
                                return
                            elif konfirmasi == 'tidak':
                                print("\nUpdate harga dibatalkan.")
                                return
                            else:
                                print("Input salah. Masukkan 'ya' atau 'tidak'.")
                    except ValueError:
                        print("Input tidak valid! Harga harus berupa angka.")
            elif pilih_update == 'merek':
                while True:
                    merek_baru = input("\nMasukkan merek baru: ").strip()
                    if not merek_baru:
                        print("Merek tidak boleh kosong.")
                    elif any(i[3].lower() == merek_baru.lower() for i in smartphones):
                        print("Merek sudah ada di daftar. Coba merek lain.")
                    else:
                        konfirmasi = input(f"Apakah Anda yakin ingin mengubah merek menjadi '{merek_baru}'? (ya/tidak): ").lower()
                        if konfirmasi == 'ya':
                            smartphones[index_update][3] = merek_baru
                            print("\nMerek smartphone berhasil diperbarui.")
                            tampilkan_smartphone()
                            return
                        elif konfirmasi == 'tidak':
                            print("\nUpdate merek dibatalkan.")
                            return
                        else:
                            print("Input salah. Masukkan 'ya' atau 'tidak'.")
        except ValueError:
            print("\nTerjadi kesalahan. Mohon ulangi.")

def beli_smartphone():
    keranjang_belanja = []
    total_harga = 0
    tampilkan_smartphone()

    while True:
        try:
            while True:
                pilihan_beli = input("\nMasukkan nama smartphone yang ingin Anda beli: ").strip().lower()
                index_beli = None

                for i in range(len(smartphones)):
                    if pilihan_beli == smartphones[i][0].lower():
                        index_beli = i
                        break

                if index_beli is not None:
                    break
                else:
                    print("\nNama smartphone tidak ditemukan. Silakan coba lagi!")

            while True:
                try:
                    stok_tersedia = smartphones[index_beli][1]
                    jumlah_beli = int(input(f"\nMasukkan jumlah yang ingin dibeli (Stock tersedia: {stok_tersedia}): "))
                    
                    if 0 < jumlah_beli <= stok_tersedia:
                        harga = jumlah_beli * smartphones[index_beli][2]
                        total_harga += harga
                        
                        keranjang_belanja.append([
                            smartphones[index_beli][0],  # nama hp
                            jumlah_beli,                # jumlah beli
                            harga,                      # harga
                            smartphones[index_beli][3]  # merek
                        ])
                        print(f"\n{jumlah_beli} unit {smartphones[index_beli][0]} berhasil ditambahkan ke keranjang.")
                        break 
                    else:
                        print("\nJumlah yang dimasukkan tidak valid atau melebihi stok yang tersedia.")
                except ValueError:
                    print("\nInput tidak valid. Harap masukkan angka yang benar.")
        
        except ValueError:
            print(f"\nTerjadi kesalahan!")
        
        while True:
            lanjutkan = input("\nApakah Anda ingin menambahkan smartphone lain ke keranjang? (Ya/Tidak): ").strip().lower()
            if lanjutkan == 'ya':
                break
            elif lanjutkan == 'tidak':
                if keranjang_belanja:
                    print('='*58)
                    print("Detail Belanja".center(58))
                    print('='*58)
                    for i in keranjang_belanja:
                        print(f'Nama Smartphone     : {i[0]}')
                        print(f'Merek               : {i[3]}')
                        print(f'Jumlah Pembelian    : {i[1]}')
                        print(f'Harga               : Rp.{i[2]:,}')
                        print('-'*58)
                    while True:
                        print("Total harga untuk semua pembelian adalah Rp.{:,}".format(total_harga))
                        print('='*58)
                        konfirmasi_bayar = input("\nApakah Anda yakin ingin melanjutkan ke pembayaran? (ya/tidak): ").strip().lower()
                        if konfirmasi_bayar == 'ya':
                            while True:
                                try:
                                    setor_uang = int(input("Masukkan jumlah uang yang Anda setorkan: "))
                                    if setor_uang >= total_harga:
                                        cetak_struk(keranjang_belanja, total_harga, setor_uang)
                                        smartphones[index_beli][1] -= jumlah_beli
                                        return 
                                    else:
                                        print(f"\nUang yang Anda setorkan tidak cukup. Uang Anda Kurang Sebesar Rp.{total_harga - setor_uang:,}")
                                except ValueError:
                                    print("\nInput tidak valid. Harap masukkan angka yang benar.")
                                    continue
                        elif konfirmasi_bayar == 'tidak':
                            print("\nPembayaran dibatalkan. Kembali ke menu utama.")
                            return
                        else:
                            print("\nInput tidak valid. Harap masukkan 'ya' atau 'tidak'.")
            else:
                print("\nInput tidak valid. Silakan masukkan 'Ya' atau 'Tidak'.")

def cetak_struk(keranjang_belanja, total_harga, setor_uang):
    print("\n" + "="*47)
    print("STRUK PEMBELIAN".center(47))
    print("="*47)
    print("GROTE CELLULAR INDONESIA".center(47))
    print("-"*47)
    for i in keranjang_belanja:
        print(f"Nama Smartphone   : {i[0]}")
        print(f"Merek Smartphone   : {i[3]}")
        print(f"Jumlah Pembelian  : {i[1]}")
        print(f"Harga             : Rp.{i[2]:,}")
        print("="*47)
    print(f"Total Harga       : Rp.{total_harga:,}")
    print(f"Setor Uang        : Rp.{setor_uang:,}")
    print(f"Kembalian         : Rp.{setor_uang - total_harga:,}")
    print("="*47)
    print("Tanggal Pembelian : ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Terima kasih telah berbelanja!")
    print("="*47)

def sub_menu():
    headers = ["No", "Menu"]
    data = [
        ["1", "Lihat Semua Daftar Smartphone"],
        ["2", "Lihat Detail Smartphone"],
        ["3", "Fitur Sorting Berdasarkan Kolom"],
        ["4", "Kembali Ke Menu Utama"]
    ]
    print(tabulate(data, headers=headers, tablefmt="simple_grid", stralign="left"))  

def bubble_sort(kolom, urutan_sort):
    if kolom not in [0, 1, 2, 3]:
        return

    listSorted = smartphones.copy() # save list asli
    if urutan_sort == "ASC":
        for i in range(len(listSorted)):
            for j in range(0, len(listSorted) - i - 1):
                if listSorted[j][kolom] > listSorted[j + 1][kolom]:
                    listSorted[j], listSorted[j + 1] = listSorted[j + 1], listSorted[j]
    elif urutan_sort == "DESC":
        for i in range(len(listSorted)):
            for j in range(0, len(listSorted) - i - 1):
                if listSorted[j][kolom] < listSorted[j + 1][kolom]:
                    listSorted[j], listSorted[j + 1] = listSorted[j + 1], listSorted[j]

    return listSorted # balikin list asli
                       
def fitur_sorting():
    tampilkan_smartphone()

    print("\nPilih Kolom untuk Sorting:")
    print("\n1. Nama")
    print("\n2. Stok")
    print("\n3. Harga")
    print("\n4. Merek")
    
    while True:
        try:
            pilihan_sort = int(input("\nPilih Kolom untuk Sorting (1-4): "))
            if pilihan_sort not in [1, 2, 3, 4]:
                print("\nInput tidak valid. Masukkan angka 1, 2, 3, atau 4!")
                continue
            
            index_kolom = {1: 0, 2: 1, 3: 2, 4: 3}
            kolom = index_kolom[pilihan_sort]

            while True:
                urutan_sort = input("\nIngin diurutkan secara apa (ASC/DESC)? ").strip().upper()
                if urutan_sort in ["ASC", "DESC"]:
                    sorted_list = bubble_sort(kolom, urutan_sort)
                    print("\nHasil Sorting:")
                    headers = ["Nomor", "Nama", "Stok", "Harga", "Merek"]
                    data = []
                    for i in range(len(smartphones)):
                        data.append([i + 1, sorted_list[i][0], sorted_list[i][1], f"Rp.{sorted_list[i][2]:,}", sorted_list[i][3]])
                    print(tabulate(data, headers=headers, tablefmt="simple_grid", colalign=("center", "left", "center", "left", "left")))
                    back()
                    return
                else:
                    print("\nInput tidak valid. Silakan pilih 'ASC' untuk ascending atau 'DESC' untuk descending!")
        except ValueError:
            print("\nInput tidak valid. Harap masukkan angka 1, 2, 3, atau 4!")                   

def menu_utama_admin():
    headers = ["No", "Deskripsi"]
    data = [
        ["1", "Menampilkan Daftar Smartphone"],
        ["2", "Menambah Smartphone"],
        ["3", "Menghapus Smartphone"],
        ["4", "Mengupdate Smartphone"],
        ["5", "Keluar Program"]
    ]
    print(tabulate(data, headers=headers, tablefmt="simple_grid", colalign=("center", "left")))

def menu_utama_user():
    headers = ["No", "Deskripsi"]
    data = [
        ["1", "Menampilkan Daftar Smartphone"],
        ["2", "Membeli Smartphone"],
        ["3", "Keluar Program"]
    ]
    print(tabulate(data, headers=headers, tablefmt="simple_grid", colalign=("center", "left")))

def back():
    while True:
        try:
            back_menu = int(input('\nMasukan angka 1 untuk kembali ke menu sebelumnya: '))
            if back_menu == 1:
                return print()           
            else:
                print('\nInput Yang Anda Masukan Salah, Mohon Masukan Angka 1 lagi')   
        except ValueError:
            print('\nInput tidak valid! Mohon masukkan angka 1.')

def main():
    table_headers = ["Peran", "Instruksi"]
    data = [
        ["Admin", "Masukkan Angka (1)"],
        ["User", "Masukkan Angka (2)"]
    ]
    print(tabulate(data, headers=table_headers, tablefmt="simple_grid", colalign=("center","left")))

main()

while True:
    try:
        login = int(input('\nLogin dengan masukan angka (1/2): '))
        if login == 1:
            while True:
                password = maskpass.askpass(prompt='\nMasukan Password : ', mask='•')
                if password == 'admin':
                    while True:
                        menu_utama_admin()
                        pilihan = input("\nMasukkan nomor menu yang ingin dijalankan: ")

                        if pilihan == '1':
                            while True:
                                sub_menu()
                                input_submenu = input("\nMasukkan nomor sub-menu yang ingin dijalankan: ")

                                if input_submenu == '1':
                                    tampilkan_smartphone()
                                    back()
                                elif input_submenu == '2':
                                    lihat_detail_smartphones()        

                                elif input_submenu == '3':
                                    fitur_sorting()
                    
                                elif input_submenu == '4':
                                    break
                                else:
                                    print("\nInput tidak valid. Silakan masukkan angka (1/2/3/4).")

                        elif pilihan == '2':
                            tampilkan_smartphone()
                            tambah_smartphone()
                            back()
        
                        elif pilihan == '3':
                            hapus_smartphone()
                         
                        elif pilihan == '4':
                            update_smartphone()

                        elif pilihan == '5':
                            print("\nTerima kasih telah menggunakan program ini!")
                            sys.exit()
                        else:
                            print("\nPilihan tidak ada dalam menu, silakan coba lagi.")
                else:
                    print("\nPassword tidak valid. Silakan coba lagi.")                   
        elif login == 2:
            while True:
                print("-" * 40)
                print('Selamat Datang di Grote Cellular!'.center(40))
                print("-" * 40)
                menu_utama_user()
                try:
                    pilihan = int(input("\nMasukkan nomor menu yang ingin dijalankan: "))
                    if pilihan == 1:
                        while True:
                            sub_menu()
                            input_submenu_user = int(input("\nMasukkan nomor sub-menu yang ingin dijalankan: "))
                            if input_submenu_user == 1:
                                tampilkan_smartphone()
                                back()
                            elif input_submenu_user == 2:
                                lihat_detail_smartphones()

                            elif input_submenu_user == 3:
                                fitur_sorting()
        
                            elif input_submenu_user == 4:
                                break
                            else:
                                print("\nInput tidak valid. Silakan masukkan angka (1/2/3).")
                    elif pilihan == 2:
                        beli_smartphone()
                        back()
                    elif pilihan == 3:
                        print("\nTerima kasih telah menggunakan program ini!")
                        sys.exit()
                    else:
                        print("\nNomor tidak valid. Harap masukkan 1, 2, atau 3.")
                except ValueError:
                    print("\n- Mohon Masukan Angka Bukan Huruf -")
        else:
            print("\nNomor tidak valid. Harap masukkan 1 atau 2 untuk login.")
    except ValueError:
        print("\n- Mohon Masukan Angka Bukan Huruf -")