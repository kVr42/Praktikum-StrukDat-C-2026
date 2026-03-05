# konverter.py

from kurs import kurs

def idr_ke_mata_uang(jumlah_idr, kode_mata_uang):# idr ke mata uang
    if kode_mata_uang in kurs:
        return jumlah_idr / kurs[kode_mata_uang]
    else:
        return None


def mata_uang_ke_idr(jumlah, kode_mata_uang):# mata uang ke idr
    if kode_mata_uang in kurs:
        return jumlah * kurs[kode_mata_uang]
    else:
        return None