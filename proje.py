def fonk1():

    print("ihtiyaç ekranına yönlendiriliyosunuz")
    ihtiyaç={"battaniye": "1000 adet",
     "su":"5000 adet",
     "hazır çorba":"100 adet",
     "mont":"2000 adet"}
    for i in ihtiyaç.keys():
        print("depomuzda",ihtiyaç[i],i,"ihtiyaç vardır")
    
    
      
        
        
def fonk2():
   while True:
    print("araç bilgilerine yönlendiriliyosunuz")
    şoförler=["ahmet","mehmet","ayşe"]
    print(şoförler)
    numara={"ahmet":"05000000000","mehmet":"05000000001","ayşe":"05000000002"}
    isim=input("aradığınız ismi giriniz\n")
    if isim in numara:
      print("kişinin numarası",numara[isim],"dır")
      break
    else:
     print("böyle bir şoför yoktur tekrar deneyin")
     continue
    
      
def fonk3():
    print("bağış sayfasına yönlendiriliyosunuz")
    iban={"a bankası":"0000000000",
          "b bankası":"0000001",
          "c bankası":"000002",
          "d bankası":"0000003"}
    bankaliste=["a bankası","b bankası","c bankası","d bankası"]
    print(bankaliste)
    banka=input("banka seçiniz \n")
    if banka in iban: 
         print("bankanın ibanı",iban[banka],"dır")
    else:
        print("bu bankayla çalışmıyoruz")
    
         
def fonk4():
    print("ihtiyaçların toplanma yerlerini gösteren sayfaya yönlendiriliyosunuz")
    adres={"şanlıurfa":"shshs mahallesi","hatay":"kfjkdjd mahallesi","adana":"aaa mahallesi","diyarbakır":"bbb mahallesi","gaziantep":"ccc mahallesi"}
    şehir=["şanlıurfa","hatay","adana","diyarbakır","gaziantep"]
    print(şehir)
    sehir=input("aradığınız şehri giriniz\n")
    if sehir in adres:
        print("aradığınız adres",adres[sehir],"dır")
    else:
     print("bu şehir yoktur")    
    
    
        
      


cevap=input("kullanıcı mısınız yönetici mi? ")

