# -*- coding: utf-8 -*-
"""LaPrak Algo.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Kz5fp47OwytxgVPMTDEdLfjf12VxzyaE
"""

panjang = int(input("Panjang Ruangan: "))
lebar = int(input("Lebar Ruangan: "))
satuan = input("Masukan satuan (meter/inci): ")
luas = panjang * lebar
luas_secara_meter = (f"Luas ruangan adalah: {luas} meter persegi")
luas_secara_inci = (f"Luas ruangan adalah: {luas} inci persegi")
tidak_valid = "Mohon maaf satuan tidak valid. Harap ganti 'meter atau inci'."
if satuan == "meter":
  print(luas_secara_meter)
elif satuan == "inci":
  print(luas_secara_inci)
else:
  print(tidak_valid)