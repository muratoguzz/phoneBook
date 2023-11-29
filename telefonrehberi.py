class Entry():
    def __init__(self, isimSoyisim, telNo, mail):
        self.isimSoyisim=isimSoyisim
        self.telNo=telNo
        self.mail=mail

Rehber=[]

def butunKayitlariGoster():
    print("----Bütün Kayıtlar----")
    for i, kisi in enumerate(Rehber):
        print(f"{i+1}. İsim Soyisim: {kisi.isimSoyisim}  Numara: {kisi.telNo}  Mail adresi: {kisi.mail}")

def kayitEkleme():
    print("----Kayıt Ekleme----")
    isimSoyisim=input("İsim giriniz: ")
    telNo=input("Numara giriniz: ")
    mail=input("Mail adresi giriniz: ")
    kisi= Entry(isimSoyisim, telNo, mail)
    Rehber.append(kisi)
    print("Kayıt eklendi..!")

def kayitCikarma():
    print("----Kayıt Çıkar----")
    isimSoyisim=input("Rehberden çıkarmak istediğiniz kişinin ismini giriniz: ")
    Rehber2 = [kisi for kisi in Rehber if kisi.isimSoyisim == isimSoyisim]
    if not Rehber2:
        print("Aradığınız kişi rehberde bulunamadı")
    else:
        print("İsime göre arama: ")
        for i, kisi in enumerate(Rehber2):
            print(f"{i+1}. İsim Soyisim: {kisi.isimSoyisim}  Numara: {kisi.telNo}  Mail adresi: {kisi.mail}")
            sil=input("Silme işlemini onaylıyor musunuz? (evet/hayır)")
            if sil=="evet":
                Rehber.remove(kisi)
                print("Kayıt silindi")
            else:
                print("Ana menüye dönüyorsunuz")

def kayitGüncelleme():
    print("----Kayıt Güncelleme----")
    isimSoyisim=input("Bilgilerini güncellemek istediğiniz kişinin ismini giriniz: ")
    Rehber2 = [kisi for kisi in Rehber if kisi.isimSoyisim == isimSoyisim]
    if not Rehber2:
        print("Aradığınız kişi rehberde bulunamadı")
    else:
        print("İsime göre arama: ")
        for i, kisi in enumerate(Rehber2):
            print(f"{i+1}. İsim Soyisim: {kisi.isimSoyisim}  Numara: {kisi.telNo}  Mail adresi: {kisi.mail}")
            guncelle=input("Güncelleme işlemini onaylıyor musunuz? (evet/hayır)")
            if guncelle == "evet":
                guncellenecekAlan = input('''Güncellenecek kısım:
1. İsim 
2. Numara
3. Mail
''')
                if guncellenecekAlan == "1":
                    yeniIsim = input("Yeni ismi giriniz: ")
                    kisi.isimSoyisim = yeniIsim
                    print("İsim güncellendi")
                elif guncellenecekAlan == "2":
                    yeniTelNo = input("Yeni numarayı giriniz: ")
                    kisi.telNo = yeniTelNo
                    print("Numara güncellendi")
                elif guncellenecekAlan == "3":
                    yeniMail = input("Yeni mail adresini giriniz: ")
                    kisi.mail = yeniMail
                    print("Mail adresi güncellendi")
            
                Rehber.remove(kisi)
                Rehber.append(kisi)
                print("Kayıt güncellendi")

while True:
    print("----Telefon Rehberi Menüsüne Hoş Geldiniz----")
    print("1. Bütün Kayıtları Göster")
    print("2. Kayıt Ekle")
    print("3. Kayıt Çıkar")
    print("4. Kayıt Güncelle")
    print("5. Çıkış")

    menu=input()

    if menu=="1":
        butunKayitlariGoster()
    
    elif menu=="2":
        kayitEkleme()

    elif menu=="3":
        kayitCikarma()
    
    elif menu=="4":
        kayitGüncelleme()
    
    elif menu=="5":
        print("Güle Güle..:)")
        break

    else:
        print("Geçersiz işlem yaptınız")
            
           
                









          


