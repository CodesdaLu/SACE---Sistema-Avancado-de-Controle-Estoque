import tkinter as tk
from tkinter import messagebox
from main import *
from pymongo import MongoClient

con = MongoClient('mongodb+srv://lcarms93:ZE7OlLBfBFX4gL6q@login.w2urk.mongodb.net/') 
db=con.get_database("Login")
collection =db.get_collection('contatos')


azul2 = '#006ed0'

def verificar_login():
    username = entry_username.get()
    password = entry_senha.get()
   
    if not username or not password:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return
    
    try:
        usuario = collection.find_one({'nome': username, 'senha': password})
        if usuario:
            messagebox.showinfo("Sucesso", f"Bem-vindo, {username}!")
            root_lo.withdraw()  # Esconde a janela de login
            iniciar_prog()
           
            
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {e}")
            
        

def abrir_janela_cadastro():
    # Fechar a janela principal de login
    root_lo.withdraw()
    
    # Criar uma nova janela para cadastro
    cadastro_window = tk.Toplevel()
    cadastro_window.title("Cadastro")
    cadastro_window.geometry("400x350")
    cadastro_window.resizable(False, False)
    cadastro_window.iconbitmap('D:\\CODEs\\CRUD\\package.ico')
    

    # Função para finalizar o cadastro
    def finalizar_cadastro():
        nome = entry_nome.get()
        senha = entry_senha_cadastro.get()

        if not nome or not senha:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return
        
        if len(nome) > 5:
            messagebox.showerror("Erro", "O nome deve ter no máximo 5 caracteres!")
            return

        if len(senha) > 5 or not senha.isdigit():
            messagebox.showerror("Erro", "A senha deve ter no máximo 5 dígitos numéricos!")
            return
        
        try:
            collection.insert_one({'nome': nome, 'senha': senha})
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            cadastro_window.destroy()
            root_lo.deiconify()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar no banco de dados: {e}")

    # Função para fechar a janela de cadastro
    def fechar_janela_cadastro():
        cadastro_window.destroy()
        root_lo.deiconify()

    # Configuração para fechar a janela
    cadastro_window.protocol("WM_DELETE_WINDOW", fechar_janela_cadastro)

    # Widgets da janela de cadastro
    tk.Label(cadastro_window, text="Cadastro", font=('Arial', 20, 'bold')).pack(pady=10)

    tk.Label(cadastro_window, text="Nome:", font=('Arial', 14)).pack(pady=5)
    entry_nome = tk.Entry(cadastro_window, font=('Arial', 12))
    entry_nome.pack(pady=5)

    tk.Label(cadastro_window, text="Senha:", font=('Arial', 14)).pack(pady=5)
    entry_senha_cadastro = tk.Entry(cadastro_window, show="*", font=('Arial', 12))
    entry_senha_cadastro.pack(pady=5)
    
    # Aviso sobre as restrições
    tk.Label(cadastro_window, text="* Nome e senha devem ter no máximo 5 caracteres.\n* A senha deve ser numérica.", 
             font=('Arial', 8), fg='grey').pack(pady=5)

    tk.Button(cadastro_window, text="Cadastrar", font=('Arial', 12), bg=azul2, fg='white', command=finalizar_cadastro).pack(pady=15)

# Criar a janela principal de login
root_lo = tk.Tk()
root_lo.title("Login")
root_lo.geometry("400x300")
root_lo.resizable(False, False)
root_lo.iconbitmap('D:\\CODEs\\CRUD\\package.ico')

# Configurações visuais
bg_color = "#f0f0f0"
button_color = azul2

root_lo.configure(bg=bg_color)

# Centralizar a janela principal
window_width = root_lo.winfo_reqwidth()
window_height = root_lo.winfo_reqheight()
position_right = int(root_lo.winfo_screenwidth()/2 - window_width/2)
position_down = int(root_lo.winfo_screenheight()/2 - window_height/2)
root_lo.geometry("+{}+{}".format(position_right, position_down))

# Widgets para login
tk.Label(root_lo, text="Login", font=('Arial', 24, 'bold'), bg=bg_color).pack(pady=10)

tk.Label(root_lo, text="Username:", font=('Arial', 12), bg=bg_color).pack(pady=5)
entry_username = tk.Entry(root_lo, font=('Arial', 12))
entry_username.pack(pady=5)

tk.Label(root_lo, text="Senha:", font=('Arial', 12), bg=bg_color).pack(pady=5)
entry_senha = tk.Entry(root_lo, show="*", font=('Arial', 12))
entry_senha.pack(pady=5)

tk.Button(root_lo, text="Login", font=('Arial', 12), bg=button_color, fg='white', command=verificar_login).pack(pady=10)
tk.Button(root_lo, text="Criar Conta", font=('Arial', 12), bg=button_color, fg='white', command=abrir_janela_cadastro).pack(pady=5)

# Executar a aplicação
root_lo.mainloop()