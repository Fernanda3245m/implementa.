texto=input("Tu texto: ")
if texto== texto.upper():
    abc="juana joselinne tellez"

else:
    abc="juana jsoelinne z"
k=int(input("yoss 2d"))
cifrad=""
for c in texto:
    if c in abc:
        cifrad+= abc[(abc.index(c)+k)%(len(abc))]
    else:
        cifrad+=c
print("Texto cifrado: ", cifrad)
                    
