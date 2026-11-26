from buku import Buku

# =====================================================
# SUBCLASS 1: BukuFiksi (Mewarisi Buku / inheritance)
# Atribut tambahan: Genre
# =====================================================

class BukuFiksi(Buku):
    def __init__(self, kode_buku, judul, penulis, stok, genre,
                 penerbit = "Tidak diketahu", tahun_terbit = "Tidak diketahui"): 
        # constructor superrclass untuk data umum
        super().__init__(kode_buku, judul, penulis, stok) 
        # validasi atribut milik subclass
        if not genre.strip():
            raise ValueError("Genre tidak valid")
        self.__genre = genre     # atribut private khusus buku fiksi
        if not penerbit.strip() or not str (tahun_terbit).strip():
            raise ValueError("Penerbit dan Tahun terbit tidak boleh kosong")
        self.__penerbit = penerbit
        self.__tahun_terbit = tahun_terbit

# Getter

    # Override Kategorri dair Class Buku
    def get_kategori(self):
        return f"Fiksi - {self.__genre}"

    def get_genre(self):
        return self.__genre

    def get_penerbit(self):
        return self.__penerbit

    def get_tahun_terbit(self):
        return self.__tahun_terbit
    
    # Menampilkan data umum + data khusus BukuFiksi
    def tampilkan_data(self):
        super().tampilkan_data()
        print("Jenis            : Fiksi")
        print("Genre            :", self.__genre)
        print("Penerbit         :", self.__penerbit)
        print("Tahun Terbit     :", self.__tahun_terbit)

    # Method untuk mengubah atribut khusus
    def ubah_genre(self, genre_baru):
        if not genre_baru.strip():
            return False
        self.__genre = genre_baru.strip()
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
        

    