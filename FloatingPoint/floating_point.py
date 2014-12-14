##
# 
#  Convertire in virgola mobile a mantissa e esponente parametrici
#
#
# Gabriele Proietti Mattia - gabry.gabry@hotmail.it
# Università La Sapienza di Roma
# Facoltà di Ingegneria Informatica
# 2014/15
#
#############################

## ieeeConvert
# @param n Number to convert
# @param nCifreExp Number of exponent
# @param nCifreMantissa Number of mantissa
#
def ieeeConvert(n, nCifreExp, nCifreMantissa) :
    ## PREPARO IL NUMERO
    # Splitto il numero
    listaNumero   = n.split(".")

    # Se è un intero non ha parte decimale la aggiungo
    if len(listaNumero) == 1 :
        listaNumero.append(0)
    
    parteIntera   = int(listaNumero[0])
    parteDecimale = int(listaNumero[1])

    ## PARTE INTERA
    # Converto il numero Intero in binario
    parteInteraBin = bin(parteIntera)
    parteInteraBin = str(parteInteraBin)[parteInteraBin.find("b") + 1:] #<<================ PARTE INTERA DEL NUMERO


    ## PARTE DECIMALE
    # Converto la parte decimale in binario fino a che serve per la mantissa
    parteDecimaleBin = ""
    nDaMoltiplicare = float("0." + str(parteDecimale))

    # Il ciclo deve fermarsi o quando le cifre della mantissa sono abbastanza, oppure se n = 1
    while len(parteInteraBin) + len(parteDecimaleBin) < (nCifreMantissa +1) or nDaMoltiplicare == 1 :
        nDaMoltiplicare = nDaMoltiplicare *2
        if nDaMoltiplicare < 1 :
            parteDecimaleBin += "0"
        else :
            parteDecimaleBin += "1"
            nDaMoltiplicare  -= 1
    
    # Controllo se le cifre collimano con la mantissa altrimenti aggiungo zeri
    mantissa = parteInteraBin + parteDecimaleBin

    if len(mantissa) < nCifreMantissa :
        mantissa += "0"*(nCifreMantissa - len(mantissa))


    ## Il numero ora è della forma 10101.01010101
    print("\n")
    print("## Number converted in binary")
    print(parteInteraBin + "." + parteDecimaleBin)


    ## ESPONENTE
    # Trovo l'esponente
    # Se la parte intera esiste conto le sue cifre per trovare l'esponente
    if parteInteraBin != 0 :
        exp = len(parteInteraBin) -1
    else :
    # Conto gli zeri da togliere
        i = 0
        nZeri = 1
        while partedecimale[i] != 1 :
            nZeri += 1
            i += 1
            
        exp = nZeri * (-1)

    # Calcolo l'eccesso
    exx = 2**(nCifreExp -1) -1

    # Trovo nuovo esponente
    exp = exx + exp

    # Converto in binario
    exp = str(bin(exp))[2:]

    # Vedo se le cifre collimano altrimenti aggiungo zeri
    if len(exp) < nCifreExp :
        exp += "0" * (nCifreExp - len(exp))
    

    if float(n) < 0 :
        segno = "1"
    else :
        segno = "0"

    print("\n## Number converted")
    print(segno + " | " + exp + " | " + mantissa[1:], "\n")

    nFinale = segno + exp + mantissa[1:]
    print(nFinale, str(len(nFinale)) + "bit", end = " ")


    if len(nFinale) != (nCifreExp + nCifreMantissa + 1) :
        print("OVERFLOW!")
    else :
        print("VALID NUMBER.")


def main():
    done = False
    
    while not done :
        
        inFile = open("config.txt", "r", encoding = "UTF-8")
        content = inFile.read()
        righe = content.split("\n")
        
        print(content)

        scelta = int(input("Choose: "))

        # Last line always "Manual"
        if scelta == len(righe) -1 :
            n               = input("Insert number to convert (Use DOT! ex. 456.43): ")
            #nCifreSegno    = int(input("Insert number of sign: "))
            nCifreExp       = int(input("Insert number of exponent: "))
            nCifreMantissa  = int(input("Insert number of mantissa: "))

            ieeeConvert(n, nCifreExp, nCifreMantissa)
            
        elif scelta == len(righe) -2 :
            n = input("Insert number to convert (Use DOT! ex. 456.43): ")
            
            for i in range(1, len(righe) -2) :
                riga = righe[i].split("|")
                ieeeConvert(n, int(riga[2]), int(riga[3]))
                riga.clear()
                print("\n", "-"*60)
        else :
            riga = righe[scelta].split("|")

            n = input("Insert number to convert (Use DOT! ex. 456.43): ")

            ieeeConvert(n, int(riga[2]), int(riga[3]))
        

     
        inFile.close()


        #/---------------------/
        done = input("\n\n||---> Done? ('y' for yes)").lower() == "y"

main()
