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

        
## costruisciConfigurazione
# @param file File di configurazione
# @return d Dizionario <voce>:[bit, segno, exp, mantissa]
#
def costruisciConfigurazione(file) :
    d = {}
    inFile = open(file, "r", encoding = "UTF-8")
    n = 0
    
    for riga in inFile :
        if riga[0] != "#" :
            d[n] = riga.strip().split(";")
            
            n += 1        
    
    inFile.close()
    return d

def main():
    done = False

    # Costruisco il dizionario di configurazione
    d = costruisciConfigurazione("config.txt")
    
    while not done :

        # Stampo a video la configurazione per consentire la scelta
        print("="*15 + " BITMAKER " + "="*15)
        print("="*2 + " Convert decimal to floating point " + "="*2)
        print("="*13 + " by gabry3795 " + "="*13)
        print("="*4 + " University La Sapienza of Rome " + "="*4)
        print("="*6 + " Computer Engineering 14/15 " + "="*6)
        for voce in d :
            if int(voce) == 0 :
                print("[N.] %7s %7s %7s %7s" %(d[voce][0], d[voce][1], d[voce][2], d[voce][3]))
            elif int(voce) == (len(d) -1) or int(voce) == (len(d) -2) :
                print("[%s.] %7s" %(voce, d[voce][0]))
            else :
                print("[%s.] %7s %7s %7s %7s" %(voce, d[voce][0], d[voce][1], d[voce][2], d[voce][3]))
        
        print("=> Choose the floating point type you want to convert to.")
        #print("=> (Use default setting or choose manual to specify mantissa and exponent)")
        scelta  = int(input("=> [1 - %d]: " % (len(d)-1) ))
        n       = input("=> Insert number to convert (Use DOT! ex. 456.43): ")
        
        # Ultima riga sempre manuale
        if scelta == len(d) -1 :
            
            #sign    = int(input("Insert number of sign: "))
            sign    = 1 # Non esistono numeri con sign > 1
            exp     = int(input("==> Insert number of exponent: "))
            mantissa = int(input("==> Insert number of mantissa: "))
            bit = str(sign + exp + mantissa) + "bit"

            print("\n" + "="*10 + " %s : Sign (%s) | Exponent (%s) | Mantissa (%s) " % (bit, sign, exp, mantissa) + "="*10)
            ieeeConvert(n, exp, mantissa)

        # Penultima riga sempre "Tutti"
        elif scelta == len(d) -2 :
            
            for i in range(1, len(d) -2) :
                bit         = d[i][0]
                sign        = d[i][1]
                exp         = int(d[i][2])
                mantissa    = int(d[i][3])
                print("\n" + "="*10 + " %s : Sign (%s) | Exponent (%s) | Mantissa (%s) " % (bit, sign, exp, mantissa) + "="*10)
                ieeeConvert(n, exp, mantissa)

                #print("\n", "-"*60)
                
        # Altrimenti 
        else :
            bit         = d[scelta][0]
            sign        = d[scelta][1]
            exp         = int(d[scelta][2])
            mantissa    = int(d[scelta][3])

            print("\n" + "="*10 + " %s : Sign (%s) | Exponent (%s) | Mantissa (%s) " % (bit, sign, exp, mantissa) + "="*10)
            ieeeConvert(n, exp, mantissa)
        

          


        #/---------------------/
        done = input("\n\n==> Done? ('y' for yes): ").lower() == "y"
        print("\n\n")

main()
