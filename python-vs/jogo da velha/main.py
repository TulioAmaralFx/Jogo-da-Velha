import tkinter as tk
from jogo_da_velha_core import JogoDaVelha
from gui_manager import GerenciadorGUI

def main():
    root = tk.Tk()
    jogo = JogoDaVelha()
    app = GerenciadorGUI(root, jogo)
    root.mainloop()

if __name__ == "__main__":
    main()