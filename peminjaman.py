# =====================================================
# CLASS PEMINJAMAN (Association/Relasi)
# Satu peminjaman memiliki 1 anggota 1 buku
# Alur status: Menunggu persetujuan --> dipinjam --> dikembalikan
#             (atau Menunggu Persetujuan --> Ditolak)
# =====================================================

from datetime import date, datetime, timedelta

class Peminjaman:
    # Atribut milik class (nilainya sama untuk semua peminjaman)
    lama_pinjam = 14            # Batas hari peminjaman
    denda_per_hari = 1000       # Denda keterlmbatan (Rp) perhari

    def __init__(self, kode_pinjam, anggota, buku):
        self.__kode_pinjam = kode_pinjam
        self.__anggota = anggota        # Relasi: 1 objek Anggota
        self.__buku = buku              # Relasi: 1 objek Buku (fiksi/non-fiksi)
        # Tanggal baru diisi setelah di acc admin / buku dikembalikan
        self.__tgl_pinjam = None
        self.__tgl_kembali = None
        self.__status = "Menunggu Persetujuan"      # Status awal setiap pengajuan

# Getter
    def get_kode_pinjam(self):
        return self.__kode_pinjam
        
    def get_anggota(self):
        return self.__anggota
        
    def get_buku(self):
        return self.__buku
    
    def get_status(self):
        return self.__status

    # Batas kembali = tgl pinjam + lama_pinjam hari (timedelta)
    def get_batas_kembali(self):
        if self.__tgl_pinjam is None:
            return None
        return self.__tgl_pinjam + timedelta(days= Peminjaman.lama_pinjam)

# Method Tambahan
    def tampilkan_data(self):
        print("Kode Pinjam      :", self.__kode_pinjam)
        print("Anggota          :", self.__anggota.get_nama())
        print("Buku             :", self.__buku.get_judul())
        print("Status           :", self.cek_status())
        # Info tgl dan denda hanya ada setelah peminjaman di acc
        if self.__tgl_pinjam:
            print("Tanggal Pinjam   :", self.__tgl_pinjam)
            print("Batas Kembali    :", self.get_batas_kembali())
            print("Denda            : Rp", self.hitung_denda())
           
    # Admin menyetujui / acc pengajuan
    def setujui(self):
        # Hanya pengajuan yang masih menunggu yang bisa disetujui
        if self.__status != "Menunggu Persetujuan":
            return False
        # Validasi batas pinjam anggota, sekaligus mengurangi stok
        if not self.__anggota.boleh_meminjam() or not self.__buku.kurangi_stok(1):
            return False
        self.__anggota.tambah_pinjam()
        self.__tgl_pinjam = date.today()    # tgl pinjam = hari disetujui
        self.__status = "Dipinjam"
        return True

    # Admin menolak pengajuan (stok tidak berubah)
    def tolak(self):
        if self.__status != "Menunggu Persetujuan":
            return False
        self.__status = "Ditolak"
        return True

    # Pengembalian buku: stok bertambah, hitungan pinjam anggota berkurang
    def kembalikan(self):
        if self.__status != "Dipinjam":
            return False
        self.__tgl_kembali = date.today()
        self.__buku.tambah_stok(1)
        self.__anggota.kurangi_pinjam()
        self.__status = "Dikembalikan"
        return True

    def hitung_denda(self):
        # Denda = hari terlambat x tarif per hari
        if self.__tgl_pinjam is None:
            return 0
        # Jika belum dikembalikan, hitung sampai hari ini
        acuan = self.__tgl_kembali or date.today()
        telat = (acuan - self.get_batas_kembali()).days
        return max(0, telat) * Peminjaman.denda_per_hari    # tidak boleh negatif

     # Status "Terlambat" dihitung otomatis dari tanggal (tidak disimpan)
    def cek_status(self):
        if self.__status == "Dipinjam" and date.today() > self.get_batas_kembali():
            return "Terlambat"
        return self.__status
