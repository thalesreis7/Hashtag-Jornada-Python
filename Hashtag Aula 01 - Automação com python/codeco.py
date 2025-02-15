import pyautogui
import pandas
import time
pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever
# pyautogui.hotkey -> atalho de teclado

#Passo 1: Abrir o sistema da empresa
    #-Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
    #Abrir o opera e entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
#pedir para o programa esperar 3 segundos, por conta da internet para carregar o site
time.sleep(3) #para esperar os 3 segundo só ai ir para o Login 

#Passo 2: Fazer Login
pyautogui.click(x=445, y=364)
pyautogui.write('gdmo.joymax@gmail.com')

pyautogui.press('tab') #passar para o campo de senha
pyautogui.write('1234567')

pyautogui.press('tab')#passa para o botão login
pyautogui.press('enter')
 

#Passo 3: Importar a base de dados  dos produtos
tabela = pandas.read_csv('produtos.csv')#para ler a base de dados dos produtos, com a variável tabela

print(tabela)

time.sleep(3) #para carregar a página se tiver net lenta
#Passo 4: Cadastrar 1 produto

for linha in tabela.index: 
    pyautogui.click(x=452, y=243) #clica no primeiro campo
    #sempre colocar um produto a mão para testar a lógica
    # MOLO000251,Logitech,Mouse,1,25.95,6.50,

    #código do produto
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    #marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    #tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')

    #categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    #preco_unitario
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    #custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    #obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter') #apertar o botão de 

    #numero positivo = scroll para cima
    #numero negativo = scroll para baixo
    pyautogui.scroll(10000)

#para pausar uma automação infinita no pyautogui é só levar o mouse para o canto superior esquerdo que ele ativa a trava de segurança

#Passo 5: Repetir o passo 4 até acabar os produtos

#nan no python é vazio not a number


#vamos utilizar o pyautogui que é uma Library para automação em Python é só instalar uma vez, n precisa instalar a cada projeto e outra que é o pandas e junto o pacote openpyxl para ciência de Dados
#pip install pyautogui
#pip install pandas openpyxl