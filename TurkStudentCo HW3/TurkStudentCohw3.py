class Film:
    def __init__(self, isim, yonetmen, tur, yil) -> None:
        self.isim = isim
        self.yonetmen = yonetmen
        self.tur = tur
        self.yil = yil

    def __str__(self):
        return f"{self.isim} ({self.yil}) - {self.tur} - Yönetmen: {self.yonetmen}"

class FilmYonetim:
    def __init__(self) -> None:
        self.filimler = []

    def film_ekle(self, film):
        if isinstance(film, Film):
            self.filimler.append(film)
            return f"{film.isim} eklendi"
        else:
            return "Eklenecek nesne bir Film olmalı!"

    def film_sil(self, film):
        if film in self.filimler:
            self.filimler.remove(film)
            return f"{film.isim} silindi"
        else:
            return "Silinecek film bulunamadı!"

    def filmlistele(self):
        if not self.filimler:
            return "Listelenecek film yok!"
        else:
            film_listesi = "Filmler:\n"
            for film in self.filimler:
                film_listesi += f"{film}\n"
            return film_listesi

# Kullanım örneği
film_yonetim = FilmYonetim()

# Filmleri ekle
godfather = Film("The Godfather", "Francis Ford Coppola", "Crime, Drama", 1972)
print(film_yonetim.film_ekle(godfather))

leon = Film("The Lion King", "Jon Favreau", "Animation, Adventure, Drama", 2019)
print(film_yonetim.film_ekle(leon))

wolfofws = Film("The Wolf of Wall Street", "Martin Scorsese", "Biography, Crime, Drama", 2013)
print(film_yonetim.film_ekle(wolfofws))

# Filmleri listele
print(film_yonetim.filmlistele())

# Film sil
print(film_yonetim.film_sil(godfather))

# Güncel listeyi tekrar göster
print(film_yonetim.filmlistele())
