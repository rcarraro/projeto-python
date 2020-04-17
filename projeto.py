from datetime import datetime
data_e_hora_ = datetime.now()
data_e_hora = data_e_hora_.strftime('%d/%m/%Y %H:%M')
def pergunta():
    print("-=-"*10)
    print(data_e_hora)
    print("""
    1 - Novo Cliente
    2 - Apaga Cliente
    3 - Debita
    4 - Deposita
    5 - Saldo
    6 - Extrato
    0 - sai
    """)
    print(data_e_hora)
    print("-=-"*10)
#capta a ação da pessoa
pergunta()
a = int(input("Insira o número da ação que deseja executar: "))
#função para cadastrar
def cadastro():
    #abre o arquivo com a permissão de escrever
    arquivo = open("Cadastros.txt", "a")
    nome = input("Insira o seu nome: ")
    cpf = input("Insira o seu cpf: ")
    tipoconta = input("""Insira o tipo da sua conta:
Salário - 1
Comum - 2
Plus - 3
""")
    valorini = input("Insira o valor inicial de sua conta: ")
    senha = input("Insira a sua senha: ")
    #escreve no arquivo
    arquivo.write("nome: {} cpf: {} tipo de conta: {} Valor em conta: {} senha: {} ".format(nome,cpf,tipoconta,valorini,senha) + "\n")
    #fecha o arquivo
    arquivo.close
    #mensagem ao final do cadastro
    print("arquivo cadastrado com sucesso")

#função para apagar um cliente
def apagar():
    #pega o cpf do cliente que quer ser removido
    ncpf = input("insira o cpf: ")
    #abre o arquivo na função read(ler)
    arquivo = open("Cadastros.txt", "r")
    #abre o arquivo na função write(escrever)
    armazenamento = open("Cadastros2.txt", "w")
    #pega linha por linha e as reescreve com excessão da que se quer apagar
    for linha in arquivo:
        valor = linha.split()
        if valor[3] != ncpf:
            armazenamento.write(linha)
    print("Cadastro removido com sucesso!")

    #fecha os arquivos
    armazenamento.close()
    arquivo.close()
    #abre novamento os arquivos invertendo agora
    armazenamento = open("Cadastros2.txt", "r")
    arquivo = open("Cadastros.txt", "w")
    #reescreve todas no arquivo Cadastros.txt
    for linha in armazenamento:
        arquivo.write(linha)

