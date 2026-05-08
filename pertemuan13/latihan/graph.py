class Graph:
    def __init__(self):
        self.graph = {}

    # 1. Menambahkan kota
    def tambah_kota(self, nama):
        if nama not in self.graph:
            self.graph[nama] = []

    # 2. Menambahkan jalan dua arah
    def tambah_jalan(self, u, v, jarak):
        self.tambah_kota(u)
        self.tambah_kota(v)

        self.graph[u].append((v, jarak))
        self.graph[v].append((u, jarak))

        print(f'[INPUT] Menambahkan jalan: {u} - {v} ({jarak} km)')

    # 3. Menampilkan graph
    def tampilkan_graph(self):
        print("\n[INFO] Struktur Jaringan Distribusi:")
        for kota in self.graph:
            tetangga = []
            for tujuan, jarak in self.graph[kota]:
                tetangga.append(f"{tujuan} ({jarak})")
            print(f"- {kota} terhubung ke: {', '.join(tetangga)}")

    # Fungsi bantu mencari kota dengan jarak minimum
    def cari_jarak_terkecil(self, jarak, dikunjungi):
        minimum = float('inf')
        kota_terdekat = None

        for kota in jarak:
            if kota not in dikunjungi and jarak[kota] < minimum:
                minimum = jarak[kota]
                kota_terdekat = kota

        return kota_terdekat

    # 4. Algoritma Dijkstra
    def dijkstra(self, kota_asal):
        jarak = {}
        for kota in self.graph:
            jarak[kota] = float('inf')

        jarak[kota_asal] = 0

        dikunjungi = set()

        # Proses semua node
        while len(dikunjungi) < len(self.graph):
            kota_sekarang = self.cari_jarak_terkecil(jarak, dikunjungi)

            # Jika tidak ada kota tersisa
            if kota_sekarang is None:
                break

            dikunjungi.add(kota_sekarang)

            # Update jarak tetangga
            for tetangga, bobot in self.graph[kota_sekarang]:
                if tetangga not in dikunjungi:
                    jarak_baru = jarak[kota_sekarang] + bobot

                    if jarak_baru < jarak[tetangga]:
                        jarak[tetangga] = jarak_baru

        return jarak

# program utama
print("SISTEM NAVIGASI LOGISTIK 'KILAT MAJU'")
print("=========================================")

# Membuat graph
g = Graph()

# Input jaringan jalan
g.tambah_jalan("Jakarta", "Bandung", 150)
g.tambah_jalan("Jakarta", "Cirebon", 200)
g.tambah_jalan("Bandung", "Tasikmalaya", 100)
g.tambah_jalan("Bandung", "Cirebon", 130)
g.tambah_jalan("Cirebon", "Semarang", 250)
g.tambah_jalan("Tasikmalaya", "Semarang", 200)

# Tampilkan struktur graph
g.tampilkan_graph()

# Jalankan Dijkstra
print("\n[PROSES] Menghitung rute terpendek dari: Jakarta...\n")
hasil = g.dijkstra("Jakarta")

# Tampilkan hasil
print("[HASIL] Jarak Terpendek dari Jakarta:")

nomor = 1
for kota, jarak in hasil.items():
    if kota != "Jakarta":
        print(f"{nomor}. Ke {kota}: {jarak} km")
        nomor += 1

print("\n=========================================")
print("Simulasi Navigasi Selesai!")