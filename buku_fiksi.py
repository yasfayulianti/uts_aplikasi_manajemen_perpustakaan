from buku import Buku

# =====================================================
# SUBCLASS 1: BukuFiksi (Mewarisi Buku / inheritance)
# Atribut tambahan: Genre
# =====================================================

class BukuFiksi(Buku):
    def __init__(self, kode_buku, judul, penulis, stok, genre): 
        # constructor superrclass untuk data umum
        super().__init__(kode_buku, judul, penulis, stok) 
        # validasi atribut milik subclass
        if not genre.strip():
            raise ValueError("Genre tidak valid")
        self.__genre = genre        # atribut private khusus buku fiksi

    def get_kategori(self):
        return f"Fiksi - {self.__genre}"

    # Overriding: menimpa get_kategori() milik Buku
    def get_genre(self):
        return self.__genre

    # Overriding: menjalankan versi (superclass), lalu menambah info fiksi
    def tampilkan_data(self):
        super().tampilkan_data()
        print("Jenis            : Fiksi")
        print("Genre            :", self.__genre)

    def ubah_genre(self, genre_baru):
        if not genre_baru.strip():
            return False
        self.__genre = genre_baru.strip()
        return True

    