#debitar um valor
def debitar():
    #pega o cpf do cliente
    ncpf = input("insira o cpf: ")
    #abre o arquivo com a função read(ler)
    arquivo = open("Cadastros.txt", "r")
    #abre o arquivo de armazenamento novamente
    armazenamento = open("Cadastros2.txt", "w")
    #procura a pessoa no banco de dados
    for linha in arquivo:
        valorcpf = linha.split()
        if ncpf == valorcpf[3]:
            print("usuario encontrado!")
            #pega a senha do cliente
            nsenha = input("insira sua senha: ")
            #verifica se a senha está correta
            if nsenha == valorcpf[13]:
                print("acesso permitido!")
                #pega o valor a ser debitado do cliente
                nvalor = float(input("insira o valor a ser debitado: "))
                #transforma o valor em float(número decimal)
                valorcpf[7] = float(valorcpf[7])
                #abre o arquivo que serão armazenados os extratos
                extratos = open("extratos.txt", "a")
                #detecta o tipo de conta Salario = 1, Comum = 2, Plus = 3 e já aplica a taxa
                if valorcpf[7] == 1:
                    tarifa = nvalor*.05
                    nvalor = nvalor*1.05
                    valorcpf[11] = float(valorcpf[11]) - nvalor 
                    #verifica se o valor está dentro do seu plano
                    if float(valorcpf[11]) < 0:
                        print("veirifique novamente as suas permissões!")
                        print("Erro ao debitar valor!")
                    else:       
                        #adiciona uma linha aos extratos
                        extratos.write("cpf: {} data: {} - {} Tarifa: {} Saldo: {}".format(ncpf, data_e_hora, nvalor, tarifa, valorcpf[11]) + "\n")
                        #armazena o valor
                        armazenamento.write("nome: {} cpf: {} tipo de conta: {} valor em conta: {} senha: {}".format(valorcpf[1],valorcpf[3],valorcpf[7],valorcpf[11],valorcpf[13]) + "\n")
                        print("valor debitado")
                elif valorcpf[7] == 2:
                    tarifa = nvalor*.03
                    nvalor = nvalor*1.03
                    valorcpf[11] = float(valorcpf[11]) - nvalor
                    #verifica se o valor está dentro do seu plano
                    if float(valorcpf[11]) < -500:
                        print("veirifique novamente as suas permissões!")
                        print("Erro ao debitar valor!")
                    else:       
                        #armazena o valor
                        armazenamento.write("nome: {} cpf: {} tipo de conta: {} valor em conta: {} senha: {}".format(valorcpf[1],valorcpf[3],valorcpf[7],valorcpf[11],valorcpf[13]) + "\n")
                        #adiciona uma linha aos extratos
                        extratos.write("cpf: {} data: {} - {} Tarifa: {} Saldo: {}".format(ncpf, data_e_hora, nvalor, tarifa, valorcpf[11]) + "\n")
                        print("valor debitado")
                elif valorcpf[7] == 3:
                    tarifa = nvalor*.01
                    nvalor = nvalor*1.01
                    valorcpf[11] = float(valorcpf[11]) - nvalor
                    #verifica se o valor está dentro do seu plano
                    if float(valorcpf[11]) < -5000:
                        print("veirifique novamente as suas permissões!")
                        print("Erro ao debitar valor!")
                    else:       
                        #adiciona uma linha aos extratos
                        extratos.write("cpf: {} data: {} - {} Tarifa: {} Saldo: {}".format(ncpf, data_e_hora, nvalor, tarifa, valorcpf[11]) + "\n")
                        #armazena o valor
                        armazenamento.write("nome: {} cpf: {} tipo de conta: {} valor em conta: {} senha: {}".format(valorcpf[1],valorcpf[3],valorcpf[7],valorcpf[11],valorcpf[13]) + "\n")
                        print("valor debitado")      
            else:
                print("acesso negado!")
        else:
            armazenamento.write(linha)

    #fecha os arquivos
    arquivo.close()
    armazenamento.close()
    #abre novamento os arquivos invertendo agora
    armazenamento = open("Cadastros2.txt", "r")
    arquivo = open("Cadastros.txt", "w")
    #reescreve todas no arquivo Cadastros.txt
    for linha in armazenamento:
        arquivo.write(linha)


def depositar():
    #pega o cpf do cliente
    ncpf = input("insira o cpf: ")
    #abre o arquivo com a função read(ler)
    arquivo = open("Cadastros.txt", "r")
    armazenamento = open("Cadastros2.txt", "w")
    #procura a pessoa no banco de dados
    for linha in arquivo:
        valorcpf = linha.split()
        if ncpf == valorcpf[3]:
            print("usuario encontrado!")
            #valor que a pessoa deseja depositar
            nvalor = float(input("Valor a ser depositado: "))
            #abre o arquivo que serão armazenados os extratos
            extratos = open("extratos.txt", "a")
            #soma o valor
            valorcpf[11] = float(valorcpf[11]) + nvalor
            #adiciona uma linha aos extratos
            extratos.write("cpf: {} data: {} + {} Tarifa: 0.00 Saldo: {}".format(ncpf, data_e_hora, nvalor, valorcpf[11]) + "\n")
            #armazena o valor
            armazenamento.write("nome: {} cpf: {} tipo de conta: {} valor em conta: {} senha: {}".format(valorcpf[1],valorcpf[3],valorcpf[7],valorcpf[11],valorcpf[13]) + "\n")
        else:
            armazenamento.write(linha)
    print("valor depositado com sucesso!")
    #fecha os arquivos
    arquivo.close()
    armazenamento.close()
    extratos.close()
    #abre novamento os arquivos invertendo agora
    armazenamento = open("Cadastros2.txt", "r")
    arquivo = open("Cadastros.txt", "w")
    #reescreve todas no arquivo Cadastros.txt
    for linha in armazenamento:
        arquivo.write(linha)
    

