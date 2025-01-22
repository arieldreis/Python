import flet as ft
def main(pagina): # O que essa função irá fazer?
    titulo = ft.Text("HASHZAP", size=12, color=ft.colors.WHITE)
    pagina.add(titulo)
    chat = ft.Column()
    pagina.add(chat)
    campo_enviar_mensagem = ft.TextField(label="Digite aqui a sua mensagem.", color=ft.colors.WHITE)
    pagina.bgcolor = ft.colors.BLUE
    def enviar_mensagem(evento): # Essa variável mostra a mensagem que o usuário digitar, tipo eu digito "Salve!" essa mensagem irá aparecer.
        if caixa_nome.value and campo_enviar_mensagem.value:
            mensagem_pessoa = ft.Text(f"{caixa_nome.value}: {campo_enviar_mensagem.value}", size=12, color=ft.colors.WHITE)
            chat.controls.append(mensagem_pessoa)
            campo_enviar_mensagem.value = ""
            chat.update()
            pagina.update()

    botao_enviar = ft.ElevatedButton("ENVIAR", on_click= enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
    def entrar_chat(evento): # Toda função que estiver associada a um botão deve ter o parâmetro evento.
        if not caixa_nome.value:
            titulo_popup.value = "Por favor, digite seu nome!"
            popup.update()
            return
        popup.open = False # Fechar o popup.
        pagina.dialog = None
        pagina.remove(titulo) # Sumir com o título.
        pagina.remove(botao) # sumir com o botão Iniciar Chat.
        chat_confirmado = ft.Text(f"{caixa_nome.value} entrou no chat.", size=12, color=ft.colors.WHITE)
        chat.controls.append(chat_confirmado)
        # carregar o chat.
        pagina.add(linha_enviar) # carregar o campo de enviar mensagem.
        pagina.update() # carregar o botão enviar.
    # Criar um PopUp
    titulo_popup = ft.Text("Bem vindo ao Hashzap", size=12, color=ft.colors.WHITE) # Aqui é o titulo do meu popup, o campo label é a mesma coisa que o placeholder.
    caixa_nome = ft.TextField(label="DIGITE O SEU NOME") # Aqui estará o input para ser digitado
    botao_popup = ft.ElevatedButton("ENTRAR NO CHAT", on_click=entrar_chat) # Aqui está o botão do meu popup
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome,
                           actions=[botao_popup]) # Aqui está variavel onde o popup será executado, todos os códigos que estão aqui nessa função serão executados
    def abrir_popup(evento): # Toda função que estiver associada a um botão deve ter o parâmetro evento.
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    botao = ft.ElevatedButton("INICIAR CHAT", on_click=abrir_popup)
    pagina.add(botao)
ft.app(main, view=ft.WEB_BROWSER) # Executar essa função com o flet