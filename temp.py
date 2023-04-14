"""1-)başla
2-)isim soyisim girdir
3-)kayıt yaptır
4-)ihtiyaç bildirimi var mı?
a-)varsa 5e git
b-)yoksa 14e git
5-)kayıtlı kullanıcılara ihtiyaç bildirimi gönder
6-)verilen eşyaların adını yaz
7-)eşya toplama alanlarını yaz
8-)eşya toplama alanlarından birini seç
9-)gidebileceği şehirleri yazdır
10-)gidebileceği şehirlerden birini seçtir
11-)aracın bilgilerini girdir
12-)araç ulaştığında eşyaların şehrin hangi bölgesinde olduğunu yaz
13-)yeni ihtiyaç var mı?
a-)varsa 5e git
b-)yoksa 14e git
14-)bitir
"""

"""1-Sisteme Üye Ol
2-Sisteme Giriş Yap
3-Şifremi Unuttum olmalıdır
4-üye olmadan ihtiyaçlara bakma
5- şu anki yoldaki araçları takip etme
6-bağış yapma
7-toplanma yerlerini öğrenme
"""
print("SEÇİMLER")
liste=["üye ol","giriş yap","unuttum","ihtiyaçlara bakma","araçları takip etme","bağış yapma","ihtiyaç toplama yerlerini öğrenme"]
print(liste)
secim=input("seçiminiz nedir \n")
if secim==liste[0]:
    print("üye olacaksınız")
    input("isminizi giriniz  ")
    input("soyisminizi giriniz  ")
    input("epostanızı giriniz  ")
    input("şifrenizi belirleyiniz  ")
    print("başarıyla üye oldunuz")
    
elif secim==liste[1]:
    input("kullanıcı adınızı giriniz ")
    input("şifrenizi giriniz ")
    
elif secim==liste[2]:
    input("e postanızı giriniz   ")
    print("e postanıza yeni şifreniz 5 saniye içinde atılıcaktır ")
    input("yeni şifreyi giriniz  ")
    print("hesabınıza girilmiştir")
    
elif secim==liste[3]:
    print("ihtiyaç ekranına yönlendiriliyosunuz")
    
elif secim==liste[4]:
    print("haritalara yönlendiriliyosunuz")
    
elif secim==liste[5]:
    print("bağış sayfasına yönlendiriliyosunuz")
    
elif secim==liste[6]:
    print("ihtiyaçların toplanma yerlerini gösteren haritarala yönlendiriliyosunuz")
else:
    print("böyle bir seçim yok")
    
    
    
    
    
    
    
    
    
    
    
    
    
    