if cevap=="kullanıcı":
     print("ekrana yönlendiriliyosunuz")
     
     print("GİRİŞ SEÇİMLERİ")
     liste=["üye ol","giriş yap","unuttum"]
     print(liste)
     
     secim=input("seçiminiz nedir \n")
    
     if secim==liste[0]:
         sözlük={} 
         print("üye olacaksınız")
         isim=input("isminizi giriniz  ")
         degerler=[]
         soyisim=input("soyisminizi giriniz  ")
         eposta=input("epostanızı giriniz  ")
         while True:
             sifre=input("şifrenizi belirleyiniz  ")
             if( len(sifre)>1 and len(sifre)<8):
               yazi="şifre {} dır"
               yazi=yazi.format(sifre)
               print(yazi,"şifre geçerli")
               degerler.append(soyisim)
               degerler.append(eposta)
               degerler.append(sifre)
               sözlük.setdefault(isim,degerler)
               print(sözlük)
               break
             else: 
               print("sifre gecersiz")
               continue
         
        
         print("başarıyla üye oldunuz")
         while True:
          print("ana menüye yönlendiriliyosunuz")
          print("ANA MENÜ")
          liste2=["ihtiyaçlara bakma","araç bilgilerini öğrenme","bağış yapma","ihtiyaç toplama yerlerini öğrenme","çıkış yapma"]
          print("Aşağıdaki seçeneklerden birini giriniz:",liste2)
          secim2=input("seçiminiz nedir \n")
         
          if secim2==liste2[0]:
           fonk1()
           a=input("ana menüye mi gitmek istersiniz yoksa çıkış yapmak mı istersiniz")
           if a=="ana menü":
               continue
           else:
               print("çıkış yapıyosunuz")
               break
           

          elif secim2==liste2[1]:
           fonk2()
           a=input("ana menüye mi gitmek istersiniz yoksa çıkış yapmak mı istersiniz")
           if a=="ana menü":
               continue
           else:
               print("çıkış yapıyosunuz")
               break
           

          elif secim2 ==liste2[2]:
           fonk3()
           a=input("ana menüye mi gitmek istersiniz yoksa çıkış yapmak mı istersiniz")
           if a=="ana menü":
               continue
           else:
               print("çıkış yapıyosunuz")
               break

          elif secim2==liste2[3]:
           fonk4()
           a=input("ana menüye mi gitmek istersiniz yoksa çıkış yapmak mı istersiniz")
           if a=="ana menü":
               continue
           else:
               print("çıkış yapıyosunuz")
               break
           
          else:
           print("böyle bir seçenek yok")
           continue
      
        
     elif secim==liste[1]:
       input("kullanıcı adınızı giriniz ")
       input("şifrenizi giriniz ")
      
       print("ana menüye yönlendiriliyosunuz")
       print("ANA MENÜ")
       while True:
        liste2=["ihtiyaçlara bakma","araç bilgilerini öğrenme","bağış yapma","ihtiyaç toplama yerlerini öğrenme","çıkış yapma"]
        print("Aşağıdaki seçeneklerden birini giriniz:",liste2)
        secim2=input("seçiminiz nedir \n")
        if secim2==liste2[0]:
         fonk1()
         a=input("ana menüye mi gitmek istersiniz yoksa çıkış yapmak mı istersiniz")
         if a=="ana menü":
             continue
         else:
             print("çıkış yapıyosunuz")
             break
        

        elif secim2==liste2[1]:
         fonk2()
         a=input("ana menüye mi gitmek istersiniz yoksa çıkış yapmak mı istersiniz")
         if a=="ana menü":
             continue
         else:
             print("çıkış yapıyosunuz")
             break

        elif secim2 ==liste2[2]:
         fonk3()
         a=input("ana menüye mi gitmek istersiniz yoksa çıkış yapmak mı istersiniz")
         if a=="ana menü":
             continue
         else:
             print("çıkış yapıyosunuz")
             break

        elif secim2==liste2[3]:
         fonk4()
         a=input("ana menüye mi gitmek istersiniz yoksa çıkış yapmak mı istersiniz")
         if a=="ana menü":
             continue
         else:
             print("çıkış yapıyosunuz")
             break
         
        else:
         print("böyle bir seçenek yoktur tekrar deneyiniz")
         continue
   

     elif secim==liste[2]:
         input("kullanıcı adınızı giriniz   ")
         import sqlite3
         sq=sqlite3.connect("kullanicilar.db")
         imlec2=sq.cursor()

         sorgu3="CREATE TABLE IF NOT EXISTS 'kullanici'('kullaniciadi','sifre')"
         imlec2.execute(sorgu3)
        
         imlec2.execute("SELECT * FROM kullanici WHERE kullaniciadi = 'ahmet_bir'")
         ver=imlec2.fetchall()
         print("şifreniz budur: ")
         print(ver)
         while True:
          print("ana menüye yönlendiriliyosunuz")
          print("ANA MENÜ")
          liste2=["ihtiyaçlara bakma","araç bilgilerini öğrenme","bağış yapma","ihtiyaç toplama yerlerini öğrenme","çıkış yapma"]
          print("Aşağıdaki seçeneklerden birini giriniz:",liste2)
          secim2=input("seçiminiz nedir \n")
         
          if secim2==liste2[0]:
           fonk1()
           a=input("ana menüye mi gitmek istersiniz yoksa çıkış yapmak mı istersiniz")
           if a=="ana menü":
               continue
           else:
               print("çıkış yapıyosunuz")
               break
           

          elif secim2==liste2[1]:
           fonk2()
           a=input("ana menüye mi gitmek istersiniz yoksa çıkış yapmak mı istersiniz")
           if a=="ana menü":
               continue
           else:
               print("çıkış yapıyosunuz")
               break

          elif secim2 ==liste2[2]:
           fonk3()
           a=input("ana menüye mi gitmek istersiniz yoksa çıkış yapmak mı istersiniz")
           if a=="ana menü":
               continue
           else:
               print("çıkış yapıyosunuz")
               break

          elif secim2==liste2[3]:
           fonk4()
           a=input("ana menüye mi gitmek istersiniz yoksa çıkış yapmak mı istersiniz")
           if a=="ana menü":
               continue
           else:
               print("çıkış yapıyosunuz")
               break
           
          else:
           print("böyle bir seçenek yok tekrar deneyin")
           continue
     else:
            print("böyle bir seçim yok")
            
