##################################


#EP2 - MAP 3121 - Métodos Numéricos e suas Aplicações


#Vitor Tiveron de Almeida Santos - 9868085
#Vincius Bueno de Moraes - 10256432



##################################

import numpy as np
import matplotlib.pyplot as plt
import math
import random as random


######## tarefa A ###########
#decomposição para Crank 
def LDL_1(d, subd): 
    
    n = d.size
    D = np.zeros(n)
    L = np.zeros(n-1)

    D[0] = d[0]
    for i in range(n):
        
        if(i>0):
            D[i] = d[i]-(D[i-1])*((L[i-1])**2)

        if(i<n-1):
            L[i] = subd[i]/D[i]

    return [D,L]     

#solução para Crank
def solucao_1(D, L, b):  
   
    n = D.size 
    x = np.zeros(n)
    y = np.zeros(n)
    z = np.zeros(n)

    for i in range(y.size):
        if(i == 0):
            y[i] = b[i]
        else:
            y[i] = b[i]-(L[i-1])*(y[i-1])

    for j in range(z.size):
        z[j] = y[j]/D[j]

    for k in range (x.size-1, -1, -1):
        if(k == x.size-1):
            x[k] = z[k]
        else:
            x[k] = z[k]-(L[k])*(x[k+1])
   
    #solução
    return x 

#realiza Crank - caso em que M = N
def Crank(M, N, lam, p,nf): 
    
    M=N
    c = 1/N
    b = np.zeros(N-1)
    u = np.zeros((N+1, N+1))
    d = np.full(N-1, 1+lam)       
    subd = np.full(N-2, (-1/2)*lam)

    [D,L] = LDL_1(d, subd)      

    for k in range (N):
    
        for i in range(N-1):
            if (i == 0):
                b[i] = u[k][i+1] + (N/2)*(0 + 0 + u[k][i+2] -2*u[k][i+1]) + (c/2)*(F((k*c),(i+1)*c, p, c) + F((k+1)*c,(i+1)*c, p, c))

            elif (i == N-2):
                b[i] = u[k][i+1] + (N/2)*(0 + 0 + u[k][i] -2*u[k][i+1]) + (c/2)*(F((k*c),(i+1)*c, p, c) + F((k+1)*c,(i+1)*c, p, c))

            else:
                b[i] = u[k][i+1] + (N/2)*(u[k][i] + u[k][i+2] -2*u[k][i+1]) + (c/2)*(F((k*c),(i+1)*c, p, c) + F((k+1)*c,(i+1)*c, p, c))

        u[k+1, 1:N] = solucao_1(D,L,b)  
    
    return u[N]



########### tarefa B ###########
#dados vetores Ut e u, monta a matriz dos prod. int. A e o vetor de prod. int. b do sistema Ax=b, onde x são os coeficientes buscados
def tarefa_b(nf, u, Ut, teste): 
  
    #dependendo do teste, o vetor Ut é armazenado de maneira diferente. Por isso, há blocos condicionais para cada teste
    
    #A: vetores unitários
    #B: u[nf][N], Ut[0][N]
    #C e D: u[nf][N], Ut[N][0]

    A = np.zeros((nf,nf))
    b = np.zeros(nf)


    if(teste=="A"):
        for i in range(nf):
            b[i]=np.dot(u,Ut)                     #como tanto a matriz como o vetor serão 1x1 , pode-se escolher qualquer método nesse caso para o produto interno
            for j in range(nf):
                A[i][j] =A[i][j]+np.dot(u,u) 

    elif(teste=="B"):
        for i in range(nf):
            soma = 0
            for j in range(u[i].size):
                soma = soma +u[i][j]*Ut[0][j] #<- itera-se a 2ª
            b[i] = soma
            
            for j in range(nf):
                soma2 = 0
                for k in range(u[i].size):
                    soma2+=u[i][k]*u[j][k]
                A[i][j] = soma2        
    
    else:
        for i in range(nf):
            soma = 0
            for j in range(u[i].size):
               soma = soma +u[i][j]*Ut[j][0]  #<- itera-se a 1ª
            b[i] = soma

            for j in range(nf):
                soma2 = 0
                for k in range(u[j].size):
                    soma2 = soma2 +u[i][k]*u[j][k]   
                A[i][j] = soma2
    

    #print(A)
    #print("vetor b: \n", b)
    return [A,b]



