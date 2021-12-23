#Testes das classes criadas
from classes.fabrica_fila import FabricaFila
from classes.estatistica_resumida import EstatisticaResumida
from classes.estatistica_detalhada import EstatisticaDetalhada


#Rodar Testes separadamente

""" print("--------Teste_01--------")
fila_teste = FabricaFila.pega_fila("NORMAL")
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()

print(fila_teste.chama_cliente(5))
print(fila_teste.chama_cliente(10)) """

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


print(fila_teste_2.estatistica(EstatisticaResumida("20/03/2025", 120)))
print(fila_teste_2.estatistica(EstatisticaDetalhada("20/03/2025", 120)))
    
