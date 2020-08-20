from tkinter import *
from tkinter import ttk, messagebox

''' ----------------- CRIANDO UMA TELA --------------------'''
screen = Tk() # Instancia um objeto do tipo TK 
screen.geometry('500x500+600+400') # Tamanho da tela - String -> 'Largura x Altura + Posição em X na tela + Posição na tela em Y'
screen['bg']= 'black' # Cor de fundo da tela (background)
screen.title('Programando com Tkinter')

''' ----------------- CRIANDO UMA LABEL --------------------'''

label = Label(
    master = screen, # Define a qual tela o widget pertence
    text = 'Exemplo Label',
    bg = 'gold', # Cor de fundo (background)
    fg = 'red', # Cor da fonte (foreground)
    font = 'Arial 12 bold',
    width = 15 # Largura 
)
label.pack(
    side = BOTTOM, # SIDE (Posição na tela): BOTTOM (BASE), TOP (TOPO), LEFT(ESQUERDA), RIGHT (DIREITA)
    fill = X) # Cobre toda a área no sentido Horizontal (X) - Para sentido verfical, usar fill = Y

''' Mais configurações para Labels: 
    activebackground, activeforeground, anchor,
    background, bitmap, borderwidth, cursor,
    disabledforeground, font, foreground,
    highlightbackground, highlightcolor,
    highlightthickness, image, justify,
    padx, pady, relief, takefocus, text,
    textvariable, underline, wraplength '''


''' ----------------- CRIANDO UM BOTÃO --------------------'''
button = Button(
    master = screen, # Define a qual tela o widget pertence
    text = 'Exemplo Botão',
    bg = 'red', # Cor de fundo (background)
    fg = 'blue', # Cor da fonte (foreground)
    relief="groove", # tipo do design do botão ---> Opções: 
    border=10, # Tamanho do design relief - quanto maior, mais evidente serão os detalhes
    font="Times 24 bold",
    width = 20, # Largura do botão,
    command = None # Comando para quando o botão for clicado - deve ser uma função que não recebe parâmetros!!!
)

button.pack(side = TOP,# SIDE (Posição na tela): BOTTOM (BASE), TOP (TOPO), LEFT(ESQUERDA), RIGHT (DIREITA)
 fill = None) # Cobre toda a área no sentido Horizontal (X) - Para sentido verfical, usar fill 

''' Mais configurações para Buttons:
    activebackground, activeforeground, anchor,
    background, bitmap, borderwidth, cursor,
    disabledforeground, font, foreground
    highlightbackground, highlightcolor,
    highlightthickness, image, justify,
    padx, pady, relief, repeatdelay,
    repeatinterval, takefocus, text,
    textvariable, underline, wraplength
   '''
# Configurações Específicas para botões : command, compound, default, height, overrelief, state, width

''' ----------------- CRIANDO UMA ENTRADA DE DADOS --------------------'''
lb = Label(screen, text = 'ENTRADA DE DADOS: ').pack()
entry = Entry(
    justify = CENTER,
    background = 'green',
    fg = 'white',
    relief = FLAT,
    width = 15
    )
entry.pack()

''' Mais configurações para Entries:
    background, bd, bg, borderwidth, cursor,
    exportselection, fg, font, foreground, highlightbackground,
    highlightcolor, highlightthickness, insertbackground,
    insertborderwidth, insertofftime, insertontime, insertwidth,
    invalidcommand, invcmd, justify, relief, selectbackground,
    selectborderwidth, selectforeground, show, state, takefocus,
    textvariable, validate, validatecommand, vcmd, width,
    xscrollcommand.
    '''

''' ----------------- CRIANDO UMA ABA --------------------'''
#Importar a classe ttk do tkinter!

abas = ttk.Notebook(screen) # Instancia um objeto do tipo Notebook que vai receber as abas na tela escolhida, no caso, SCREEN
abas.pack(expand = 1, fill = BOTH)

primeira_aba = ttk.Frame(abas) #Cria um FRAME no notebook ABAS
abas.add(primeira_aba, text = 'PRIMEIRA ABA') # add o frame criado ao notebook

#Para criar widgets nas abas é só passar como parametro a aba em que desejar colocar o objeto
texto_primeiraAba = Label(primeira_aba, text = 'COLOCANDO UMA LABEL').pack()

segunda_aba = ttk.Frame(abas)
segunda_aba = Frame(bg = 'black') #Para mudar a cor da aba, é necessário acessar parametros do objeto tipo FRAME
abas.add(segunda_aba, text = 'SEGUNDA ABA')

#Criando uma mensagem - importar classe messagebox do tkinter
def mensagem():
    messagebox.showinfo('MENSAGEM', 'Você Apertou o Botão da Segunda Aba')

bt_segundaAba = Button(segunda_aba, text = 'APERTE', command = mensagem)
bt_segundaAba.pack()

''' ----------------- CRIANDO UMA SEGUNDA TELA --------------------'''
#Criaremos a segunda tela para ser acessada somente quando um botão na tela SCREEN for clicado

#Vamos definir uma função que criará a tela:

def cria_segunda_tela():
    segunda_tela = Toplevel(screen)
    segunda_tela.title('Segunda Tela')
    segunda_tela.geometry('300x300+700+700')
    segunda_tela['bg'] = 'gold'

    lb = Label(segunda_tela, text = 'TELA CRIADA!').pack()

#Vamos criar um novo botão na primeira aba:

bt_primeira_aba = Button(primeira_aba, text = 'Click para abrir uma nova tela',
command = cria_segunda_tela)
bt_primeira_aba.pack(side = BOTTOM)


''' ----------------- CRIANDO UM MENU --------------------'''

menu_principal = Menu(screen) #Instanciando o objeto do tipo MENU e dizendo à qual tela ele pertence
menu = Menu(menu_principal) #Criando um MENU dentro do objeto instanciado
menu.add_command(label = 'Opção 1', command = None) # ADD labels e comandos de click
menu.add_command(label = 'Opção 2',command = None)
menu.add_command(label = 'Opção 3')
menu_principal.add_cascade(label = 'OPÇÕES', menu = menu) #Add os labels criados no estipo cascata ao menu

segundo_menu = Menu(menu_principal)
segundo_menu.add_command(label = 'ONE')
segundo_menu.add_command(label = 'TWO')
segundo_menu.add_command(label = 'Tree')
menu_principal.add_cascade(label = 'OUTRAS OPÇÕES', menu = segundo_menu)

''' ----------------- CRIANDO UMA SCROLLBAR E LISTBOX--------------------'''
lista = Listbox(screen, width = 10, height = 10) #Criando a área para a scrollbar
lista.pack(side = LEFT)

barra_rolagem = Scrollbar(screen) # Cria a barra de rolagem 
barra_rolagem.pack(side = LEFT)
barra_rolagem.configure(command = lista.yview) # Passa a lista de nomes com o parametro yview para rolagem

lista_nomes = ['Renato','BIA','Julia','João','Carlos','Livia',
1,2,3,4,5,6,7,8,9,10]
for nome in lista_nomes:
    lista.insert(END,nome)


screen.configure(menu = menu_principal) #Adiciona o menu criado à tela SCREEN
''' ----------------- CRIANDO UMA ...--------------------'''


screen.mainloop() # Aplica um loop na aplicação