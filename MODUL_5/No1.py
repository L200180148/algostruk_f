from Modul5Keg import *

class MhsTif(object):
    def __init__(self,nama,nim,kota,uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku
    def __str__(self):
        s = self.nama + ', nim ' + str(self.nim)\
            + '. Tinggal di ' + self.kota\
            + '. Uang saku Rp ' + str(self.uangSaku)\
            + '. tiap bulannya.'
        return s

c0 = MhsTif("DDhimas", 148, "Sragen", 200000)
c1 = MhsTif("Rohmad", 101, "Riau", 190000)
c2 = MhsTif("Aezo", 65, "Sragen", 220000)
c3 = MhsTif("Iqbal", 155, "Wonogiri", 215000)
c4 = MhsTif("Fanditol", 118, "Sragen", 150000)
c5 = MhsTif("Wahyu", 31, "Salatiga", 250000)
c6 = MhsTif("Rama", 213, "Klaten", 245000)
c7 = MhsTif("Hanan", 170, "Wonogiri", 245000)
c8 = MhsTif("Mujab", 139, "Rembang", 245000)
c9 = MhsTif("Saipuul", 164, "Karanganyar", 270000)
c10 = MhsTif("Ilham", 129, "Purwodadi", 265000)

Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

def urutkanNim(list):
    NIM = []
    for i in list:
        NIM.append(i.nim)
    insertionSort(NIM)
    return NIM
