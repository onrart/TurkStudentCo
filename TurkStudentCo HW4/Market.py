import os

class Market:
    def __init__(self, dosya_adi="product.txt"):
        self.dosya_adi = dosya_adi

        if not os.path.exists(dosya_adi):
            print(f"{dosya_adi} dosyası bulunamadı! Dosya oluşturuldu.")
            with open(dosya_adi, encoding="utf-8", mode="w") as dosya:
                pass  # Boş dosya oluşturuldu
        else:
            print(f"{dosya_adi} dosyası mevcut.")

    def urun_ekle(self, ürün_adi, kategori, fiyat, stok_miktari):
        with open(self.dosya_adi, encoding="utf-8", mode="a") as dosya:
            dosya.write(f"{ürün_adi},{kategori},{fiyat},{stok_miktari}\n")
            print(f"Ürün eklendi: {ürün_adi}, {kategori}, {fiyat}, {stok_miktari}")

    def urun_sil(self):
        self.urunlistele()
        satir_numarasi = int(input("Silinecek ürünün satır numarasını giriniz: "))
        with open(self.dosya_adi, encoding="utf-8", mode="r") as dosya:
            satirlar = dosya.readlines()

        if 0 <= satir_numarasi < len(satirlar):
            silinecek_satir = satirlar.pop(satir_numarasi)
            print(f"Silinen satır: {silinecek_satir.strip()}")
        else:
            print("Geçersiz satır numarası!")

        with open(self.dosya_adi, encoding="utf-8", mode="w") as dosya:
            dosya.writelines(satirlar)
            print("Dosya güncellendi.")

    def urunlistele(self):
        try:
            with open(self.dosya_adi, encoding="utf-8", mode="r") as dosya:
                satirlar = dosya.read().splitlines()
                if not satirlar:
                    print("Dosya boş, listelenecek ürün yok.")
                    return

                for index, satir in enumerate(satirlar, start=1):
                    ürün_adi, kategori, fiyat, stok_miktari = satir.split(",")
                    print(f"{index}: Ürün Adı: {ürün_adi}, Kategori: {kategori}, Fiyat: {fiyat}, Stok Miktarı: {stok_miktari}")
        except FileNotFoundError:
            print(f"{self.dosya_adi} dosyası bulunamadı!")

if __name__ == "__main__":
    market = Market()

    # Ürün ekleme
    market.urun_ekle("ürün1", "kategori1", 10, 5)
    market.urun_ekle("ürün2", "kategori2", 20, 10)
    market.urun_ekle("ürün3", "kategori3", 30, 15)

    # Ürün listeleme
    market.urunlistele()

    # Ürün silme
    market.urun_sil()
    market.urunlistele()