########### tarefa C ###########
# - decompõe matriz de produtos internos em uma matriz diagonal D e uma matriz triangular inferior L  
def LDL_2(A,b):

    n=b.size

    #diagonal
    D = np.zeros((n,n))


    #matriz L triangular inferior
    L = np.zeros((n,n))

    for i in range(n): 
        L[i][i]= 1
        
        for j in range(i,n):
            soma_low = 0
            for k in range(j):
                soma_low += D[k][k]*L[j][k]*L[j][k]

            if(i==j):    
                D[i][j] =A[i][j]- soma_low
    
            soma_sup = 0

            for k in range(0,i):
                soma_sup += L[j][k]*L[i][k]*D[k][k]
            L[j][i] = (A[i][j]-soma_sup)/D[i][i]

    return [L,D]

# - resolve o sistema (LDL^t)*x = b para obter o vetor de intensidades  
def solucao_2(L, D, b):

    n = b.size

    #vetor solução x
    x = np.zeros(n)

    
    #somas auxiliares utilizadas durante o método
    soma_y = 0
    soma_z = 0

 
   
    #y utilizada em Ly = b
    y = np.zeros(n)

    #z para Dz = y
    z =np.zeros(n)

    #resolvendo Ly = b
    y[0] = b[0]

    for i in range(1,n):
        soma_y = 0
        for j in range(0,n):
            soma_y =soma_y+L[i][j]*y[j]
        y[i]=b[i] -soma_y


    for i in range(0,n):
        z[i]= y[i]/D[i][i]
     
    #agora L'x = z
    x[n-1] = z[n-1]

    for i in range(n-2,-1,-1):
        soma_z = 0
        for j in range(i+1,n):
            soma_z =soma_z+L[j][i]*x[j]
        x[i]=z[i]-soma_z
    
    #devolve vetor solução x
    return x
  



#calcula a função utilizada durante o método de Crank-Nicolson
def F(t,x, p, dx):  
    
    if(p-dx/2.0<=x and x<=p+dx/2.0):
        gh = (1.0/dx)
    else:
        gh =  0.0
           
            #função r(t)*gh(t)
    return 10.0*(1.0+math.cos(5*t))*gh


#lê o arquivo e devolve-o dentro de um vetor ordenado - utilizada para testes C e D
def leitura(filename): 
    f = open(filename,"r")
    return [list(map(float, line.strip().split())) for line in f]

#calcula o erro quadrático de acordo com a fórmula fornecida
#teste entra aqui apenas para plotar gráficos
#caso deseje ver os gráficos, favor descomentar a linha que contém a chamada a função de plotagem ("plota")
def erro(u,Ut,a,N,nf, teste): 

    soma = 0
    sub = 0
    
    for i in range(nf):
        soma = soma + a[i]*u[i]

  
    for i in range(N):
        sub = sub + (Ut[i][0]-soma[i])**2

    dx = 1/N
    erro = math.sqrt((1/N)*sub)
#########################################################################################################################
    #plota(soma,Ut,dx, N, teste, erro) 

    return erro




#roda o teste A
def testeA(teste):
    
    #parâmetros para o teste A

        N = 128
        dx = float(1.0/N)
        lam = round(dx/dx**2, 2)
        nf = 1
        p = 0.35
        
        u = Crank(N,N,lam,p,nf)
        Ut = 7*u
        print("teste selecionado: teste "+teste)
        [A,b] = tarefa_b(nf,u,Ut, teste)
        
        print("vetor solução: ")

        [L,D] = LDL_2(A,b)

        print(solucao_2(L,D,b))

