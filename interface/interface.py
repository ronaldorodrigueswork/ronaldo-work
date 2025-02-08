import tkinter as tk

janela = tk.Tk()
janela.title("Minha Interface Gráfica")
janela.geometry("300x200")

label = tk.Label(janela, text="Olá, Tkinter!")
label.pack()

botao = tk.Button(janela, text="Clique Aqui")
botao.pack()

janela.mainloop()