from scr.model.no import No


class ListaSimples:
    
    def __init__(self):
        
        self.init = None
        self.end = None
        self.size = 0
        self.limitSize = None
        
    
    def initInsert(self, value):
        no = No(value)
        
        if self.isEmpty():
            self.init = no
            self.end = no
            self.size+=1
        else:
            no.proximo = self.init
            self.init = no
            self.size+=1

    def remove(self, i):

        if i == 0:
            if not self.isEmpty():
                no_aux = self.init
                self.init = no_aux.proximo
                no_aux = None

                self.size-=1

            else:
                print('Error')
        elif i >= self.size:

            no_anterior = self.init

            while no_anterior.proximo != self.end:
                no_anterior = no_anterior.proximo

            self.end = no_anterior
            self.end.proximo = None
            self.size -=1
        else:

            no_anterior = self.init
            no_atual = self.init.proximo
            i_atual = 1

            while no_atual != None:
                if i_atual == i:
                    no_anterior.proximo = no_atual.proximo
                    no_atual.proximo = None

                no_anterior = no_atual
                no_atual = no_anterior.proximo
                i_atual+=1




    def isEmpty(self):
        return False if self.size!=0 else True


    def printList(self):
        no_aux = self.init
        i = 0

        while no_aux is not None:
            print("{} - {}".format(i, no_aux.value))

            no_aux = no_aux.proximo
            i+=1