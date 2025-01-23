from tkinter import *
import tkinter as tk
from tkinter import ttk, Tk, Label, Frame
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from datetime import date
from PIL import Image, ImageTk
from tkinter import Button, Label
from view import *

########### Janela SACE ############
def iniciar_prog():
    
    # cores
    azul = "#120a8f"
    azul2 = '#006ed0'
    verde = "#007d00"
    verde2= '#0a5a0a'
    branco = "#f5f5f5"
    cinza = "#dcdcdc"
    preto = '#000000'
    vermelho = "#940014"    
    
    root = Tk()
    root.title("SACE - Sistema Avançado de Controle Estoque")
    root.resizable(width=FALSE, height=FALSE)
    root.iconbitmap('D:\\CODEs\\CRUD\\package.ico')
    
    
    tarja = Frame(root, width=400, height=80, bg=azul, relief='flat')
    tarja.grid(row=0, column=0)

    escopo = Frame(root, width=310, height=500, bg=branco, relief='flat')
    escopo.grid(row=1, column=0, padx=1, pady=0, sticky=NSEW)

    direita = Frame(root, width=1000, height=80, bg=cinza, relief='flat')
    direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

    
    ############## Labels ##############


    nome = Label(tarja, text='SACE', bg=azul, fg=branco, font=('Ivy 16 bold'), anchor=NW, relief='flat')
    nome.place(x=60, y=15)

    nomep = Label(tarja, text='Sistema Avançado de Controle Estoque', bg=azul, fg=branco, font=('Ivy 8 '), anchor=NW, relief='flat')
    nomep.place(x=60, y=40)

   

    #Variável global
    global tree

    #função inserir
    def inserir():
        produto = entry_prod.get()
        codigo = entry_cod.get()
        quantidade = entry_quant.get()
        loja =  loja_combobox.get()
        data = entry_atualizacao.get()
        
        lista = [codigo, produto, quantidade, loja, data]
        
        if produto == '':
            messagebox.showerror('Error', 'O produto não pode ser vazio!')
        else:
            inserir_info(lista)
            messagebox.showinfo('Sucesso!', 'Os dados foram inseridos com sucesso!')
            
        entry_prod.delete(0,'end' )
        entry_loja.delete(0,'end' )
        entry_cod.delete(0,'end' )
        entry_quant.delete(0,'end' )
        entry_atualizacao.delete(0,'end' )

        for widget in direita.winfo_children():
            widget.destroy()
            
        mostrar_tabela()
        
        
    def atualizar():
        
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista = treev_dicionario['values']
            
            id_valor = tree_lista[0]
            
            entry_prod.delete(0,'end')
            entry_loja.delete(0,'end')
            entry_cod.delete(0,'end')
            entry_quant.delete(0,'end')
            entry_atualizacao.delete(0,'end')
            
            
            entry_prod.insert(0,tree_lista[2])
            entry_loja.insert(0,tree_lista[4])
            entry_cod.insert(0,tree_lista[1])
            entry_quant.insert(0,tree_lista[3])
            entry_atualizacao.insert(0,tree_lista[5])
            
            
            
            def update():
                produto = entry_prod.get()
                codigo = entry_cod.get()
                quantidade = entry_quant.get()
                loja =  loja_combobox.get()
                data = entry_atualizacao.get()
                
                lista = [codigo, produto, quantidade, loja, data, id_valor]

                                
                if produto == '':
                    messagebox.showerror('Error', 'O produto não pode ser vazio!')
                else:
                    atualizar_info(lista)
                    messagebox.showinfo('Sucesso!', 'Os dados foram atualizados com sucesso!')
                    
                entry_prod.delete(0,'end' )
                entry_loja.delete(0,'end' )
                entry_cod.delete(0,'end' )
                entry_quant.delete(0,'end' )
                entry_atualizacao.delete(0,'end' )

                # Destruir o botão de confirmação após a atualização
                
                bt_confirmar.destroy()

                for widget in direita.winfo_children():
                    widget.destroy()
                    
                    
                mostrar_tabela()


            bt_confirmar = Button(escopo,command=update , text='CONFIRMAR ATUALIZAÇÃO', width=30, bg=verde2, fg=branco, font=('Ivy 10 bold'), relief='raised', overrelief='ridge')
            bt_confirmar.place(x=10, y=370)

        except IndexError:
            messagebox.showerror('Error', 'Ops! Selecione um dos dados da tabela!')

        

        
            


    def deletar():
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista = treev_dicionario['values']
            
            id_valor = [tree_lista[0]]
            
            deletar_info(id_valor)
            
            messagebox.showinfo('Sucesso!', 'Os dados foram deletados com sucesso!')
            
            mostrar_tabela()
            
        except IndexError:
            messagebox.showerror('Error', 'Ops! Selecione um dos dados da tabela!')
            
        
    nome_prod = Label(escopo, text='Nome do produto', fg=preto, font=('Ivy 10 bold'), anchor=NW, relief='flat')
    nome_prod.place(x=10, y=25)

    entry_prod = Entry(escopo, width=30, justify='left', fg=preto, relief='solid')
    entry_prod.place(x=10, y=47)

    cod_prod = Label(escopo, text='Código do produto', fg=preto, font=('Ivy 10 bold'), anchor=NW, relief='flat')
    cod_prod.place(x=10, y=95)

    entry_cod = Entry(escopo, width=10, justify='left', fg=preto, relief='solid')
    entry_cod.place(x=10, y=117)



    quant = Label(escopo, text='Quantidade', fg=preto,
                font=('Ivy 10 bold'), anchor=NW, relief='flat')
    quant.place(x=10, y=165)

    entry_quant = Entry(escopo, width=20, justify='left', fg=preto, relief='solid')
    entry_quant.place(x=10, y=187)


    nome_loja = Label(escopo, text='Loja', fg=preto, font=(
        'Ivy 10 bold'), anchor=NW, relief='flat')
    nome_loja.place(x=10, y=235)

    entry_loja = Entry(escopo, width=45, justify='left', fg=preto, relief='solid')
    entry_loja.place(x=10, y=257)

    def exibir_opcao(*args):
        opcao_selecionada = loja_combobox.get()
        print(f"Opção selecionada: {opcao_selecionada}")

    loja_combobox = ttk.Combobox(entry_loja, values=["", "Mr.", "Ms.", "Dr."])
    loja_combobox.set('Escolha uma opção')
    loja_combobox.bind("<<ComboboxSelected>>", exibir_opcao)
    loja_combobox.grid(row=1, column=2)









    ## Atualização ##

    atualizacao = Label(escopo, text='Atualização', fg=preto,
                        font=('Ivy 10 bold'), anchor=NW, relief='flat')
    atualizacao.place(x=10, y=305)

    entry_atualizacao = DateEntry(
        escopo, width=15, background='#120a8f', foreground='white', borderwidth=1)
    entry_atualizacao.place(x=10, y=327)

    entry_atualizacao = DateEntry(
        escopo, 
        width=15, 
        background='#120a8f', 
        foreground='white', 
        borderwidth=1, 
        date_pattern='dd/mm/yyyy'  # Definindo o formato de data desejado
    )
    entry_atualizacao.place(x=10, y=327)


    ############## Botao ##############

    bt_add = Button(escopo, text='ADICIONAR', command=inserir,  width=10, bg=azul2, fg=branco, font=(
        'Ivy 10 bold'), relief='raised', overrelief='ridge')
    bt_add.place(x=10, y=430)


    bt_atualizar = Button(escopo, command=atualizar, text='ATUALIZAR', width=10, bg=verde, fg=branco, font=(
        'Ivy 10 bold'), relief='raised', overrelief='ridge')
    bt_atualizar.place(x=130, y=430)

    bt_excluir = Button(escopo,command=deletar, text='EXCLUIR', width=10, bg=vermelho, fg=branco, font=(
        'Ivy 10 bold'), relief='raised', overrelief='ridge')
    bt_excluir.place(x=250, y=430)



    ## TABLE ##

    def mostrar_tabela():
        
        global tree
        
        lista = mostrar_info()

        df_list = lista

        table_head = ['ID', 'Cód Produto', 'Nome do Produto', 'Quantidade', 'Loja', 'Data de atualização']

        # criando a tabela
        tree = ttk.Treeview(direita, selectmode="extended",
                            columns=table_head, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(direita, orient="vertical", command=tree.yview)

        # horizontal scrollbar
        hsb = ttk.Scrollbar(direita, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        direita.grid_rowconfigure(0, weight=15)

        hd = ["center", "center", "center", "center", "center", "center"]
        h = [50, 100, 150, 70, 150, 150]
        n = 0

        for col in table_head:
            tree.heading(col, text=col.title(), anchor=CENTER)
            # adjust the column's width to the header string
            tree.column(col, width=h[n], anchor=hd[n])

            n += 1

        for item in lista:
            tree.insert('', 'end', values=item)
        
    
        

    mostrar_tabela()


    root.mainloop()