## coding: utf-8 ## Avisa ao Python que o código está no formato UTF-8
# Universidade Federal de Campina Grande - CEEI - DEE  
# Redes de Computadores
# Professor: Leocarlos B. S. Lima
# 1º Módulo - Conceitos Gerais sobre redes. Internet. Camada de Aplicação
#
# Questão 02)
# Cliente de correio simples, que envia mensagem a qualquer destinatário.
# O cliente : 
#	a)estabelece conexão TCP com o servidor de correio GMAIL, 
#	b)dialoga com esse servidor usando o protocolo SMTP,
#	c)envia uma mensagem de correio a um destinatário pelo servidor de correio,
#	d)fecha a conexão TCP com o servidor de correio.
# Teste: enviar e-mail para contas de usuários difeentes.

# Referências: https://github.com/PabloVallejo/mail-client/blob/master/client.py
#              https://docs.python.org/3/library/ssl.html
#

# O módulo socket contém definições e instruções
# para interfaces de rede.
import socket
# Oferece segurança na camada de transporte, permitindo
# acessar servidores com gmail.
import ssl
import base64

#############################################
# Dados necessário ao enviar um e-mail
# E-mail e senha do remetente para efetuar login. Para teste, foi criado uma conta no gmail.
# Mensagem a ser enviada.
# Destinatário

#Login
remetente = 'aiaividaa@gmail.com' 
senha = 'vamoquevamo'
#Forma a mensagem base64 com o login e a senha
login = base64.b64encode('\000'+remetente+'\000'+senha) 

#Mensagem
mensagem = 'Deu certo. Pode dá 10!'
mensagem = mensagem + '\r\n.\r\n' 

#Destinatário
destinatario = 'srh00albuquerque@gmail.com'

##############################################

# Cria socket que possibilita uma conexão TCP/IP 
# por conta do argumentos passados na criação do objeto cliente.
cliente = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

# O servidor de correio GMAIL é acessado pelo endereço smtp.gmail.com.
ServidorGMAIL = 'smtp.gmail.com'
# A porta do servidor pode ser 465 ou 587. 465 quando se usa ssl. E 587
# quando se usa tls. 
porta = 587

#	a)estabelece conexão TCP com o servidor de correio GMAIL
cliente.connect((ServidorGMAIL, porta))

#	b)dialoga com esse servidor usando o protocolo SMTP
resposta = cliente.recv(1024)
print resposta

#   Comando EHLO
comandoEHLO = 'EHLO oie\r\n'
cliente.sendall(comandoEHLO) 
resposta = cliente.recv(1024)
print resposta


#   Comando STARTTLS
#   Informa que se trata de uma conexão segura para a camada de transporte
#    usando TLS.
comandoSTARTTLS = 'STARTTLS\r\n' 
cliente.send(comandoSTARTTLS) 
resposta = cliente.recv(1024)
print resposta

# Um objeto socket TLS é criado
clienteSSL = ssl.wrap_socket(cliente) 

#   Comando EHLO através da conexão TLS
comandoEHLO = 'EHLO oie\r\n'
clienteSSL.sendall(comandoEHLO) 
resposta = clienteSSL.recv(1024)
print(resposta)


# Comando de autenticação: AUTH PLAIN
# Enviado o comando de autenticação e o login, recebe autorização para continuar o dialogo.
clienteSSL.send('AUTH PLAIN ' + login + b'\r\n') 
resposta = clienteSSL.recv(1024)
print resposta

#Mensagens Padrão

clienteSSL.send('MAIL FROM: <'+ remetente +b'>\r\n')
resposta = clienteSSL.recv(1024)
print resposta

clienteSSL.send('RCPT TO: <'+destinatario+b'>\r\n')
resposta = clienteSSL.recv(1024)
print resposta

clienteSSL.send('DATA\r\n')
resposta = clienteSSL.recv(1024)
print resposta

clienteSSL.send('From: login\r\nTO: '+destinatario+b'\r\nSubject: Teste\r\n')#Envia o cabeçalho da mensagem
clienteSSL.send(mensagem)

resposta = clienteSSL.recv(1024)
print resposta

clienteSSL.close()










