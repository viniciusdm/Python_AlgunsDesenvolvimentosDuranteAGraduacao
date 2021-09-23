#Biblioteca usadas
import numpy as np
import math
import matplotlib.pyplot as plt


#Cabecalho
print("MAP3121 - EP1 de Cálculo Numérico - 05/2020")
print("Nome: Vincius Bueno de Moraes | Turma:03")
print("NUSP: 10256432 | Email: viniciusbuenodemoraes@hotmail.com")
print()
print("Este Exercício Programa conta com diferentes modos de operação,")
print("cabendo ao usuário a escolha. Mais detalhes de funcionamento estão")
print("dispostos no arquivo \"LEIAME.txt\" anexado a pasta do trabalho.")
print()
exer = int(input("Escolha a Tarefa (1 ou 2): "))
item = str(input("Esolha o item da Tarefa digitada que deseja (a, b ou c): "))

if exer == 1:
    if item == "a" or item == "A":
        modo = int(input("Escolha entre a primeira (1) ou segunda (2) f(t,x): "))
        if modo == 1:
            print()
            print("##### Você escolheu a Tarefa 1, item a, primeira f(t,x) #####")
            print()
            
            #Entrada de parametros
            T = int(input("Digite o valor de T: "))
            N = int(input("Digite o valor de N: "))
            lambida = float(input("Digite o valor de λ: "))
            dx = float = 1/N
            print ("Δx = ", dx)

            #Cálculo do Delta T 
            dt_ast = float = (dx**2)*lambida

            #Cálculo de M
            M_ast = float = T/dt_ast

            #Normalizacao de M para inteiro
            M = int = math.ceil(M_ast)
            print ("M = ", M)

            #Correcao do Delta T 
            dt = float = T/M
            print ("Δt = ", dt)

            #Criacao de vetor
            vetor = np.zeros((M+1, N+1))
            vetor_grafico = np.zeros ((N+1, 11))

            #Variaveis necessárias:
            k = 0
            j = 1
            l = 0
            e = 0
            
            #Laco Principal de Trabalho
            while k <= M:
                tk = round(k*dt, 6)
                i = 0
                while i <= N:
                    xi = float = i*dx
                    if k == 0:
                        u = 0
                    elif i == 0 or i == N:
                        u = 0
                    else:
                        u = vetor[k-1, i]+dt*(((vetor[k-1, i-1]-2*vetor[k-1, i]+vetor[k-1, i+1])/dx**2) + 10*xi**2*(xi-1)-60*xi*tk+20*tk)
                    vetor[k, i] = u
                    #Novo vetor (Necessario para plotar com variacao de 0,1 em 0,1 de t)
                    if tk == 0.0 or tk == 0.1 or tk == 0.2 or tk == 0.3 or tk == 0.4 or tk == 0.5 or tk == 0.6 or tk == 0.7 or tk == 0.8 or tk == 0.9 or tk == 1.0:
                        vetor_grafico[i, l] = u
                        if i == N:
                            l = l + 1
                    #Calculo do Erro
                    if k == M:
                        novo_e = 10*tk*xi**2*(xi-1) - vetor[k, i]
                        if abs(novo_e) > abs(e):
                            e = novo_e
                            e = abs(e)
                    i = i + 1
                j = j + 1
                k = k + 1
            print ("erro = ", e)
            #Plotagem dos dados
            plt.suptitle("Item: 1.a) Eq. \"1\" - Gráfico da Solução Encontrada x t")
            plt.title("N: " +str(N)+ " e λ: " +str(lambida)+ " | Erro: " +str(e))
            plt.xlabel("Posição")
            plt.ylabel("y - Solução (u)")
            linha = np.linspace(0, 1, N+1)
            plt.plot(linha, vetor_grafico[0:N+1, 0], label="t : 0.0")
            plt.plot(linha, vetor_grafico[0:N+1, 1], label="t : 0.1")
            plt.plot(linha, vetor_grafico[0:N+1, 2], label="t : 0.2")
            plt.plot(linha, vetor_grafico[0:N+1, 3], label="t : 0.3")
            plt.plot(linha, vetor_grafico[0:N+1, 4], label="t : 0.4")
            plt.plot(linha, vetor_grafico[0:N+1, 5], label="t : 0.5")
            plt.plot(linha, vetor_grafico[0:N+1, 6], label="t : 0.6")
            plt.plot(linha, vetor_grafico[0:N+1, 7], label="t : 0.7")
            plt.plot(linha, vetor_grafico[0:N+1, 8], label="t : 0.8")
            plt.plot(linha, vetor_grafico[0:N+1, 9], label="t : 0.9")
            plt.plot(linha, vetor_grafico[0:N+1, 10], label="t : 1.0")
            plt.legend()
            plt.grid()
            plt.show()
            
        elif modo == 2:
            print()
            print("##### Você escolheu a Tarefa 1, item a, segunda f(t,x) #####")
            print ()
            
            #Entrada de parametros
            T = int(input("Digite o valor de T: "))
            N = int(input("Digite o valor de N: "))
            lambida = float(input("Digite o valor de λ: "))
            dx = float = 1/N
            print ("Δx = ", dx)

            #Cálculo do Delta T 
            dt_ast = float = (dx**2)*lambida

            #Cálculo de M
            M_ast = float = T/dt_ast

            #Normalizacao de M para inteiro
            M = int = math.ceil(M_ast)
            print ("M = ", M)

            #Correcao do Delta T 
            dt = float = T/M
            print ("Δt = ", dt)

            #Criacao de vetor
            vetor = np.zeros((M+1, N+1))
            vetor_grafico = np.zeros ((N+1, 11))

            #Variaveis necessárias:
            k = 0
            j = 1
            l = 0
            e = 0
            
            #Laco Principal de Trabalho
            while k <= M:
                tk = round(k*dt, 6)
                i = 0
                while i <= N:
                    xi = float = i*dx
                    if k == 0:
                        u = (xi**2)*((1-xi)**2)
                    elif i == 0 or i == N:
                        u = 0
                    else:
                        u = vetor[k-1, i]+dt*(((vetor[k-1, i-1]-2*vetor[k-1, i]+vetor[k-1, i+1])/dx**2) + 10*math.cos(10*tk)*(xi**2)*((1-xi)**2)-(1+math.sin(10*tk))*(12*(xi**2)-12*xi+2))
                    vetor[k, i] = u
                    #Novo vetor (Necessario para plotar com variacao de 0,1 em 0,1 de t)
                    if tk == 0.0 or tk == 0.1 or tk == 0.2 or tk == 0.3 or tk == 0.4 or tk == 0.5 or tk == 0.6 or tk == 0.7 or tk == 0.8 or tk == 0.9 or tk == 1.0:
                        vetor_grafico[i, l] = u
                        if i == N:
                            l = l + 1
                    #Calculo do Erro
                    if k == M:
                        novo_e = (1 + math.sin(10*tk))*xi**2*(1-xi)**2 - vetor[k, i]
                        if abs(novo_e) > abs(e):
                            e = novo_e
                            e = abs(e)
                    i = i + 1
                j = j + 1
                k = k + 1
            print ("erro = ", e)
            #Plotagem dos dados
            plt.suptitle("Item: 1.a) Eq. \"2\" - Gráfico da Solução Encontrada x t")
            plt.title("N: " +str(N)+ " e λ: " +str(lambida)+ " | Erro: " +str(e))
            plt.xlabel("Posição")
            plt.ylabel("y - Solução (u)")
            linha = np.linspace(0, 1, N+1)
            plt.plot(linha, vetor_grafico[0:N+1, 0], label="t : 0.0")
            plt.plot(linha, vetor_grafico[0:N+1, 1], label="t : 0.1")
            plt.plot(linha, vetor_grafico[0:N+1, 2], label="t : 0.2")
            plt.plot(linha, vetor_grafico[0:N+1, 3], label="t : 0.3")
            plt.plot(linha, vetor_grafico[0:N+1, 4], label="t : 0.4")
            plt.plot(linha, vetor_grafico[0:N+1, 5], label="t : 0.5")
            plt.plot(linha, vetor_grafico[0:N+1, 6], label="t : 0.6")
            plt.plot(linha, vetor_grafico[0:N+1, 7], label="t : 0.7")
            plt.plot(linha, vetor_grafico[0:N+1, 8], label="t : 0.8")
            plt.plot(linha, vetor_grafico[0:N+1, 9], label="t : 0.9")
            plt.plot(linha, vetor_grafico[0:N+1, 10], label="t : 1.0")
            plt.legend()
            plt.grid()
            plt.show()
            
    elif item == "b" or item == "B":
        print()
        print("##### Você escolheu a Tarefa 1, item b, Condições Determinadas #####")
        print()
        
        #Entrada de parametros
        T = int(input("Digite o valor de T: "))
        N = int(input("Digite o valor de N: "))
        lambida = float(input("Digite o valor de λ: "))
        dx = float = 1/N
        print ("Δx = ", dx)

        #Cálculo do Delta T 
        dt_ast = float = (dx**2)*lambida

        #Cálculo de M
        M_ast = float = T/dt_ast

        #Normalizacao de M para inteiro
        M = int = math.ceil(M_ast)
        print ("M = ", M)

        #Correcao do Delta T 
        dt = float = T/M
        print ("Δt = ", dt)

        #Criacao de vetor
        vetor = np.zeros((M+1, N+1))
        vetor_grafico = np.zeros ((N+1, 11))

        #Variáveis necessárias de trabalho
        k = 0
        j = 1
        l = 0
        e = 0

        #Laco Principal de Trabalho
        while k <= M:
            tk = round(k*dt, 6)
            i = int = 0
            while i <= N:
                xi = float = i*dx
                if k == 0:
                    u = math.exp(-xi)
                elif i == 0:
                    u = math.exp(tk)
                elif i == N:
                    u = math.exp(tk-1)*math.cos(5*tk)
                else:
                    u = vetor[k-1, i]+dt*(((vetor[k-1, i-1]-2*vetor[k-1, i]+vetor[k-1, i+1])/dx**2) + math.exp(tk-xi)*(25*tk**2*math.cos(5*xi*tk)-5*math.sin(5*tk*xi)*(xi+2*tk)))                                                                                                                                                                
                vetor[k, i] = u
                #Novo vetor (Necessario para plotar com variacao de 0,1 em 0,1 de t)
                if tk == 0.0 or tk == 0.1 or tk == 0.2 or tk == 0.3 or tk == 0.4 or tk == 0.5 or tk == 0.6 or tk == 0.7 or tk == 0.8 or tk == 0.9 or tk == 1.0:
                    vetor_grafico[i, l] = u
                    if i == N:
                        l = l + 1
                #Calculo do Erro
                if k == M:
                    a = math.exp(tk-xi)*math.cos(5*tk*xi)
                    novo_e = a - vetor[k, i]
                    if abs(novo_e) > abs(e):
                        e = novo_e
                        e = abs(e)
                i = i + 1
            j = j + 1
            k = k + 1
        print ("erro = ", e)
        #Plotagem dos dados
        plt.suptitle("Item: 1.b) - Gráfico da Solução Encontrada x t")
        plt.title("N: " +str(N)+ " e λ: " +str(lambida)+ " | Erro: " +str(e))
        plt.xlabel("Posição")
        plt.ylabel("y - Solução (u)")
        linha = np.linspace(0, 1, N+1)
        plt.plot(linha, vetor_grafico[0:N+1, 0], label="t : 0.0")
        plt.plot(linha, vetor_grafico[0:N+1, 1], label="t : 0.1")
        plt.plot(linha, vetor_grafico[0:N+1, 2], label="t : 0.2")
        plt.plot(linha, vetor_grafico[0:N+1, 3], label="t : 0.3")
        plt.plot(linha, vetor_grafico[0:N+1, 4], label="t : 0.4")
        plt.plot(linha, vetor_grafico[0:N+1, 5], label="t : 0.5")
        plt.plot(linha, vetor_grafico[0:N+1, 6], label="t : 0.6")
        plt.plot(linha, vetor_grafico[0:N+1, 7], label="t : 0.7")
        plt.plot(linha, vetor_grafico[0:N+1, 8], label="t : 0.8")
        plt.plot(linha, vetor_grafico[0:N+1, 9], label="t : 0.9")
        plt.plot(linha, vetor_grafico[0:N+1, 10], label="t : 1.0")
        plt.legend()
        plt.grid()
        plt.show()
        
    elif item == "c" or item == "C":
        print()
        print("##### Você escolheu a Tarefa 1, item c, Fonte Pontual #####")
        print()
        #Entrada de parametros
        T = int(input("Digite o valor de T: "))
        N = int(input("Digite o valor de N: "))
        lambida = float(input("Digite o valor de λ: "))
        dx = float = 1/N
        print ("Δx = ", dx)

        #Cálculo do Delta T 
        dt_ast = float = (dx**2)*lambida

        #Cálculo de M
        M_ast = float = T/dt_ast

        #Normalizacao de M para inteiro
        M = int = math.ceil(M_ast)
        print ("M = ", M)

        #Correcao do Delta T 
        dt = float = T/M
        print ("Δt = ", dt)

        #Criacao de vetor
        vetor = np.zeros((M+1, N+1))
        vetor_grafico = np.zeros ((N+1, 11))

        #Variaveis necessárias:
        k = 0
        j = 1
        l = 0
        #Laco Principal de Trabalho
        while k <= M:
            tk = round(k*dt, 6)
            i = 0
            while i <= N:
                xi = float = i*dx
                g = 0
                if k == 0:
                    u = 0
                elif xi >= (0.25-dx/2):
                    if xi <= (0.25+dx/2):
                        g = 1/dx
                r = (10000*(1-2*tk**2))*g
                if i == 0 or i == N:
                    u = 0
                elif k == 0:
                    u = 0
                else:
                    u = vetor[k-1, i]+dt*(((vetor[k-1, i-1]-2*vetor[k-1, i]+vetor[k-1, i+1])/dx**2) + r)
                vetor[k, i] = u
                #Novo vetor (Necessario para plotar com variacao de 0,1 em 0,1 de t)
                if tk == 0.0 or tk == 0.1 or tk == 0.2 or tk == 0.3 or tk == 0.4 or tk == 0.5 or tk == 0.6 or tk == 0.7 or tk == 0.8 or tk == 0.9 or tk == 1.0:
                    vetor_grafico[i, l] = u
                    if i == N:
                        l = l + 1
                i = i + 1
            j = j + 1
            k = k + 1

        #Plotagem dos dados
        plt.suptitle("Item: 1.c) - Gráfico da Solução Encontrada x t")
        plt.title("N: " +str(N)+ " e λ: " +str(lambida))
        plt.xlabel("Posição")
        plt.ylabel("y - Solução (u)")
        linha = np.linspace(0, 1, N+1)
        plt.plot(linha, vetor_grafico[0:N+1, 0], label="t : 0.0")
        plt.plot(linha, vetor_grafico[0:N+1, 1], label="t : 0.1")
        plt.plot(linha, vetor_grafico[0:N+1, 2], label="t : 0.2")
        plt.plot(linha, vetor_grafico[0:N+1, 3], label="t : 0.3")
        plt.plot(linha, vetor_grafico[0:N+1, 4], label="t : 0.4")
        plt.plot(linha, vetor_grafico[0:N+1, 5], label="t : 0.5")
        plt.plot(linha, vetor_grafico[0:N+1, 6], label="t : 0.6")
        plt.plot(linha, vetor_grafico[0:N+1, 7], label="t : 0.7")
        plt.plot(linha, vetor_grafico[0:N+1, 8], label="t : 0.8")
        plt.plot(linha, vetor_grafico[0:N+1, 9], label="t : 0.9")
        plt.plot(linha, vetor_grafico[0:N+1, 10], label="t : 1.0")
        plt.legend()
        plt.grid()
        plt.show()

