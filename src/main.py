#Testes das classes criadas
from fabrica_fila import FabricaFila


print("--------Teste_01--------")
fila_teste = FabricaFila.pega_fila("NORMAL")
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()

print(fila_teste.chama_cliente(5))
print(fila_teste.chama_cliente(10))

print("\n--------Teste_02--------")
fila_teste_2 = FabricaFila.pega_fila("PRIORITARIA")
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()

print(fila_teste_2.chama_cliente(4))
print(fila_teste_2.chama_cliente(1))
print(fila_teste_2.chama_cliente(5))
print(fila_teste_2.chama_cliente(7))

print(fila_teste_2.estatistica("10/01/1993", 198, "detail"))
