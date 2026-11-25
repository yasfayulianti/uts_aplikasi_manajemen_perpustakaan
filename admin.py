# =====================================================
# CLASS ADMIN
# Admin acc/tolak peminjaman, memproses pengembalian
# dan kelola data
# =====================================================

class Admin:
    def __init__(self, id_admin, nama, password):
        # Validasi panjang password
        if len(password) < 6:
            raise ValueError("Password minimal 6 karakter")
        # Atribut private (encapsulation)
        self.__id_admin = id_admin
        self.__nama = nama
        self.__password = password   # Password tidak ada getter
        
# Getter
    def get_id_admin(self):
        return self.__id_admin

    def get_nama(self):
        return self.__nama

# Method tambahan

    def tampilkan_data(self):
        print("Id Admin         :", self.__id_admin)
        print("Nama             :", self.__nama)

    # Verifikasi login tanpa buka isi pw
    def cek_password(self, password):
        return self.__password == password

    # Tiga method dibawah meneruskan perintah admin ke objek peminjaman
    def setujui_peminjaman(self, peminjaman):
        return peminjaman.setujui()

    def tolak_peminjaman(self, peminjaman):
        return peminjaman.tolak()

    def proses_pengembalian(self, peminjaman):
        return peminjaman.kembalikan()

    
    