if cevap=="yönetici":
    print("giriş yapınız")
    ad=input("adınız nedir\n")
    for i in range(3):
     if ad=="berna" or ad=="murat":
         kod=input("kodu giriniz\n")
         if kod=="1234":
             print("doğru")
             break
         else:
             print("yanlış'3 yanlış cevaptan sonra sistemden otomatik çıkarsınız'")
             continue
     else:
         print("böyle bir yöneticimiz yoktur")
         break
     
    while True:
      print("ekrana yönlendiriliyosunuz")
      liste3=["(1)kullanıcıların bilgilerini görüntüle","(2)soförlerin bilgilerini görüntüle","(3)yapılan bağışları görüntüle"]
      print(liste3)
      a=input("seçiminiz nedir?  ")
      
      if a =="1":
         print("mevcut kullanıcılarımızla ilgili bilgilere gidiyosunuz")
         import pandas as pd

         test=pd.read_csv("c.csv")
         print(test)
         b=input("ekrana mı gitmek istersiniz yoksa çıkış yapmak mı istersiniz\n")
         if b=="ekran":
             continue
         else:
             print("çıkış yapıyosunuz")
             break
       
      elif a=="2":
       import sqlite3
       vt=sqlite3.connect("soforlerinbilgileri.db")
       imlec=vt.cursor()

       sorgu="CREATE TABLE IF NOT EXISTS 'bilgiler'('isim','soyisim','sehir','konum')"
       imlec.execute(sorgu)

       sorgu1="select * from bilgiler"
       imlec.execute(sorgu1)
       veri=imlec.fetchall()
       print(veri)
       b=input("ekrana mı gitmek istersiniz yoksa çıkış yapmak mı istersiniz\n")
       if b=="ekran":
               continue
       else:
               print("çıkış yapıyosunuz")
               break  
           
      elif a=="3":
          print("bağış ekranına yönlendiriliyosunuz")
          import pandas as pd
          sozluk = {'İsim':pd.Series(['ada','ada','ayşe','ayşe','ayşe','mehmet']),
           'bağış':pd.Series(['para','battaniye','su','çocuk bezi','para','mont']),
           'Tarih':pd.Series(['06.02.2023','06.02.2023','10.02.2023','10.02.2023','10.02.2023','20.02.2023']),
           'Yaş':pd.Series([25, None, 40, None, None, 17]),
           'meslek':pd.Series(['avukat','avukat','kuaför','kuaför','kuaför','öğrenci'])}
           
          df = pd.DataFrame(sozluk)

          a=df.head(6)
          print(a)
          
          seç=input("yaşların aritmetik ortalamasını öğrenmek ister misiniz? ")
          if seç=="evet":
           b=df['Yaş'].mean()
           print("aritmetik ortalama", b, "dır")
           
          else:
              break
          
          seç2=input("yaşların grafiğini görmek ister misiniz?")
          if seç2=="evet":
            df.plot(x='İsim', y='Yaş', style='*')
          else:
              break
          
          b=input("ekrana mı gitmek istersiniz yoksa çıkış yapmak mı istersiniz\n")
          if b=="ekran":
                  continue
          else:
                  print("çıkış yapıyosunuz")
                  break  
              

         

             
