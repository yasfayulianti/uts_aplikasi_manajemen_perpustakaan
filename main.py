# =====================================================
# MAIN: APLIKASI MANAJEMEN PERPUSTAKAAN (CLI)
# File ini hanya menjalankan program: menyimpan dafta objek,
# menampilkan menu, dan manggil method dr class-class domain.
# Ada Dua peran:
# - Admin   : Kelola buku/anggota/peminjaman (tolak/acc), pengembalian
# - Anggota : Ajukn peminjaman, ubah profil, lihat data buku
# =====================================================

from buku_nonfiksi import BukuNonFiksi
from buku_fiksi import BukuFiksi
from peminjaman import Peminjaman
from buku import Buku
from anggota import Anggota
from admin import Admin


# Penyimpanan data sementara
daftar_buku = [
    BukuFiksi("B001", "Pulang", "Tere Liye", 3, "Aksi/Drama", "Republika", 2015),
    BukuNonFiksi("B002", "Pemrogoraman Berbasis Objek", "Mahardika Abdi dkk", 4, "Informatika", "UMSU Press", 2025)
]

daftar_anggota = [Anggota("A001", "Yasfa", "Arcamanik, Bandung", "yasfayuliantinazia@gmail.com")]
daftar_admin = [Admin("ADM01", "Petugas Perpustakaan", "admin123")]
daftar_pinjam = []

# Fungsi bantu
def input_angka(pesan):
    # Ulangi sampai pengguna memasukkan angka bulat
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input harus berupa angka.")

# Tiga fungsi dibawah mengembalikan objek yg cocok atau None
def cari_buku(kode):
    for b in daftar_buku:
        if b.get_kode_buku().lower() == kode.lower():
            return b
    return None

def cari_anggota(id_anggota):
    for a in daftar_anggota:
        if a.get_id_anggota().lower() == id_anggota.lower():
            return a
    return None

def cari_pinjam(kode):
    for p in daftar_pinjam:
        if p.get_kode_pinjam().lower() == kode.lower():
            return p
    return None

def tampil_daftar(data, kosong="Belum ada data."):
    # Menampilkan tiap objek lewat method tampilkan_data(), tiap class punya tampilaka_data() versinya sendiri
    if not data:
        print(kosong)
    for i, item in enumerate(data, 1):
        print(f"\n--- Data {i} ---")
        item.tampilkan_data()

# Menampilkan hasil operasi (True/False)
def hasil(berhasil):
    print("Berhasil" if berhasil else "Gagal / data tidak valid")

# Ubah data jika diisi, input kosong = lewati
def ubah_jika_diisi(label, fungsi):
    nilai = input(f"{label} baru (kosongkan jika tidak diubah):")
    if nilai.strip():
        print(f"{label}:", end=" ")
        hasil(fungsi(nilai))


# =====================================================
# MENU ADMIN
# =====================================================
# Menu 1: Tambah data buku atau anggota
def admin_tambah():                                          
    print("1. Buku      2. Anggota")
    k = input("Pilih:   ").strip()
    if k == "1":
        kode = input("Kode Buku    :").strip()
        # Kode tidak boleh kosong / kembar
        if not kode or cari_buku(kode):     
            print("Kode kosong / sudah dipakai.")
            return
        judul = input("Judul        :").strip()
        penulis = input("Penulis      :").strip()
        stok = input_angka("Stok         :")
        jenis = input("Jenis (1=Fiksi, 2=Non-Fiksi):").strip()
        # try/exceept menangkap ValueError dari constructor (data tidak valid)
        try:
            if jenis == "1":
                # Objek subclass BukuFiksi disimpan di list bertipe Buku
                daftar_buku.append(BukuFiksi(kode, judul, penulis, stok,            
                                             input("Genre        :"), input("Penerbit     :"), input("Tahun Terbit :")))
            elif jenis == "2":
                daftar_buku.append(BukuNonFiksi(kode, judul, penulis, stok,
                                                input("Bidang ilmu  :"), input("Penerbit     :"), input("Tahun Terbit :")))   
            else:
                print("Jenis tidak valid.") 
                return
            print("Buku berhasil ditambahkan.")
        except ValueError as e:
            print("Gagal        :", e)
    elif k == "2":
        id_a = input("Id Anggota        :").strip()
        if not id_a or cari_anggota(id_a):
            print("Id kosong / sudah dipakai.")
            return
        try: 
            daftar_anggota.append(Anggota(id_a, input("Nama         :"),
                                          input("Alamat       :"),
                                          input("Email        :")))
            print("Anggota berhasil ditambahkan.")
        except ValueError as e:
            print("Gagal        :", e)
    else:
        print("Pilihan tidak valid.")

# Menu 2: Tampilkan data (buku/anggota/peminjaman)
def admin_tampil():
    print("1. Buku      2. Anggota      3. Peminjaman")
    k = input("Pilih:   ").strip()
    # Dictionary memetakan pilihan ke list data yang sesuai
    data = {"1": daftar_buku, "2": daftar_anggota, "3": daftar_pinjam}.get(k)
    if data is None:
        print("Pilihan tidak valid.")
    else:
        tampil_daftar(data)

