from modelo import Pessoa, Aluno

p1 = Pessoa("Carlos", 23)

print(p1.nome)

print(p1.idade)

p1.idade = 18
print(p1.idade)

p1.idade = 12
print(p1.idade)

aluno = Aluno("Rita", 23)

print(aluno.nome)

print(aluno.turma)
