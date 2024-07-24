# Importando as bibliotecas
from tkinter import *
from tkinter import ttk, messagebox
from tkscrolledframe import ScrolledFrame
from PIL import Image, ImageTk

# Definindo cores e criando a janela
cor_de_fundo_1 = "#FFFFFF"
cor_de_fundo_2 = "#E1F2FD"
cor_letra = "#403d3d"

janela = Tk()
janela.title("Bot de Suporte")
janela.geometry('500x500')
janela.configure(background=cor_de_fundo_1)
janela.resizable(width=False, height=False)

# Criando frames
frameCima = Frame(janela, width=500, height=100, bg=cor_de_fundo_1, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)  

frameMeio = Frame(janela, width=500, height=300, bg=cor_de_fundo_1, relief="solid")
frameMeio.grid(row=1, column=0, sticky="NSEW")

frameBaixo = Frame(janela, width=500, height=100, bg=cor_de_fundo_1, relief="flat")
frameBaixo.grid(row=2, column=0, sticky="NSEW")

# Adicionar imagens ao frame de cima
img_app = Image.open('C:/Users/Renan Tito/Documents/ESTUDOS/python/img/img-robo.png')
img_app = img_app.resize((70, 70))
img_app = ImageTk.PhotoImage(img_app)
app_ = Label(frameCima, height=70, image=img_app, compound=LEFT, anchor='center', bg=cor_de_fundo_1)
app_.place(x=10, y=10)

app_logo = Label(frameCima, text="ChatBot de Suporte", compound=LEFT, padx=5, anchor=NW, font=('System 20 bold'), bg=cor_de_fundo_1, fg=cor_letra)
app_logo.place(x=100, y=20)

# Configurar frame meio com scrolledframe
sf = ScrolledFrame(frameMeio, width=480, height=380)  # Corrigido aqui
sf.grid(row=1, column=0, sticky=NW)
sf.bind_arrow_keys(frameMeio)
sf.bind_scroll_wheel(frameMeio)
framecanva = sf.display_widget(Frame, bg=cor_de_fundo_1)
# Usamos o SCROLLEDFRAME para criar uma área de rolagem para as mensagens no frameMeio.

# Adicionar componentes ao frame meio
frame_chat = Frame(framecanva, width=480, height=480, bg=cor_de_fundo_2, relief="flat")  # Corrigido aqui
frame_chat.grid(row=0, column=0, sticky=NSEW, padx=7, pady=10)

text_chat = Text(frame_chat, wrap=WORD, state=DISABLED, font=('Arial 10'), bg=cor_de_fundo_2, fg=cor_letra)
text_chat.pack(expand=True, fill=BOTH)
# Criamos um frame para o chat dentro da área de rolagem e um widget de texto para exibir as mensagens.

# Adicionar entrada de mensagem e botão de envio
entry_mensagem = Entry(frameBaixo, font=('Arial 12'), width=48, relief="solid")
entry_mensagem.grid(row=0, column=0, padx=10, pady=5)

button_imagem = Image.open('C:\Users\Renan Tito\Documents\ESTUDOS\python\img')
button_imagem = button_imagem.resize((30, 30))
button_imagem = ImageTk.PhotoImage(button_imagem)
button_enviar = Button(frameBaixo, image=button_imagem, command=lambda: enviar_mensagem(entry_mensagem, text_chat), bg=cor_de_fundo_1, relief=FLAT)
button_enviar.grid(row=0, column=1, padx=5, pady=5)

# Definir funções
def enviar_mensagem(entry, text_widget):
    mensagem_usuario = entry.get()
    if mensagem_usuario:
        adicionar_mensagem(mensagem_usuario, "Usuário", text_widget)
        entry.delete(0, END)

def adicionar_mensagem(mensagem, remetente, text_widget):
    text_widget.config(state=NORMAL)
    text_widget.insert(END, f"{remetente}: {mensagem}\n\n")
    text_widget.config(state=DISABLED)
    text_widget.yview(END)

# Adicionar mensagens de exemplo
adicionar_mensagem("Olá! Como posso ajudar?", "Bot", text_chat)
adicionar_mensagem("Estou com um problema no meu código.", "Usuário", text_chat)
adicionar_mensagem("Claro, vou tentar ajudar. Qual o problema?", "Bot", text_chat)
# Adicionamos algumas mensagens de exemplo ao iniciar o aplicativo

janela.mainloop()


