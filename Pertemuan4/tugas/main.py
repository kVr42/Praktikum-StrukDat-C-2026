from kurs import kurs
from konverter import idr_ke_mata_uang, mata_uang_ke_idr
from tabulate import tabulate
from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.CYAN + "=== KONVERTER MATA UANG ===")

# Tabel kurs
table = []
for kode, nilai in kurs.items():
    table.append([kode, f"{nilai:,}".replace(",", ".")])

print(tabulate(table, headers=["Kode", "Kurs (IDR)"], tablefmt="grid"))

# Input
dari = input(Fore.YELLOW + "Dari (IDR/USD/EUR/SGD/JPY): ").upper()
ke = input(Fore.YELLOW + "Ke (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input(Fore.YELLOW + "Jumlah: "))

# Proses
if dari == "IDR" and ke != "IDR":
    hasil = idr_ke_mata_uang(jumlah, ke)
    print(Fore.GREEN + f"Rp {jumlah:,.0f} = {hasil:.2f} {ke}")

elif dari != "IDR" and ke == "IDR":
    hasil = mata_uang_ke_idr(jumlah, dari)
    print(Fore.GREEN + f"{jumlah:.2f} {dari} = Rp {hasil:,.0f}")

else:
    print(Fore.RED + "Konversi hanya mendukung IDR ke mata uang lain atau sebaliknya.")