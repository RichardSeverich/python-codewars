#Given a string str, reverse it omitting all non-alphabetic characters.
#Example
#For str = "krishan", the output should be "nahsirk".
#For str = "ultr53o?n", the output should be "nortlu".

def reverse_letter(string):
    soloLetras = []
    for char in string:
            if char.isalpha():
                soloLetras.append(char)
    soloLetras.reverse()
    invertido = "".join(soloLetras)
    return invertido