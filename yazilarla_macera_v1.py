import time

# Oyuncu sınıfı tanımlama
class Oyuncu:
    def __init__(self):
        self.envanter = []

    def esya_ekle(self, esya):
        self.envanter.append(esya)

    def esya_cikar(self, esya):
        self.envanter.remove(esya)


# Oda sınıfı tanımlama
class Oda:
    def __init__(self, ad, aciklama):
        self.ad = ad
        self.aciklama = aciklama
        self.esyalar = []
        self.bagli_odalar = {}

    def odayi_bagla(self, yon, oda):
        self.bagli_odalar[yon] = oda

    def esya_ekle(self, esya):
        self.esyalar.append(esya)

    def esya_cikar(self, esya):
        self.esyalar.remove(esya)


# Esya sınıfı tanımlama
class Esya:
    def __init__(self, ad, aciklama):
        self.ad = ad
        self.aciklama = aciklama


# Odaları ve esyaları oluşturma
mutfak = Oda("Mutfak", "Geniş ve iyi donanımlı bir mutfak.")
oturma_odasi = Oda("Oturma Odası", "Şömineli rahat bir oturma odası.")
yatak_odasi = Oda("Yatak Odası", "Büyük bir yatakla donatılmış rahat bir yatak odası.")
bahce = Oda("Bahçe", "Renkli çiçeklerle süslü güzel bir bahçe.")

anahtar = Esya("Anahtar", "Parlak altın bir anahtar.")
kilic = Esya("Kilic", "Keskin ve sağlam bir kilic.")


# Oda bağlantılarını ayarlama
mutfak.odayi_bagla("güney", oturma_odasi)
oturma_odasi.odayi_bagla("kuzey", mutfak)
oturma_odasi.odayi_bagla("batı", yatak_odasi)
yatak_odasi.odayi_bagla("doğu", oturma_odasi)
oturma_odasi.odayi_bagla("doğu", bahce)
bahce.odayi_bagla("batı", oturma_odasi)


# Esyaları odalara ekleme
mutfak.esya_ekle(anahtar)
yatak_odasi.esya_ekle(kilic)


# Oyun fonksiyonları
def gecikmeli_yaz(text, gecikme=1.5):
    print(text)
    time.sleep(gecikme)


def oyuncu_komutu_al():
    return input(">> ").strip().lower()


def oyuncu_hareketi_yonet(oyuncu, mevcut_oda, yon):
    if yon in mevcut_oda.bagli_odalar:
        return mevcut_oda.bagli_odalar[yon]
    else:
        gecikmeli_yaz("Bu yöne gidemezsiniz!")
        return mevcut_oda


def oyuncu_etkilesimi_yonet(oyuncu, mevcut_oda, komut):
    if komut.startswith("al "):
        esya_ad = komut[3:]
        for esya in mevcut_oda.esyalar:
            if esya.ad.lower() == esya_ad:
                oyuncu.esya_ekle(esya)
                mevcut_oda.esya_cikar(esya)
                gecikmeli_yaz(f"{esya_ad} eşyasını aldınız.")
                return
        gecikmeli_yaz("Eşya bulunamadı!")
    elif komut.startswith("bırak "):
        esya_ad = komut[6:]
        for esya in oyuncu.envanter:
            if esya.ad.lower() == esya_ad:
                oyuncu.esya_cikar(esya)
                mevcut_oda.esya_ekle(esya)
                gecikmeli_yaz(f"{esya_ad} eşyasını bıraktınız.")
                return
        gecikmeli_yaz("Envanterinizde eşya bulunamadı!")
    else:
        gecikmeli_yaz("Geçersiz komut!")


# Oyun başlatma
def ana():
    oyuncu = Oyuncu()
    mevcut_oda = mutfak

    gecikmeli_yaz("Metin Tabanlı Macera Oyununa Hoş Geldiniz!")
    gecikmeli_yaz("Kendinizi bir mutfakta buldunuz. Keşfedin ve hazineler bulun!")
    gecikmeli_yaz("Komutlar: 'kuzey', 'güney', 'doğu', 'batı', 'al eşya', 'bırak eşya', 'çıkış'")

    # Oyun döngüsü
    while True:
        gecikmeli_yaz("\n" + "=" * 30)
        gecikmeli_yaz(f"{mevcut_oda.ad}\n{mevcut_oda.aciklama}")
        komut = oyuncu_komutu_al()

        if komut == "yardım":
            gecikmeli_yaz("Komutlar: 'kuzey', 'güney', 'doğu', 'batı', 'al eşya', 'bırak eşya', 'çıkış'")
        elif komut == "çıkış":
            gecikmeli_yaz("Oynamak için teşekkürler! Hoşça kal!")
            break
        elif komut in ["kuzey", "güney", "doğu", "batı"]:
            mevcut_oda = oyuncu_hareketi_yonet(oyuncu, mevcut_oda, komut)
        else:
            oyuncu_etkilesimi_yonet(oyuncu, mevcut_oda, komut)


if __name__ == "__main__":
    ana()
