from buku import Buku

# =====================================================
# SUBCLASS 2: BukuNonFiksi (Mewarisi Buku / inheritance)
# Atribut tambahan: Bidang ilmu
# =====================================================

class BukuNonFiksi(Buku):
    def __init__(self, kode_buku, judul, penulis, stok, bidang,
                    penerbit = "Tidak diketahu", tahun_terbit = "Tidak diketahui"):
        # constructor superrclass untuk data umum
        super().__init__(kode_buku, judul, penulis, stok)  
        # validasi atribut milik subclass
        if not bidang.strip():
            raise ValueError("Bidang tidak valid")
        self.__bidang = bidang          # atribut private khusus buku non-fiksi
        if not penerbit.strip() or not str (tahun_terbit).strip():
            raise ValueError("Penerbit dan Tahun terbit tidak boleh kosong")
        self.__penerbit = penerbit
        self.__tahun_terbit = tahun_terbit

# Getter

    # Override Kategorri dair Class Buku
    def get_kategori(self):
        return f"Non-Fiksi - {self.__bidang}"

    def get_bidang(self):
        return self.__bidang

    def get_penerbit(self):
        return self.__penerbit

    def get_tahun_terbit(self):
        return self.__tahun_terbit

    # Menampilkan data umum + data khusus BukuNonFiksi
    def tampilkan_data(self):
        super().tampilkan_data()
        print("Jenis            : Non-Fiksi")
        print("Bidang           :", self.__bidang)
        print("Penerbit         :", self.__penerbit)
        print("Tahun Terbit     :", self.__tahun_terbit)

    # Method untuk mengubah atribut khusus
    def ubah_bidang(self, bidang_baru):
        if not bidang_baru.strip():
            return False
        self.__bidang = bidang_baru.strip()
        return True

    def ubah_penerbit(self, penerbit_baru):
        if not penerbit_baru.strip():
            return False
        self.__penerbit = penerbit_baru.strip()
        return True

    def ubah_tahun_terbit(self, tahun_terbit_baru):
        if not str(tahun_terbit_baru).strip():
            return False
        self.__tahun_terbit = str(tahun_terbit_baru).strip()
        return True
    