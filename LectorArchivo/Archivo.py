

class Archivo:
    
    diccionario = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [], 
               'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': [],
               '0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], 'especiales': []}
    lineas = 0
    
    consonantes = 0
    
    vocales = 0
    
    especiales= 0
    
    numeros= 0
    
    archivo = ""
    
    palabras = 0
    
    letras = 0
    
    textoNuevo = ""
    
    
    def __init__(self, texto):
        self.texto = texto.lower()
    
    def analizarTexto(self):
        
        self.diccionario = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [], 
               'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': [],
               '0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], 'especiales': []}
        
        self.lineas = 0
    
        self.consonantes = 0
        
        self.vocales = 0
        
        self.especiales= 0
        
        self.numeros= 0
        
        self.palabras = 0
        
        self.letras = 0
        
        self.textoNuevo = ""
        
        try:
            for letra in range(0,len(self.texto)):
                
                if self.texto[letra] in "bcdfghjklmnpqrstvwxyz":
                    self.consonantes +=1
                    self.diccionario[str(self.texto[letra])].append(letra)
                elif self.texto[letra] in "aeiou":
                    self.vocales +=1
                    self.diccionario[str(self.texto[letra])].append(letra)
                elif self.texto[letra] in "0123456789":
                    self.numeros +=1
                    self.diccionario[str(self.texto[letra])].append(letra)
                else:
                    self.especiales +=1
                    self.diccionario["especiales"].append(letra)
            self.contarPalabras()
            self.contarLetras()
            self.contarLineas()
                    
        except Exception as e:
            print(e)
            
    def contarPalabras(self):
        for letra in self.texto:
            if (letra ==" " or "\n" or "\t"):
                self.palabras+=1
    
    def contarLetras(self):
        for letra in self.texto:
            if letra != "\n" or " " or "\t":
                self.letras+=1
    
    def contarLineas(self):
        for letra in self.texto:
            if letra == "\n":
                self.lineas+=1
        self.lineas+=1
        
    def verEstadisticas(self):
        try:
            self.textoNuevo = "Estadisticas:\n\n"
            for clave, valor in self.diccionario.items():
                if valor :
                    self.textoNuevo += f'{clave} = {valor}\n'
                    
            self.textoNuevo+= f'Numero de letras = {self.letras}\n'
            self.textoNuevo+= f'Numero de palabras = {self.palabras}\n'
            self.textoNuevo+= f'Numero de vocales = {self.vocales}\n'
            self.textoNuevo+= f'Numero de consonantes = {self.consonantes}\n'
            self.textoNuevo+= f'Numero de caracteres especiales = {self.especiales}\n'
            self.textoNuevo+= f'Numero de lineas = {self.lineas}\n'
            self.textoNuevo+= f'Numero de numeros = {self.numeros}'
            
        except Exception as e:
            print(e) 
    
    def modificarTexto(self, letra1, letra2):
        lista = self.diccionario.get(letra2)
        lista2 = list(self.texto) 
        
        for indice in lista:
            lista2[indice] = letra1
            
        self.texto = ""
        
        for letra in lista2:
            self.texto +=letra
        
