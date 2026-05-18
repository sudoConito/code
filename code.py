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
esPalindromo("ReCoNoCeR")  
contadorDeVocales("etcetera")
prueba()