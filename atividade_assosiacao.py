class Curso:
  def __init__(self, disciplina):
    self.disciplina = disciplina

  def mostrar_disciplina(self):
  return f"{self.disciplina}"

class Professor:
  def __init__(self, nome):
    self.nome = nome

  def mostrar_informacoes(self):
  return f"O curso tem como um dos professores {self.nome} que ministra aulas de {self.disciplina.mostrar_disciplina()}"

disciplina_dieimes = Curso("Programação")
dieimes = ("Dieimes", disciplina_dieimes)

print(dieimes.mostrar_informacoes())
