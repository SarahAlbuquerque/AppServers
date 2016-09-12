## coding: utf-8 ## Avisa ao Python que o código está no formato UTF-8
# Universidade Federal de Campina Grande - CEEI - DEE  
# Redes de Computadores
# Professor: Leocarlos B. S. Lima
# 1º Módulo - Conceitos Gerais sobre redes. Internet. Camada de Aplicação
#
# Questão 01)
# Servidor Web simples, capaz de processar apenas uma requisição.
# O servidor Web deverá:
#	a) criar um socket de conexão quando contatado por um cliente (navegador);
#	b) receber requisição HTTP dessa conexão;
#	c) analisar a requisição p/ determinar o arquivo específico sendo requisitado;
#	d) obter o arquivo solicitado do sistema de arquivo do servidor;
#	e) criar uma mensagem de resposta HTTP consistindo no arquivo requisitado
#		precedido por linhas de cabeçalho.
#	f) enviar resposta pela conxão TCP ao navegador requisitante
#
# Se o navegador requisitar um arquivo que não está disponivel no servidor,
# este retornará uma mensagem de erro "404 Não Encontrado"
#
# O servidor foi testado enviando requisições de navegadores rodando
# em hospedeiros diferentes e não obteve o resutado esperado.

# O módulo socket contém definições e instruções
# para interfaces de rede.
import socket 
# Módulo que permite usar funcionalidade do sistema operacional
import os 


# Cria o objeto socket através da função socket().
# Através do objeto socket s criado, é possível usar
# funcionalidades da classe socket.
# Na criação do objeto s, a família de endereços é especificada. 
# Para o servidor foi usada a família AF_INET que usa o par 
# (hospedeiro, porta). O hospedeiro é uma string representada
# por um 'hostname' em notação de domínio da internet ou um endereço
# IPv4. A porta é um inteiro. O SOCK_STREAM indica TCP.

# Para servidor Web, atribui-se valor da porta igual a 80.
# Feito isso, no navegador, pode-se digitar apenas o nome do 
# hospedeiro, por exemplo: pode ser https://end_ip:80 ou https://end_ip.
# Nessa aplicação, usa-se a função socket.gethostname() para nomear 
# hospedeiro. Tenta-se também usar essa função para que se consiga
# acessar o servidor usando navegadores em hospedeiros diferentes.
# Isso não foi conseguido.
 
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
porta = 80; 
end_ip = socket.gethostname();
print 'Use o seguinte nome para acessar o servidor:\r\n' + end_ip + '\r\n'

#.SO_REUSEADDR: permite reutilizar um socket local no estado de
# espera sem esperar por seu tempo limite natural para expirar.
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Associa um endereço ao socket.
s.bind((end_ip,porta))


# Habilita o servidor para aceitar conexões. O valor passado 
# como parâmentro indica o numero de conexões aceitas pelo sistema
# antes de recusar novas conexões.
s.listen(1) 


while True:
#	a) criar um socket de conexão quando contactado por um cliente 
#      (navegador);

	# O socket deve estar vinculado a um endereço e aguardando as conexões.
	# Usando a função accept(), ela retorna o socket conexão que é 
	# usado para enviar e receber dados na conexão. E o endereco
	# vinculado a outra extremidade da conexão.
	# Então, um socket conexão é criado quando o socket aceita a conexão.
	conexao, endereco = s.accept() 
	
#	b) receber requisição HTTP dessa conexão;
	# Recebe a requisição através da conexão
	requisicao = conexao.recv(2048)
	
	print 'Requisição:\r\n' + requisicao + '\r\n'
	
#	c) analisar a requisição p/ determinar o arquivo 
#		específico sendo requisitado;	

	 
	# Como essa aplicação é de um servidor 
	# simples para responder à requisição de um arquivo
	# identificado no campo URL, se considerará apenas
	# o método GET vindo da requisição. Não sendo possível
	# outro método.
	
	# Se nada foi requisitado, não há arquivo.
	# Caso contrário - algo foi requisitado,
	# a requisição é separada através de espaço em brancos. 
	# O primeiro valor é o método que, para essa aplicação, sempre
	# será o GET. O segundo valor será o arquivo desejado e, esse é
	# idexado por 1 na lista de strings gerada pela função split.
	if not requisicao:
		arquivoPedido = '';
	else:
		requisicao = requisicao.split()
		arquivoPedido = requisicao[1]
		
#	d) obter o arquivo solicitado do sistema de arquivo do servidor;
	if os.path.isfile(arquivoPedido):
#	e) criar uma mensagem de resposta HTTP consistindo no arquivo 
#		requisitado precedido por linhas de cabeçalho.
		arquivo = open(arquivoPedido,'r')
		msg = arquivo.read() 
		msgOK = 'HTTP/1.1 200 OK\r\n\r\n' + arquivoPedido + ' existe:\n\n'
		msgFinal = msgOK + msg
#	f) enviar resposta pela conxão TCP ao navegador requisitante
		conexao.send(msgFinal)
		print 'Arquivo enviado com sucesso'
# Se o navegador requisitar um arquivo que não está disponivel no servidor,
# este retornará uma mensagem de erro "404 Não Encontrado"	
	else :
		msgErro = 'HTTP/1.1 404 Not Found\r\n'
		msgErro = msgErro + '\r\n' + '404 Não Encontrado'
		conexao.send(msgErro)
		print 'Arquivo n enviado com sucesso'
	conexao.close()
# Usando o break, apenas uma requisição é processada.
#	break 
	
# O servidor foi testado enviando requisições de navegadores rodando
# em hospedeiros diferentes e não obteve o resutado esperado.
	

