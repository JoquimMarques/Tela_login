# from tkinter import *

# tela = Tk()
# tela.title("Login")
# tela.geometry("500x500")

# def clik():
#     print("Loginnnnnnnn")


# texto = Label(tela, text="Fazer Login")
# texto.pack(padx=10, pady=10)

# botao= Button(tela, text="Login", command=clik)
# botao.pack(padx= 10, pady=10)


# tela.mainloop()
 
import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

tela = customtkinter.CTk()
tela.title("Tela de Login")
tela.geometry("500x300")

def clik():
    if email.get() == "teste@email.com":

        texto.pack_forget()
        email.pack_forget()
        senha.pack_forget()
        botao.pack_forget()
        

        label_parabens = customtkinter.CTkLabel(tela, text="PARABENS VOCÊ ENTROU", font=("Arial", 100))
        label_parabens.pack(pady= 80)

    else:
         mensagem_erro = customtkinter.CTkLabel(tela, text="Email inválido. Tente novamente.", font=("Arial", 16))
         mensagem_erro.pack(pady=10)





 
texto = customtkinter.CTkLabel(tela, text="Fazer Login", font=("Arial", 30, "bold"))
texto.pack(padx=20, pady= 20)

email = customtkinter.CTkEntry(tela, placeholder_text="Digite seu email",font=("Arial", 13), width=300, height=40)
email.pack(padx=10, pady= 10)

senha = customtkinter.CTkEntry(tela, placeholder_text="senha", show="$", font=("Arial", 13), width=300,height=40)
senha.pack(padx=10, pady= 10)

botao = customtkinter.CTkButton(tela, text="Login", command=clik, font=("Arial", 13), width=200, height=40)
botao.pack(padx=10, pady=10)


tela.mainloop()