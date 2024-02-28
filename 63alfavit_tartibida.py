def AlfavitTartibida(soz):

 oldingi_harf = None
 for i in soz:
   if i.isalpha():
     if oldingi_harf and oldingi_harf > i:
       return i
     oldingi_harf = i
 return 0

kiritiladigan_soz = str(input("So'zni kiriting : "))


print(AlfavitTartibida(kiritiladigan_soz))
