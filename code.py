def arrays():
    array=[1,10,20,2,32,23]
    array.sort()
    array.reverse()
    for i in array:
        print(i)
########################
def esPalindromo(palabra):
    # palabra=str(input("Escribe una palabra: "))
    if palabra.lower() in palabra[::-1].lower():
        print("Palindromo")
    else:
        print("Falso")
def contadorDeVocales(palabra1):
    vocales=0
    for i in palabra1:
        if i in "aeiou":
            vocales+=1
    print(f"Escribiste '{palabra1}'. En tu palabra\nhay {vocales} vocales en total.")
def prueba():
    resultado=0
    for x in [3,3,5]:
        if x>=3:
            resultado-=x
        else:
            resultado+=x
    print(resultado)
def par_impar(numero):
    if numero%2==0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")
###############        
# esPalindromo("ReCoNoCeR")  
# contadorDeVocales("etcetera")
# prueba()
# par_impar(4)
###############
# font normal: Consolas, 'Courier New', monospace
#font pixel: Monocraft

#git config --global user.name "TuNombreDeUsuario"
#git config --global user.email "tu-correo@email.com"
#####################################################

def start():
    print("start")
    return
def update():
    print("hola")
    return
def main():
    start()
    update()
main()