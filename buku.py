# =====================================================
# SUPERCLASS BUKU
# Menyimpan data umum yang dimiliki semua jenis buku
# =====================================================

class Buku:
    #  constructor berparameter + validasi data awal
    def __init__(self, kode_buku, judul, penulis, stok):
        # Atribute private (encapsulation)
        self.__kode_buku = kode_buku
        self.__judul = judul
        self.__penulis = penulis
        self.__stok = stok
        # Validasi stok awal tidak boleh negatif
        if stok < 0:
            raise ValueError("Stok tidak valid")

# Getter (cara untuk baca atribut private)
    def get_kode_buku(self):
        return self.__kode_buku
    
    def get_judul(self):
        return self.__judul
    
    def get_penulis(self):
        return self.__penulis

    def get_stok(self):
        return self.__stok
    
    # Kategori umum: di-override oleh subclass
    def get_kategori(self):
        return "Umum"
    
# Method tambahan

    # Menampilkan data buku 
    def tampilkan_data(self):
        print("Kode             :", self.__kode_buku)
        print("Judul Buku       :", self.__judul)
        print("Penulis          :", self.__penulis)
        print("Stok             :", self.__stok)
        print("Status           :", self.cek_status())

    # Status ketersediaan stok
    def cek_status(self):
        return "Tersedia" if self.__stok > 0 else "Habis"

    # Menambah stok (buku dikembalikan)
    def tambah_stok(self, jumlah):
        # Ditolak jika jumlah <= 0
        if jumlah <= 0:
            return False
        self.__stok += jumlah
        return True

    # Mengurangi stok (buku dipinjam)
    def kurangi_stok(self, jumlah):
        # Ditolak jika jumlah tidak valid atau melebihi stok
        if jumlah <= 0 or jumlah > self.__stok:
            return False
        self.__stok -= jumlah
        return True

    # Setter dengan validasi: nilai kosong ditolak
    def ubah_judul(self, judul_baru):
        if not judul_baru.strip():
            return False
        self.__judul = judul_baru.strip()
        return True

    def ubah_penulis(self, penulis_baru):
        if not penulis_baru.strip():
            return False
        self.__penulis = penulis_baru.strip()
        return True

    # Atur ulang stok oleh Admin: stok tidak boleh <0 (negatif)
    def ubah_stok(self, stok_baru):
        if stok_baru < 0:
            return False
        self.__stok = stok_baru
        return True