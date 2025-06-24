#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.
dias = 3
dia01 = int(input("dias para a atividade 01"))
dia02 = int(input("dias para a atividade 02"))
dia03 = int(input("dias para a  atividade 03"))

soma = dia01 + dia02 + dia03
if dia01 < 0 or dia02 < 0 or dia03 < 0:
    print("erro número negatvo")
else:
    soma = dia01 + dia02 + dia03
    print(F"Tempo total do projeto:{soma} dias")