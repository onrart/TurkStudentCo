from Market import Market

market = Market()
while True:
    print("\nMenu:")
    print("1. Ürün Ekle")
    print("2. Ürün Sil")
    print("3. Ürün Listele")
    print("4. Cikis")

    secim = input("Seciminiz: ")

    if secim == "1":
        market.urun_ekle()
    elif secim == "2":
        
        market.urun_sil()
    elif secim == "3":
        
        market.urunlistele()
    elif secim == "4":
        print("Program sonlandırılıyor...")
        del market
        break