# Menu 3: Cari data berdasarkan kata kunci
def admin_cari():
    print("1. Buku      2. Anggota      3. Peminjaman")
    k = input("Pilih:   ").strip()
    kata = input("Kata kunci:   ").strip().lower()
    if k == "1":
        ketemu = [b for b in daftar_buku
                  if kata in b.get_judul().lower()
                  or kata in b.get_penulis().lower()
                  or kata in b.get_kode_buku().lower()
                  or kata in b.get_kategori().lower()]
    elif k == "2":
        ketemu = [a for a in daftar_anggota
                  if kata in a.get_nama().lower()
                  or kata in a.get_id_anggota().lower()]
    elif k == "3":
        ketemu = [p for p in daftar_pinjam
                  if kata in p.get_kode_pinjam().lower()
                  or kata in p.get.buku().get_penulis().lower()
                  or kata in p.get_anggota().get_nama().lower()
                  or kata in p.get_buku().get_judul().lower()]
    else:
        print("Pilihan tidak valid.")
        return
    tampil_daftar(ketemu, "Data tidak ditemukan.")

# Menu 4: Ubah data buku (judul, penulis, stok, genre/bidang)
def admin_ubah_buku():
    b = cari_buku(input("Kode Buku  :").strip())
    if not b:
        print("Buku tidak ditemukan.")
        return
    b.tampilkan_data()
    print("\n(kosongkan jika tidak diubah)")
    ubah_jika_diisi("Judul", b.ubah_judul)
    ubah_jika_diisi("Penulis", b.ubah_penulis)
    ubah_jika_diisi("Penerbit", b.ubah_penerbit)
    ubah_jika_diisi("Tahun Terbit", b.ubah_tahun_terbit)
    stok = input("Stok baru (kosongkan jika tidak diubah):").strip()
    if stok:
        print("Stok:", end=" ")
        hasil(stok.isdigit() and b.ubah_stok(int(stok)))
    # Insistance: memeriksa jenis objek untuk mengubah atribut khusus subclass
    if isinstance(b, BukuFiksi):
        ubah_jika_diisi("Genre", b.ubah_genre)
    elif isinstance(b, BukuNonFiksi):
        ubah_jika_diisi("Bidang", b.ubah_bidang)

    ubah_jika_diisi("Penerbit", b.ubah_penerbit)
    ubah_jika_diisi("Tahun Terbit", b.ubah_tahun_terbit)

# Menu 5: Cek status buku/anggota/peminjaman
def admin_cek_status():
    print("1. Buku      2. Anggota      3. Peminjaman")
    k = input("Pilih:   ").strip()
    if k == "1":
        b = cari_buku(input("Kode Buku  :").strip())
        if b:
            print(b.get_judul(), "->", b.cek_status(), "| stok", b.get_stok())
        else:
            print("Buku tidam ditemukan.")
    elif k == "2":
        a = cari_anggota(input("Id Anggota      :").strip())
        if a:
            print(a.get_nama(), "sedang meminjam", a.get_jumlah_pinjam(), "buku",
                  "boleh meminjam lagi" if a.boleh_meminjam() else "sudah mencapai batas" )
        else:
            print("Anggota tidak ditemukan.")
    elif k == "3":
        p = cari_pinjam(input("Kode Peminjaman  :").strip())
        if p:
            print("Status:", p.cek_status(), "| Denda: Rp", p.hitung_denda())
        else:
            print("Peminjaman tidak ditemukan.")
    else:
        print("Pilihan tidak valid.")

# Menu 6: Admin menyetujui/ menolak pengajuan peminjaman
def admin_persetujuan(admin):
    # Daftar pengajuan yang masih menunggu
    menunggu = [p for p in daftar_pinjam
                if p.get_status() == "Menunggu Persetujuan"]
    tampil_daftar(menunggu, "Tidak ada pengajuan yang menunggu.")
    if not menunggu:
        return
    p = cari_pinjam(input("\nKode Peminjaman yang diproses: ").strip())
    if not p or p not in menunggu:
        print("Kode tidak valid.")
        return
    aksi = (input("1. Setujui        2. Tolak        :").strip())
    if aksi == "1":
        # Stok berkurang (di dalam setujui_peminjaman)
        if admin.setujui_peminjaman(p):
            print("Peminjaman Disetujui, stok berkurang.")
        else:
            print("Gagal: stok habis atau anggota sudah mencapai batas pinjam.")
    elif aksi == "2":
        hasil(admin.tolak_peminjaman(p))
    else:
        print("Pilihan tidak valid.")

# Menu 7: Pengembalian buku (stok bertambah (dikembalikan ke rak), denda dihitung)
def admin_pengembalian(admin):
    p = cari_pinjam(input("Kode Peminjaman  :").strip())
    if not p:
        print("Peminjaman tidak ditemukan.")
    elif admin.proses_pengembalian(p):
        print("Buku dikembalikan. Denda :Rp", p.hitung_denda())
    else:
        print("Gagal: peminjaman ini tidak berstatus 'Dipinjam'.")

