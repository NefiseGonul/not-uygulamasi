def not_gir():
     ad = input("öğrenci adi : ")
     soyad = input("öğrenci soyadı: ")
     not1 = input("not1: ")
     not2 = input("not2: ")
     not3 = input("not3: ")
     with open("sinav_notlari.txt" , "a" , encoding = "utf-8") as file:
           file.write(ad + ' , ' + soyad + ' '+ not1 + '' +',' +not2 + ','+not3 +'\n' )
def notlari_oku():
     with open("sinav_notlari.txt" , "r" , encoding = "utf-8") as file:
          for satir in file :
               print(satir)
def notlari_kaydet(): 
     with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        satirlar = file.readlines()

     with open("sonuclar.txt", "w", encoding="utf-8") as file2:
        for satir in satirlar:
            bilgi = satir.strip().split(",")

            not1 = int(bilgi[2])
            not2 = int(bilgi[3])
            not3 = int(bilgi[4])

            ortalama = (not1 + not2 + not3) / 3

            if ortalama >= 50:
                durum = "Gecti"
            else:
                durum = "Kaldi"

            file2.write(bilgi[0] + " " + bilgi[1] + " - " + durum + "\n")

     print("Kaydedildi.")

while True:
    islem=input("1-not gir\n 2-notları oku\n 3-notları kaydet\n 4-cıkış\n")

    if islem == "1":
         not_gir() 
    elif islem=="2":
         notlari_oku()
    elif islem =="3":
         notlari_kaydet()
    else :
         break