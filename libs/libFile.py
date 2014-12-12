##
# Funzioni utili files
# @en Useful files functions
# - 
#   
# Gabriele Proietti Mattia - gabry.gabry@hotmail.it
# Università La Sapienza di Roma
# Facoltà di Ingegneria Informatica
# 2014/15
##

## Empty a file
# @param Name of file (ex. Example.txt)
#
def emptyFile(name) :
    outFile = open(name, "w", encoding = "UTF-8")
    outFile.write("")
    outFile.close()
