class programacao:
     def__init__(self, id, nome,tipo,genero,categoria):
         self.__id = id
         self.__nome = nome
         self.__tipo = tipo
         self.__genero = genero
         self.__categoria = categoria
     
     @property
     def nome(self):
         return self.__nome

     @property
     def tipo(self):
         return self.__tipo

     @property
     def genero(self):
         return self.__genero

     @property
     def categoria (self):
         return self.__categoria        
        