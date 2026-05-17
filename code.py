def arrays():
    array=[1,10,20,2,32,23]
    array.sort()
    array.reverse()
    for i in array:
        print(i)
########################
def esPalindromo(palabra):
    # palabra=str(input("Escribe una palabra: "))
    if palabra in palabra[::-1]:
        print("Palindromo")
    else:
        print("Falso")
    