#função para ver o saldo
def Saldo():
    #pega o cpf do cliente
    ncpf = input("insira o cpf: ")
    #abre o arquivo com a função read(ler)
    arquivo = open("Cadastros.txt", "r")
    #procura a pessoa no banco de dados
    for linha in arquivo:
        valorcpf = linha.split()
        if ncpf == valorcpf[3]:
            print("usuario encontrado!")
            #pega a senha do cliente
            nsenha = input("insira sua senha: ")
            #verifica se a senha está correta
            if nsenha == valorcpf[13]:
                print("acesso permitido!")
                print()
                print("saldo: ",valorcpf[11])
                print()
    
#ver o extrato
def extrato():
    a = 0
    #pega o cpf do cliente
    ncpf = input("insira o cpf: ")
    #abre o arquivo com a função read(ler)
    arquivo = open("Cadastros.txt", "r")
    #abre o extrato com a função read(ler)
    extrato = open("extratos.txt", "r")
    #procura a pessoa no banco de dados
    for linha in arquivo:
        valorcpf = linha.split()
        if ncpf == valorcpf[3]:
            print("usuario encontrado!")
            #pega a senha do cliente
            nsenha = input("insira sua senha: ")
            #verifica se a senha está correta
            if nsenha == valorcpf[13]:
                print("acesso permitido!")
                for linha1 in extrato:
                    valorcpf2 = linha1.split()
                    #confere o cpf
                    if valorcpf2[1] == ncpf:
                        if a == 0:
                            #printa o extrato
                            print(valorcpf[0], valorcpf[1])
                            print(valorcpf[2], valorcpf[3])
                            #transforma o item da tabela em int
                            valorcpf[7] = float(valorcpf[7])
                            #verifica o tipo da sua conta e printa
                            if valorcpf[7] == 1:
                                
                                print(valorcpf[4], valorcpf[5], valorcpf[6], "Salário")
                            if valorcpf[7] == 2:
                                print(valorcpf[4], valorcpf[5], valorcpf[6], "Comum")
                            if valorcpf[7] == 3:
                                print(valorcpf[4], valorcpf[5], valorcpf[6], "Plus")
                            a = a + 1    
                        
                        print(valorcpf2[2], valorcpf2[3], valorcpf2[4], valorcpf2[5], valorcpf2[6], valorcpf2[7], valorcpf2[8], valorcpf2[9], valorcpf2[10])
                    
#looping infinito
while a != 0:
    if a == 1:
        cadastro()
        pergunta()
        a = int(input("Insira o número da ação que deseja executar: "))
    elif a == 2:
        apagar()
        pergunta()
        a = int(input("Insira o número da ação que deseja executar: "))
    elif a == 3:
        debitar()
        pergunta()
        a = int(input("Insira o número da ação que deseja executar: "))
    elif a == 4:
        depositar()
        pergunta()
        a = int(input("Insira o número da ação que deseja executar: "))
    elif a == 5:
        Saldo()
        pergunta()
        a = int(input("Insira o número da ação que deseja executar: "))
    elif a == 6:
        extrato()
        pergunta()
        a = int(input("Insira o número da ação que deseja executar: "))
    else:
        print("insira um valor válido!")
        a = int(input("Insira o número da ação que deseja executar: "))

print("Muito obrigado, até logo!")
