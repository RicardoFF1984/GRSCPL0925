from modelos import AgendaContacto, Contacto

ct = Contacto("nome", "+351 913129123", "nome@mail.com")

agenda = AgendaContacto()

agenda.adicionar_contacto(contacto=ct)

print(agenda.lista_contactos[0])
print(agenda.lista_contactos)
