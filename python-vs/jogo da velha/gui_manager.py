import tkinter as tk
from tkinter import messagebox
from jogo_da_velha_core import JogoDaVelha, ComandoJogada, ComandoResetar

class GerenciadorGUI:
    
    def __init__(self, master, jogo):
        self.master = master
        self.jogo = jogo
        self.jogo.adicionar_observador(self)
        
        self.master.title("Jogo da Velha")
        
        self.botoes_tabuleiro = []
        self._criar_widgets()
        self.atualizar(self.jogo.tabuleiro, self.jogo.jogador_atual)

    def _criar_widgets(self):
        for i in range(9):
            botao = tk.Button(self.master, text=" ", font=("Arial", 24), width=5, height=2,
                              command=self._obter_comando(i))
            self.botoes_tabuleiro.append(botao)
            botao.grid(row=i // 3, column=i % 3)

        botao_reset = tk.Button(self.master, text="Reiniciar", font=("Arial", 16), command=self._obter_comando("reset"))
        botao_reset.grid(row=3, column=0, columnspan=3, pady=10)

    def _obter_comando(self, acao):

        if acao == "reset":
            return ComandoResetar(self.jogo).executar
        else:
            comando = ComandoJogada(self.jogo, acao)
            return lambda: self._executar_jogada(comando)

    def _executar_jogada(self, comando):
        resultado = comando.executar()
        
        if resultado == "vitoria":
            messagebox.showinfo("Fim de Jogo", f"Parabéns! O jogador {self.jogo.jogador_atual} venceu!")
            self.jogo.resetar_jogo()
        elif resultado == "empate":
            messagebox.showinfo("Fim de Jogo", "O jogo terminou em empate!")
            self.jogo.resetar_jogo()
        elif resultado == "invalida":
            messagebox.showwarning("Jogada Inválida", "Essa posição já está ocupada. Tente outra.")

    def atualizar(self, tabuleiro, jogador_atual):

        for i, text in enumerate(tabuleiro):
            self.botoes_tabuleiro[i].config(text=text)