if exer == 2:
    if item == "a" or item == "A":
        print()
        print("Você escolheu a Tarefa 2, item A, para realização correta desta, lhe será pedido: ")
        print ()
        print ("Um valor de N, representado a dimensão do problema")
        print("Valores do vetor que representa a Diagonal da matriz A (COM N-1 ELEMENTOS)")
        print("Valores do vetor que representa a Subdiagonal da matriz A (COM N-2 ELEMENTOS)")
        print("Valores do vetor que representa o lado -B- direito da igualdade (COM N-1 ELEMENTOS)")
        print()
        print("E ao final, lhe será exibido:")
        print()
        print("O vetor L, resultado da Fatoração LDLt")
        print("O vetor D, resultado da Fatoração LDLt")
        print("A solução computada -X-")
        print()
        print("Preparado? - VAMOSSS")
        print()
        N = int(input("Entre com o valor de N: "))

        #Criacao do vetor Diagonal de A
        print()
        print ("-Composição do vetor que representa a Diagonal da Matriz A-")
        print()
        i = 0
        AD = []
        while i <= N-2:
            v = float(input("Digite o elemento do vetor que representa a Diagonal de A: "))
            AD.append(v)
            i = i + 1
            
        #Criacao do vetor subdiagonal da matriz A
        print()
        print ("-Composição do vetor que representa a Subdiagonal da Matriz A-")
        print()
        i = 0
        SD = []
        while i <= N-3:
            v = float(input("Digite o elemento do vetor que representa a Subdiagonal de A: "))
            SD.append(v)
            i = i + 1

        #Criacao do vetor que representara B
        print()
        print ("-Composição do vetor que representa o lado direito -B- da igualdade")
        print()
        i = 0
        B = []
        while i <= N-2:
            v = float(input("Digite o elemento do vetor que representa o lado direito -B- da Igualdade: "))
            B.append(v)
            i = i + 1

        #Criacao do shape da matriz "A", para o processo de fatoração LDLt
        L1 = np.diagflat(AD)
        L2 = np.diagflat(SD, k=1)
        L3 = np.diagflat(SD, k=-1)
        A = L1+L2+L3

        #Criacao do shape das matrizes L e D
        L = np.zeros((N-1, N-1))
        D = np.zeros((N-1, 1))

        #Decomposicao LDLt
        a = 0
        b = 0
        c = 0
        d = 0
        for i in range(N-1):
            for j in range(i):
                a = (L[i][j])**2*D[j]
                b = a + b
            D[i] = A[i][i] - b
            b = 0 
            for j in range(i, N-1):
                for k in range(i):
                    c = L[j][k]*L[i][k]*D[k]
                    d = c + d 
                L[j][i] = (A[j][i]-d)/D[i]
                d = 0
        L_T1 = L[np.where(L!=0)]
        L_T = L_T1[np.where(L_T1!=1)]

        #Transposiçao de D
        D_F = np.zeros((N-1))
        i = 0
        while i <= N-2:
            v = D[i][0]
            D_F[i] = v
            i = i + 1

        # Achar primeira variavel intermediaria "Y" para resolucao do sistema
        Y = []
        i = 0
        while i <= N-2:
            if i == 0:
                Y.append(B[i])
                i = i + 1
            else:
                Y.append(B[i] - L_T[i-1]*Y[i-1])
                i = i + 1

        # Achar segunda variavel intermediaria "Z" para resolucao do sistema
        Z = []
        i = 0 
        while i <= N-2:
            v = Y[i]/D_F[i]
            Z.append(v)
            i = i + 1

        # Achar a variavel final "X" para resolucao do sistema
        X = np.zeros((N-1))
        j = 0
        i = 0
        while i <= N-2:
            if i == 0:
                X[N-2] = Z[N-2]
                i = i + 1
            else:
                w = Z[N-2-i] - X[N-2-j]*L_T[N-2-i]
                X[N-2-i] = w
                i = i + 1
                j = j + 1
        print()
        print("Vetor L = ", L_T)
        print()
        print("Vetor D = ", D_F)
        print()
        print("Vetor solução X = ", X)
        print()
    elif item == "b" or item == "B":
        escolha = str(input("Escolha o item da Tarefa 1 ((a), (b) ou (c)) que deseja simular via Euler Implícito: "))
        if escolha == "a":
            print()
            print("##### Você escolheu a Tarefa 2, item b, Euler Implícito - Função 1.a) #####")
            print()
            print("########## Item ainda não realizado ##########")
            print()
        elif escolha == "b" or escolha == "B":
            print()
            print("##### Você escolheu a Tarefa 2, item b, Euler Implícito - Função 1.b) #####")
            print()
            print("########## Item ainda não realizado ##########")
            print() 
        elif escolha == "c" or escolha == "C":
            print()
            print("##### Você escolheu a Tarefa 2, item b, Euler Implícito - Função 1.c) #####")
            print()
            print("########## Item ainda não realizado ##########")
            print() 
    elif item == "c" or item == "C":
        escolha = str(input("Escolha o item da Tarefa 1 ((a), (b) ou (c)) que deseja simular via Crank-Nicolson: "))
        if escolha == "a" or escolha == "A":
            print()
            print("##### Você escolheu a Tarefa 2, item c, Cranck-Nicolson - Função 1.a)#####")
            print()
            print("########## Item ainda não realizado ##########")
            print()
        elif escolha == "b" or escolha == "B":
            print()
            print("##### Você escolheu a Tarefa 2, item c, Cranck-Nicolson - Função 1.b) #####")
            print()
            print("########## Item ainda não realizado ##########")
            print()
        elif escolha == "c" or escolha == "C":
            print()
            print("##### Você escolheu a Tarefa 2, item c, Cranck-Nicolson - Função 1.c) #####")
            print()
            print("########## Item ainda não realizado ##########")
            print()
