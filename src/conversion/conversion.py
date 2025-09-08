class Conversion:

    def celsius_a_fahrenheit(self, celsius):

        return (celsius * 9/5) + 32
    
    def fahrenheit_a_celsius(self, fahrenheit):

        return (fahrenheit - 32) * 5/9
    
    def metros_a_pies(self, metros):

        return metros * 3.28084
    
    def pies_a_metros(self, pies):

        return pies * 0.3048
    
    def decimal_a_binario(self, decimal):

        if decimal == 0:
            return "0"
        binario = ""
        while decimal > 0:
            restante = decimal % 2
            binario = str(restante) + binario
            decimal //= 2
        return binario
                                  
    def binario_a_decimal(self, binario):
 
        cont = 0
        for posicion, digito in enumerate(binario):
            potencia = (len(binario) - 1) - posicion
            valor = int(digito) * (2 ** potencia)
            cont += valor
        return cont
    
    def decimal_a_romano(self, numero):

        valores  = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        simbolos = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        resultado = ""
        for i, valor in enumerate(valores):
            while numero >= valor:
                resultado += simbolos[i]
                numero -= valor
        return resultado
            
    
    def romano_a_decimal(self, romano):

        simbolos = ["M", "D", "C", "L", "X", "V", "I"]
        valores  = [1000, 500, 100, 50, 10, 5, 1]
        acumulador = 0
        i = 0
        while i < len(romano):
            valor_actual = valores[simbolos.index(romano[i])]
            if i + 1 < len(romano):
                valor_siguiente = valores[simbolos.index(romano[i+1])]
                if valor_actual < valor_siguiente:
                    acumulador += valor_siguiente - valor_actual
                    i += 2
                    continue
            acumulador += valor_actual
            i += 1
        return acumulador
    
    def texto_a_morse(self, texto):

        letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + list("0123456789")
        morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
            "--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--..",
            "-----",".----","..---","...--","....-",".....","-....","--...","---..","----."
        ]
        texto = texto.upper()
        codigo = []
        for caracter in texto:
            if caracter == " ":
                codigo.append("/")
            elif caracter in letras:
                indice = letras.index(caracter)
                codigo.append(morse[indice])
        return " ".join(codigo)
    
    def morse_a_texto(self, morse):

        letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + list("0123456789")
        codigo_morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
            "--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--..",
            "-----",".----","..---","...--","....-",".....","-....","--...","---..","----."
        ]
        palabras = [p.strip() for p in morse.split('/') if p.strip() != ""]
        resultado = []
        for palabra in palabras:
            letras_morse = palabra.split()
            texto = ""
            for simbolo in letras_morse:
                if simbolo in codigo_morse:
                    indice = codigo_morse.index(simbolo)
                    texto += letras[indice]
                else:
                    texto += "?"
            resultado.append(texto)
        return " ".join(resultado)