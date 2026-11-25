from buku import Buku

# =====================================================
# SUBCLASS 2: BukuNonFiksi (Mewarisi Buku / inheritance)
# Atribut tambahan: Bidang ilmu
# =====================================================

class BukuNonFiksi(Buku):
    def __init__(self, kode_buku, judul, penulis, stok, bidang): 
        # constructor superrclass untuk data umum
        super().__init__(kode_buku, judul, penulis, stok)  
        # validasi atribut milik subclass
        if not bidang.strip():
            raise ValueError("Bidang tidak valid")
        self.__bidang = bidang          # atribut private khusus buku non-fiksi

    # Overriding: menimpa get_kategori() milik Buku
    def get_kategori(self):
        return f"Non-Fiksi - {self.__bidang}"

    # Overriding: menjalankan versi (superclass), lalu menambah info non-fiksi
    def tampilkan_data(self):
        super().tampilkan_data()
        print("Jenis            : Non-Fiksi")
        print("Bidang           :", self.__bidang)

    def ubah_bidang(self, bidang_baru):
        if not bidang_baru.strip():
            return False
        self.__bidang = bidang_baru.strip()
        return True

    