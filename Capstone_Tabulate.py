
# CAPSTONE PROJECT - ANDI RIZKI NOFENTRI 

#DATA PERUSAHAAN KARYAWAN SUKSES

from tabulate import tabulate

data_karyawan = [
    {"id": 1, "nama": "Andi", "jabatan": "Manager", "divisi": "Operasional", "gaji": 15000000},
    {"id": 2, "nama": "Budi", "jabatan": "Staff", "divisi": "Finance", "gaji": 7000000},
    {"id": 3, "nama": "Citra", "jabatan": "HRD", "divisi": "SDM", "gaji": 9000000},
    {"id": 4, "nama": "Dewi", "jabatan": "Supervisor", "divisi": "Produksi", "gaji": 11000000},
    {"id": 5, "nama": "Eka", "jabatan": "Staff", "divisi": "Marketing", "gaji": 8000000},
    {"id": 6, "nama": "Fajar", "jabatan": "Analis", "divisi": "Data", "gaji": 10000000},
    {"id": 7, "nama": "Gita", "jabatan": "Manager", "divisi": "IT", "gaji": 15000000},
    {"id": 8, "nama": "Hadi", "jabatan": "Staff", "divisi": "Logistik", "gaji": 7500000},
    {"id": 9, "nama": "Indah", "jabatan": "Supervisor", "divisi": "Produksi", "gaji": 10500000},
    {"id": 10, "nama": "Joko", "jabatan": "Admin", "divisi": "General Affair", "gaji": 6500000}
]

def tampilkan_data():
    print("\n=== DATA KARYAWAN ===")
    headers = ["ID", "Nama", "Jabatan", "Divisi", "Gaji"]
    rows = []
    for d in data_karyawan:
        rows.append([d['id'], d['nama'], d['jabatan'], d['divisi'], d['gaji']])
    print(tabulate(rows, headers=headers, tablefmt="grid", numalign="right", stralign="left"))
    input("\nTekan Enter untuk kembali ke menu...")

def tambah_data():
    print("\n=== TAMBAH DATA KARYAWAN ===")
    id_baru = int(input("Masukkan ID: "))
    nama = input("Masukkan Nama: ")
    jabatan = input("Masukkan Jabatan: ")
    divisi = input("Masukkan Divisi: ")
    gaji = int(input("Masukkan Gaji: "))
    data_karyawan.append({"id": id_baru, "nama": nama, "jabatan": jabatan, "divisi": divisi, "gaji": gaji})
    print("✅ Data berhasil ditambahkan!")
    input("\nTekan Enter untuk kembali ke menu...")

def ubah_data():
    print("\n=== UBAH DATA KARYAWAN ===")
    id_edit = int(input("Masukkan ID yang akan diubah: "))
    for karyawan in data_karyawan:
        if karyawan["id"] == id_edit:
            karyawan["nama"] = input("Masukkan Nama Baru: ")
            karyawan["jabatan"] = input("Masukkan Jabatan Baru: ")
            karyawan["divisi"] = input("Masukkan Divisi Baru: ")
            karyawan["gaji"] = int(input("Masukkan Gaji Baru: "))
            print("✅ Data berhasil diubah!")
            input("\nTekan Enter untuk kembali ke menu...")
            return
    print("❌ ID tidak ditemukan.")
    input("\nTekan Enter untuk kembali ke menu...")

def hapus_data():
    print("\n=== HAPUS DATA KARYAWAN ===")
    id_hapus = int(input("Masukkan ID yang akan dihapus: "))
    for i, karyawan in enumerate(data_karyawan):
        if karyawan["id"] == id_hapus:
            del data_karyawan[i]
            print("✅ Data berhasil dihapus!")
            input("\nTekan Enter untuk kembali ke menu...")
            return
    print("❌ ID tidak ditemukan.")
    input("\nTekan Enter untuk kembali ke menu...")

def menu_utama():
    while True:
        print("\n=== SISTEM DATA KARYAWAN PT SUKSES SELALU ===")
        print("1. Tampilkan Data Karyawan")
        print("2. Tambah Data Karyawan")
        print("3. Ubah Data Karyawan")
        print("4. Hapus Data Karyawan")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan menu (1-5): ")

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("👋 Terima kasih. Program selesai.")
            break
        else:
            print("❗ Pilihan tidak valid, coba lagi.")

menu_utama()
