# TurkStudentCo

### Soru-1: Kullanıcıdan iki sayı alarak bu sayıları toplayan bir programın pseudo kodu

````
Başla
    Kullanıcıdan birinci sayıyı al ve birinci_sayı değişkenine ata
    Kullanıcıdan ikinci sayıyı al ve ikinci_sayı değişkenine ata
    toplam = birinci_sayı + ikinci_sayı
    Ekrana toplamı yazdır
Bitir



````
### Soru-2: 1'den 100'e kadar olan sayıları toplayan bir programın pseudo kodu
````
Başla
    toplam = 0
    i = 1
    while i ≤ 100
        toplam = toplam + i
        i = i + 1
    Ekrana toplamı yazdır
Bitir
````

### Soru-3: Kullanıcıdan alınan bir sayının asal olup olmadığını bulan bir programın pseudo kodu

```
Başla
    Kullanıcıdan bir sayı al ve sayı değişkenine ata
    Eğer sayı ≤ 1 ise
        Ekrana "Asal değil" yazdır
        Bitir
    else
        for i = 2 to (sayı - 1)
            Eğer sayı mod i = 0 ise
                Ekrana "Asal değil" yazdır
                Bitir
        Ekrana "Asal" yazdır
Bitir  
                         
```
    

### Soru-4: Bir dizideki (array) elemanların tekrar edip etmediğini kontrol eden bir programın pseudo kodu

```
Başla
    Kullanıcıdan bir dizi al ve dizi değişkenine ata
    Boş bir sözlük oluştur ve sözlük_değişkenine ata
    for i = 0 to (dizi uzunluğu - 1)
        Eğer dizi[i] sözlük_değişkeninde varsa
            Ekrana "Dizide tekrar eden eleman var" yazdır
            Bitir
        aksi halde
            sözlük_değişkenine dizi[i] değerini ekle
    Ekrana "Dizide tekrar eden eleman yok" yazdır
Bitir
```
