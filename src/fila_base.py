from abc import ABCMeta, abstractmethod


class FilaBase(metaclass=ABCMeta):
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""
    
    def reseta_fila(self) -> None:
        if self.codigo >= 200:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self):
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()
        
    def insere_cliente(self):
        self.fila.append(self.senha_atual)

    @abstractmethod
    def gera_senha_atual(self):
        pass

    @abstractmethod
    def chama_cliente(self, caixa):
        pass