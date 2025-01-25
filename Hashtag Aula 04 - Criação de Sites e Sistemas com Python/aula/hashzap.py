# Tela inicial:
    # Botão: iniciar Chat
        # quando clicar no botão:
        # abrir um popup/modal/alerta
            # Título: bem vindo ao Hashzap
            # Caixa de texo: escreva seu nome no chat
            # Botão: entrar no chat
                # Quando clicar no botão 
                # fechar o popup 
                # sumir com o título 
                # sumir com o botão iniciar Chat 
                    # Carregar o Chat
                    # carregar o campo de enviar mensagem: "Digite sua mensagem"
                    # Carregar o botão enviar
                        # Quando clicar no botão enviar
                        # enviar a mensagem
                        # limpar a caixa de mensagem

# Para criar sites
    # Flask
    # Django
# Para criar aplicativo
    # Kivy
# Para criar telas para seus programas
    # Tkinter

# Para criar sites, aplicativos e programas de computador
    # Flet -> constroi o front e o back-end, com o mesmo código constroi sites, apps e programas
    # instalação
        # pip install flet
        
# 3 etapas que sempre tem que fazer no Flet
    # importar o flet
import flet as ft

    
    # criar uma função principal para rodar o seu aplicativo
def main(pagina):
    # titulo
    titulo = ft.Text("Hashzap")

    
    def enviar_mensagem_tunel(mensagem):
        # executar tudo que eu quero que aconteça para todos os usuários que receberem a mensagem
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        # para limpar a caixa de enviar mensagem
        campo_enviar_mensagem.value = ""
        pagina.update()
    
    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem aqui", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
    chat = ft.Column()
    
    def entrar_chat(evento):
        # fechar o popup 
        popup.open = False
        # sumir com o título
        pagina.remove(titulo)
        # sumir com o botão iniciar Chat
        pagina.remove(botao)
        # carregar o chat 
        pagina.add(chat)
        # carregar o campo de enviar mensagens 
        # carregar o botão de enviar
        pagina.add(linha_enviar)
        
        #adicionar no chat a mensagem "Fulano entrou no chat"
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario}: entrou no chat"
        pagina.pubsub.send_all(mensagem)
        
        pagina.update()
    
    # crair o popup
    titulo_popup = ft.Text("Bem vindo ao Hashzap!")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])
    
    # botao inicial
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
               
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    
    # colocar os elementos na página
    pagina.add(titulo)
    pagina.add(botao)
    
# executar essa função com o flet
ft.app(main, view=ft.WEB_BROWSER)#WEB_BROWSER para rodar a aplicação no nagevador
