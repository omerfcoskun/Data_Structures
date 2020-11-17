kaynak = open("source.c", "r") #Kaynak dosyayı yalnızca okuma amaçlı olarak açıyoruz.
hedef = open("target.c", "w") #Üstüne yazma amacıyla sıfırdan bir hedef dosyası oluşturuyoruz.

satir = kaynak.readlines() #Kaynak dosyadaki tüm satırları, bir diziye aktarıyoruz.
kaynak.close() #Artık kaynak dosyasıyla bir işimiz olmadığından, onu kapatıyoruz.

tab = 0 #Kodların ilk satırlarına "tab" yani çoklu boşluk eklemeyiz. O yüzden bu değer sıfır olarak başlıyor.

for i in range(0, len(satir)): #Her satırı okuyacak ve dizi sona erdiğinde çalışmayı durduracak bir döngü yaratıyoruz.

    if satir[i-1] == "{\n": #Bir önceki satırda parantez açılmış ise, boşluk sayısını artırıyoruz.
        tab += 1
    elif satir[i] == "}\n": #Mevcut satırda parantez kapanmış ise, boşluk sayısını azaltıyoruz.
        tab -= 1
    else: #Süslü paranteze rastalamadığımız durumda, aynı boşluk sayısıyla devam ediyoruz.
        pass

    for j in range(0,tab): #Satırdaki içeriğin önüne doğru sayıda boşluk bırakacak yeni bir döngü oluşturuyoruz.
        hedef.write("\t")

    hedef.write(satir[i]) #Ardından o satırın içeriğini yazıyoruz.

hedef.close() #Kaynak dosyamızda olduğu gibi, hedef dosyamızı da kapatıyoruz.
