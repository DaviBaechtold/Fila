"""Construir um código capaz, de somar, item a item, todos os inteiros entre 1 e 1.000.000.
#Para realizar está tarefa você deverá criar duas estrutura de dados, uma pilha e uma fila.
#Depois preencher esta estrutura com todos os valores necessarios, percorrendo a estrutura.
#Somar todos os valores das estrturas de dados.
#Medir os tempos para percorrer e somar 1.000.000 de inteiros em uma determinada estrutura de dados."""

import time

class Stack:
    def __init__(self):
        self.__stack = [] 
        self.cont = 0
        self.capacity = 10
  
    def push(self, str):
        self.cont += 1
        self.__stack.insert(0,str)
        
    def pop(self):
        self.__stack.pop()

    def empty(self):
        if self.__stack is None:
            print("Pilha Vazia")
        elif len(self.__stack) == 10:
              print("Pilha Cheia")
        else:
            print("Pilha não esta vazia ou cheia")

    def lenght(self):
        return len(self.__stack)

    def capacit(self):
        print(self.capacity - len(self.__stack))

    def TimeSum(self):
        start = time.time()
        sum(self.__stack)
        end = time.time()
        print("Sum: ",sum(self.__stack))
        print("Runtime: ", end - start, "second")
        
class Fist_InOut:
    def __init__(self):
        self.__io = [] #io -> In Out
        self.cont = 0
        self.capacity = 10
    
    def push(self, str):
        self.cont += 1
        self.__io.append(str)
    
    def pop(self):
        self.__io.pop()

    def empty(self):
        if self.__io is None:
            print("Lista Vazia")
        elif len(self.__io) == 10:
           print("Lista Cheia")
        else:
            print ("Linha nao esta cheia ou vazia")
            
    def lenght(self):
        return len(self.__io)

    def capacit(self):
        print("the capacity is: ", self.capacity -len(self.__io))

    def TimeSum(self):
        start = time.time()
        sum(self.__io)
        end = time.time()
        print("Sum: ", sum(self.__io))
        print("Run time:" ,end - start, "second")

def main():

    list = Fist_InOut()
    pilha = Stack()
    i= 0
    for i in range(10):
        list.push(i)
        pilha.push(i)

    print("*****Stack****")
    pilha.pop()
    pilha.TimeSum()
    print("++++Row++++")
    list.pop()
    list.TimeSum()

if __name__ == "__main__":
    main()