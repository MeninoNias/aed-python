from scr.model.ListaSimples import ListaSimples

lista = ListaSimples()

lista.initInsert(10)
lista.initInsert(20)
lista.initInsert(30)
lista.initInsert(40)


lista.printList()

print()

lista.remove(2)

lista.printList()

print()
lista.remove(0)
lista.printList()

print()
lista.remove(1)
lista.printList()