#roda o teste B
def testeB(teste): 
    
    print("teste selecionado: teste "+teste)

    #parâmetros para teste B
    us = [] #vetor de u's
    Uts=[] #vetor de Ut's
    N = 128
    nf=4
    dx = float(1.0/N)  
    lam = round(dx/dx**2, 2)
    

    #calcula o vetor u através do método de Crank para cada p e seu respectivo Ut
    for i in range(4):

        if (i==0):
            p = 0.15
            u = Crank(N,N,lam,p,nf)
            Ut = 2.3*u
            us.append(u)
  
        if(i==1):
            p=0.3
            u = Crank(N,N,lam,p,nf)
            Ut += 3.2*u
            us.append(u)

        if(i==2):
            p=0.7
            u = Crank(N,N,lam,p,nf)
            Ut += 0.5*u
            us.append(u)
  
        if(i==3):
            p=0.8
            u= Crank(N,N,lam,p,nf)
            Ut += 4.2*u
            us.append(u)
            Uts.append(Ut)


    [A,b] = tarefa_b(nf,us,Uts,teste)   
    [L,D] = LDL_2(A,b)

    solve = solucao_2(L,D,b)

    for i in range (len(solve)):
        print("intensidade a"+str(i)+":" + '{0:.5f}'.format(solve[i]))
    
#roda os testes C e D          
def testeCD(teste):
        #caso o nome do arquivo tenha sido modificado, favor editar aqui #################################################
        filename = "arquivo_teste_ep2.txt"

        us=[] #vetor de u's
        Uts=[] #vetor de Ut's
        N = 1
        
        nf = 10
        data = leitura(filename)
        print("teste selecionado: teste "+ teste)
        print("por favor, selecione o número correspondente ao N que será utilizado na execução do teste:")
        print("1 -> N = 128")
        print("2 -> N = 256")
        print("3 -> N = 512")
        print("4 -> N = 1024")
        print("5 -> N = 2048")
        ene = int(input())
        if(ene == 1):
            N = 128
        elif(ene == 2):
            N = 256
        elif(ene == 3):
            N = 512
        elif(ene ==4):
            N = 1024
        elif(ene == 5):
            N = 2048
        else:
            print("Entrada incorreta. Encerrando programa.")
            return 0
        
        print("rodando teste "+teste+ " para N = "+ str(N))

        dx = float(1.0/N)
        lam = round(dx/dx**2,2)
        #data[0] contém o vetor de p's
        for i in range(len(data[0])):
            u = Crank(N,N,lam,data[0][i],nf)
            us.append(u)

        for i in range(1,len(data),int(2048/N)): #roda de 1 a 2048/N-1 -> não pega os pontos de borda
                Uts.append(data[i])
        
        #multiplica cada valor do vetor Uts por um número aleatório entre -1 e 1 - teste D
        if(teste == "D"):
            for i in range(len(Uts)):
                rand = random.random()
                aleatorio = 1+(rand- 0.5)*2*0.01
                Uts[i][0] = aleatorio*Uts[i][0]
            

        [A,b] = tarefa_b(nf,us,Uts,teste)
        [L,D] = LDL_2(A,b)

        solve = solucao_2(L,D,b)
        for i in range (len(solve)):
            print("intensidade a"+str(i)+":  "+ '{0:.16f}'.format(solve[i]))
        print("O erro quadrático calculado é igual a ", erro(us,Uts,solve,N,nf, teste))


#Função que plota o resultado calculado e a resposta exata, para item C e D
def plota(soma, Ut, dx, N, teste, erro): 
    plt.axis([0,1,0,25])
    plt.plot(np.arange(0,1+dx,dx),soma, linewidth = 2)
    plt.plot(np.arange(0,1+dx,dx),Ut, linestyle = "dashed", color = "red", linewidth = 2)
    plt.ylabel("Temperatura")
    plt.xlabel("posição")

    plt.suptitle("Gráfico para N = "+str(N)+", teste "+teste+" e erro = "+str(erro))
    plt.show()

def main():
    print("\n\n\nBem Vindo ao Exercício Programa 2!\n")
    print("Dupla: \nVitor Tiveron de Almeida Santos - 9868085\nVincius Bueno de Moraes - 10256432\n")
    print("Por favor, digite número correspondente ao teste a ser executado:\n")
    print("\n 1 - Teste A\n 2 - Teste B\n 3 - Teste C\n 4 - Teste D")
    t = int(input())
    if(t == 1):
        teste = "A"
        testeA(teste)
    elif(t == 2):
        teste = "B"
        testeB(teste)
    elif(t == 3):
        teste = "C"
        testeCD(teste)
    elif(t==4):
        teste = "D"
        testeCD(teste)
    else:
        print("Entrada inválida. Por favor, tente novamente.")
        return 0

if __name__ == "__main__":
    main()
    
