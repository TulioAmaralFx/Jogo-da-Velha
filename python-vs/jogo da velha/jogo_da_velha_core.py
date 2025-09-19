
class JogoDaVelha:
    
    def __init__(self):
        self._observers = []
        self.resetar_jogo()

    def resetar_jogo(self):
        self.tabuleiro = [" " for _ in range(9)]
        self.jogador_atual = "X"
        self.turno = 0
        self._notificar_observadores()

    def fazer_jogada(self, posicao):
        if self.tabuleiro[posicao] == " ":
            self.tabuleiro[posicao] = self.jogador_atual
            self.turno += 1
            
            self._notificar_observadores()
            
            if self.verificar_vitoria(self.jogador_atual):
                return "vitoria"
            elif self.verificar_empate():
                return "empate"
            else:
                self._alternar_jogador()
                return "continuar"
        return "invalida"

    def _alternar_jogador(self):
        self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def verificar_vitoria(self, jogador):
        condicoes_vitoria = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for condicao in condicoes_vitoria:
            if all(self.tabuleiro[i] == jogador for i in condicao):
                return True
        return False

    def verificar_empate(self):
        return " " not in self.tabuleiro

    # Métodos do Padrão Observer
    def adicionar_observador(self, observer):
        self._observers.append(observer)

    def _notificar_observadores(self):
        for observer in self._observers:
            observer.atualizar(self.tabuleiro, self.jogador_atual)


class ComandoJogada:
    
    def __init__(self, jogo, posicao):
        self._jogo = jogo
        self._posicao = posicao

    def executar(self):
        return self._jogo.fazer_jogada(self._posicao)

class ComandoResetar:

    def __init__(self, jogo):
        self._jogo = jogo

    def executar(self):
        self._jogo.resetar_jogo()