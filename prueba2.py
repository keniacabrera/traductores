import string
letras=string.printable
clave=raw_input("ingrese una clave de 4 digitos >>")
while len(clave)!=4 :
  print  "\nError tiene que ser uan clave de 4 digitos!\n"
  clave=raw_input("ingrese una clave de 4 digitos >>")
clave_correcta=False
for i in letras:
  if clave_correcta:break
  for j in letras:
    if clave_correcta:break
    for k in letras:
      if clave_correcta:break
      for m in letras:
        if i+j+k+m==clave:
          clave_correcta=True
          print "\n\n\n\nla clave es: "+i+j+k+m
          break
        else:
          print "clave erronea generada "+i+j+k+m
