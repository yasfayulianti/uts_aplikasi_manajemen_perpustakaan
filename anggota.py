# =====================================================
# CLASS ANGGOTA
# Anggota perpustakaan: dapat mengajukan peminjaman, ubah
# profil (nama, alamat), dan melihat data buku
# =====================================================

class Anggota:
    # constructor berparameter (batas_pinjam punya nilai default 3,
    # jadi boleh tidak diisi)
    def __init__(self, id_anggota, nama, alamat, email, batas_pinjam=3):
         # Atribut private (encapsulation)
        self.__id_anggota = id_anggota
        self.__nama = nama
        if not nama.strip():        # validasi data awal
            raise ValueError("Nama tidak valid")
        self.__alamat = alamat
        if not alamat.strip():
            raise ValueError("Alamat tidak valid")
        self.__email = ""              # Email divalidasi lewat method ubah_email
        if not self.ubah_email(email):
            raise ValueError("Email awal tidak valid")
        self.__batas_pinjam = batas_pinjam          # maksimal buku yg boleh dipinjam
        if batas_pinjam <= 0:
            raise ValueError("Batas pinjam tidak valid")
        self.__jumlah_pinjam = 0                    # status awal: belum meminjam

# Getter (cara untuk baca atribut private)
    def get_id_anggota(self):
        return self.__id_anggota

    def get_nama(self):
        return self.__nama

    def get_alamat(self):
        return self.__alamat

    def get_email(self):
        return self.__email

    def get_batas_pinjam(self):
        return self.__batas_pinjam

    def get_jumlah_pinjam(self):
        return self.__jumlah_pinjam

# Method tambahan

    # Menampilkan data anggota
    def tampilkan_data(self):
        print("Id Anggota       :", self.__id_anggota)
        print("Nama             :", self.__nama)
        print("Alamat           :", self.__alamat)
        print("Email            :", self.__email)
        print("Batas Pinjam     :", self.__batas_pinjam, "buku")
        print("Sedang Dipinjam  :", self.__jumlah_pinjam, "buku")

    # Untuk cek sudah mencapai batas/belum?
    def boleh_meminjam(self):
        return self.__jumlah_pinjam < self.__batas_pinjam

    # Dipanggil saat peminjaman di acc admin
    def tambah_pinjam(self):
        if not self.boleh_meminjam():
            return False
        self.__jumlah_pinjam += 1
        return True

    # Dipanggil saat buku dikembalikan
    def kurangi_pinjam(self):
        if self.__jumlah_pinjam <= 0:
            return False
        self.__jumlah_pinjam -= 1
        return True

    # Anggota hanya boleh mengubah nama dan alamat
    def ubah_nama(self, nama_baru):
        if not nama_baru.strip():
            return False
        self.__nama = nama_baru.strip()
        return True

    def ubah_alamat(self, alamat_baru):
        if not alamat_baru.strip():
            return False
        self.__alamat = alamat_baru.strip()
        return True

    # Validasi sederhana: email harus mengandung "@" dan "."
    def ubah_email(self, email_baru):
        if "@" not in email_baru or "." not in email_baru:
            return False
        self.__email = email_baru
        return True

    