# Menu admin: berhenti saat memilih 0 (keluar)
def menu_admin(admin):
    while True:
        print(f"\n== MENU ADMIN ({admin.get_nama()}) ===")
        print("1. Tambah data (buku/anggota)")
        print("2. Tampilkan data")
        print("3. Cari data")
        print("4. Ubah data buku (judul, penulis, stok, kategori)")
        print("5. Cek status data")
        print("6. Persetujuan peminjaman")
        print("7. Proses Pengembalian")
        print("0. Keluar")
        pilih = input("Pilih menu   :").strip()
        print()
        if pilih == "1":
            admin_tambah()
        elif pilih == "2":
            admin_tampil()
        elif pilih == "3":
            admin_cari()
        elif pilih == "4":
            admin_ubah_buku()
        elif pilih == "5":
            admin_cek_status()
        elif pilih == "6":
            admin_persetujuan(admin)
        elif pilih == "7":
            admin_pengembalian(admin)
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")


# =====================================================
# MENU ANGGOTA
# =====================================================
# Anggota melihat daftar buku (judul, penulis, kategori, stok)
def anggota_katalog():
    # Anggota melihat info buku: judul, penulis, kategori, stok
    tampil_daftar(daftar_buku, "Belum ada buku.")

# Anggota mencari buku berdasarkan judul / kategori
def anggota_cari():
    kata = input("Cari judul/kategori: ").strip().lower()
    ketemu = [b for b in daftar_buku
              if kata in b.get_judul().lower()
              or kata in b.get_kategori().lower()]
    tampil_daftar(ketemu, "Buku tidak ditemukan.")

# Anggota mengajukan peminjaman: status "Menunggu Persetujuan"
def anggota_ajukan(anggota):
    b = cari_buku(input("Kode Buku yang ingin dipinjam: ").strip())
    if not b:
        print("Buku tidak ditemukan.")
        return
    if b.get_stok() <= 0:
        print("Stok buku habis.")
        return
    if not anggota.boleh_meminjam():
        print("Kamu sudah mencapai batas peminjaman.")
        return
    # Kode Otomatis: PJ001, PJ002, ...
    kode = f"PJ{len(daftar_pinjam) + 1:03d}"
    # Buat objek peminjaman, menghubungkan 1 anggota 1 buku
    daftar_pinjam.append(Peminjaman(kode, anggota, b))
    print(f"Pengajuan terkirim (kode {kode}). Menunggu persetujuan admin.")

# Menampilkan peminjaman hanya milik anggota yg sedang login
def anggota_peminjaman_saya(anggota):
    milik = [p for p in daftar_pinjam if p.get_anggota() is anggota]
    tampil_daftar(milik, "Belum ada peminjaman.")

# Anggota hanya boleh mengubah nama dan alamat
def anggota_ubah_profil(anggota):
    print("(kosongkan jika tidak diubah)")
    ubah_jika_diisi("Nama", anggota.ubah_nama)
    ubah_jika_diisi("Alamat", anggota.ubah_alamat)

# Menu anggota: berhenti saat memilih 0 (keluar)
def menu_anggota(anggota):
    while True:
        print(f"\n=== MENU ANGGOTA ({anggota.get_nama()}) ===")
        print("1. Lihat katalog buku")
        print("2. Cari buku")
        print("3. Ajukan peminjaman")
        print("4. Peminjaman saya / cek status")
        print("5. Lihat profil")
        print("6. Ubah profil (nama, alamat)")
        print("0. Logout")
        pilih = input("Pilih menu: ").strip()
        print()
        if pilih == "1":
            anggota_katalog()
        elif pilih == "2":
            anggota_cari()
        elif pilih == "3":
            anggota_ajukan(anggota)
        elif pilih == "4":
            anggota_peminjaman_saya(anggota)
        elif pilih == "5":
            anggota.tampilkan_data()
        elif pilih == "6":
            anggota_ubah_profil(anggota)
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")


# =====================================================
# LOGIN & MENU UTAMA
# =====================================================
# Login Admin: id & pw harus cocok; mengembalikan objek Admin / None
def login_admin():
    id_admin = input("Id Admin : ").strip()
    password = input("Password : ").strip()
    for a in daftar_admin:
        if a.get_id_admin() == id_admin and a.cek_password(password):
            return a
    return None

# Menu utama: pilih peran (Admin / Anggota) atau keluar dari program
def main():
    while True:
        print("\n=== PERPUSTAKAAN ===")
        print("1. Login Admin")
        print("2. Login Anggota")
        print("0. Keluar")
        pilih = input("Pilih: ").strip()
        print()
        if pilih == "1":
            admin = login_admin()
            if admin:
                menu_admin(admin)
            else:
                print("Id/password salah.")
        elif pilih == "2":
            anggota = cari_anggota(input("Id Anggota : ").strip())
            if anggota:
                menu_anggota(anggota)
            else:
                print("Id anggota tidak ditemukan.")
        elif pilih == "0":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()