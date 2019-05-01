# gencon
Generador de contraseñas basado en el sistema diceware.


USO:
gencon.py [-n NUM] [-s SEPARADOR] [-d DICCIONARIO] [-f SALIDA] [-l LETRA]

-n NUM          Número de palabras a usar. Cuantas más palabras, más larga y segura la contraseña.
                Valor por defecto: 4

-s SEPARADOR    Separador que irá entre las palabras. Se recomienda '.' o '-'
                Valor por defecto: ' '

-d DICCIONARIO  Lista de palabras a usar. Una por linea.
                Valor por defecto: 'SP_wordlist.lst'

-f SALIDA       La contraseña generada se escribe al final de este archivo. Si se omite, se imprime en pantalla.

-l LETRA        Todas las palabras empezarán por ese caracter.
