# Rafael Cabral   - 84757
# Valter Martinho - 57425

# Construtor:

def cria_coordenada(l,c):
    '''cria_coordenada : int x int -> coordenada
       cria_coordenada(l,c) cria uma coordenada correspondente ao par
       (l,c). '''
    if isinstance(l,int) and isinstance(c,int) and l >= 1 and c >= 1:
        return(l,c)
    else:
        raise ValueError ('cria_coordenada: argumentos invalidos')

# -- Fim: cria_coordenada -- #

# Selectores:

def coordenada_linha(c):
    ''' coordenada_linha : coordenada -> int
        coordenada_linha(c) devolve linha correspondente a coordenada c. '''
    
    return c[0]

# -- Fim_ coordenada_linha -- #

def coordenada_coluna(c):
    ''' coordenada_coluna : coordenada -> int
        coordenada _coluna(c) devolve a coluna correspondente a coordenada
        c.'''
    
    return c[1]

# -- Fim: coordenada_coluna -- #

# Reconhecedor

def e_coordenada(coord_verif):
    ''' e_coordenada : universal -> bool
        e_coordenada(coord_verif) devolve True caso coord_verif seja do tipo 
        coordenada e False em caso contrario.'''
    
    # Para um argumento ser considerado coordenada tem de ser um tuplo com dois 
    # elementos (l,c) e esses elementos tem de ser numeros inteiros
    # maiores ou iguais a 1
    
    return isinstance(coord_verif,tuple) and len(coord_verif) == 2 and isinstance(coord_verif[0],int) and isinstance(coord_verif[1],int) and coord_verif[0] >= 1 and coord_verif[1] >= 1

# -- Fim: e_coordenada -- #

#Teste

def coordenadas_iguais(coord1,coord2):
    '''Funcao coordenadas_iguais: tuple x tuple -> bool
       Recebe como argumentos dois elementos do tipo coordenada.
       Devolve True caso esses elementos a mesma posicao (l,c)
       do tabuleiro e False caso contrario.'''
    
    return coordenada_linha(coord1) == coordenada_linha(coord2)\
           and coordenada_coluna(coord1) == coordenada_coluna(coord2)

# -- Fim: coordenadas_iguais -- #

def coordenada_para_cadeia(coord1):
    '''Funcao coordenada_para_cadeia: tuple -> string
       Recebe como argumento um elemento do tipo coodenada.
       Devolve uma cadeia de caracteres que representa a coordenada'''
    
    return str(('('+str(coordenada_linha(coord1))+' : '+str(coordenada_coluna(coord1))+')'))


# -- Fim: coordenada_para_cadeia -- #

# ---- T.A.D. tabuleiro ---- #
# Um tabuleiro 

#Construtor

def cria_tabuleiro(t):
    ''' Funcao cria_tabuleiro: tuple -> tabuleiro 
        Recebe como argumento um elemento do tipo tuplo. 
        Devolve um elemento do tipo tabuleiro de acordo com a representacao
        interna escolhida'''
    l = {}
    l['EspL'] = t[0]
    l['EspC'] = t[1]
    
    if not (isinstance(t, tuple) and len(t) == 2 and isinstance(t[0], tuple) and isinstance(t[1], tuple) and len(t[0]) == len(t[1])):
        raise ValueError ('cria_tabuleiro: argumentos invalidos')
    for i in t:
        for j in i:
            if not isinstance(j, tuple):
                raise ValueError ('cria_tabuleiro: argumentos invalidos')
            for x in j:
                if not (isinstance(x,int) and x > 0):
                    raise ValueError ('cria_tabuleiro: argumentos invalidos')
    else:
        for i in range(len(t[0])):
            for j in range(len(t[1])):
                l[cria_coordenada(i+1,j+1)] = 0 
        return l

# -- Fim: cria_tabuleiro -- #
            
# Seletor

def tabuleiro_dimensoes(tab):
    '''Funcao tabuleiro_dimensoes: tabuleiro -> tuple
       Recebe como argumento um elemento do tipo tabuleiro.
       Devolve um elemento do tipo tuplo'''
    return (len(tab['EspL']), len(tab['EspC']))

# -- Fim: tabuleiro_dimensoes -- #

# Seletor 

def tabuleiro_especificacoes(tab):
    '''Funcao tabuleiro_especificacoes: tabuleiro -> tuple
       Recebe como argumento um elemento do tipo tabuleiro.
       Devolve um tuplo composto por dois tuplos de tuplos inteiros
       sendo o primeiro tuplo correspondente a especificacao das linhas e o 
       segundo a especificacao das colunas.'''
    return (tab['EspL'], tab['EspC'])

# -- Fim: tabuleiro_especificacoes -- #

# Seletor

def tabuleiro_celula(tab,coord):
    '''Funcao tabuleiro_celula: tabuleiro x coordenada -> int
       Recebe como argumentos um elemento do tipo tabuleiro e uma coordenada.
       Devolve um elemento do tipo inteiro entre 0 e 2, correspondente ao valor 
       contido na celula do tabuleiro referente a coordenada.
       Caso a celula correspondente a coordenadenada esteja vazia devolve o 
       valor 0, caso o corresponda a uma celula em branco devolve o valor 1 e 
       caso a celula esteja preenchida deve devolver o valor 2.'''
    dim = tabuleiro_dimensoes(tab)
    dimL = dim[0]
    dimC = dim[1]
    if not e_tabuleiro(tab):
        raise ValueError ('tabuleiro_celula: argumentos invalidos') 
    elif not e_coordenada(coord):
        raise ValueError ('tabuleiro_celula: argumentos invalidos')
    elif coord[0] > dimL or coord[1] > dimC:
        raise ValueError ('tabuleiro_celula: argumentos invalidos')     
    else:
        return tab[coord]
    
# Modificador

def tabuleiro_preenche_celula(tab,coord,jog):
    '''Funcao tabuleiro_preenche_celula: tabuleiro x coordenada x int -> tabuleiro
    Recebe como um argumentos um elemento do tipo tabuleiro um elemento c do tipo 
    coordenada e um inteiro entre 0 e 2.
    Modifica o tabuleiro t preenchendo a celula referente a coordenada c com o 
    elemento e, que pode ser 0, 1 ou 2, para representar vazio, uma celula em 
    branco ou uma caixa, respetivamente.
    Devolve o tabuleiro modificado.'''
    dim = tabuleiro_dimensoes(tab)
    dimL = dim[0]
    dimC = dim[1]    
    if not e_tabuleiro(tab):
        raise ValueError ('tabuleiro_preenche_celula: argumentos invalidos')
    elif not e_coordenada(coord):
        raise ValueError('tabuleiro_preenche_celula: argumentos invalidos')
    elif not (jog == 0 or jog == 1 or jog == 2):
        raise ValueError ('tabuleiro_preenche_celula: argumentos invalidos') 
    elif coord[0] > dimL or coord[1] > dimC:
        raise ValueError ('tabuleiro_preenche_celula: argumentos invalidos')        
    else:
        tab[coord] = jog
        return tab

# Reconhecedor

def e_tabuleiro(tab):
    '''Funcao e_tabuleiro: universal -> logico
       Recebe um unico argumento, devolvendo True se o seu 
       argumento for do tipo tabuleiro e falso em caso contrario'''
    if not(isinstance(tab, dict) and ('EspL' in tab) and ('EspC' in tab) and isinstance(tab['EspL'],tuple) and isinstance(tab['EspL'],tuple) and (len(tab['EspL']) == len(tab['EspC'])) and (len(tab['EspL'])) > 0 and len(tab['EspC']) > 0 and len(tab) == ((len(tab['EspC'])*len(tab['EspL'])) + 2)):
        return False
    else:
        return True
    
# Reconhecedor

def tabuleiro_celulas_vazias(tab):
    linhas = 0
    colunas = 0
    tam = tabuleiro_dimensoes(tab)
    tamL = tam[0] 
    tamC = tam[1]
    cont = 0
    for i in range(0,tamC):
        for j in range(0,tamL):
            if tabuleiro_celula(tab,cria_coordenada(i+1,j+1)) == 0:
                cont += 1
    return cont

def linha_completa(tupesp,listaesp):
    cont = []
    acc = 0
    for i in listaesp:
        if i == 2:
            cont[acc] = cont[acc] + 1  
        elif i == 1:
            if cont[acc] == tupesp[acc] and :
                acc += 1
        else:
            return False
            
    elif listaesp[i] == 1:
    else:
        return False
                    
            
    

def tabuleiro_completo(tab):
    '''Funcao tabuleiro completo: tabuleiro -> logico
       Recebe como argumento um elemento t  do tipo tabuleiro 
       Devolve True caso o tabuleiro t esteja totalmente preenchido corretamente 
       de acordo com as suas especificacoes, e Falso caso contrario'''
    linhas = 0
    colunas = 0
    tam = tabuleiro_dimensoes(tab)
    tamL = tam[0] 
    tamC = tam[1]
    for i in range(0,tamC):
        for j in range(0,tamL):
            acc = 0
            cont = 0
            esp = tabuleiro_especificacoes(tab)
            if tabuleiro_celula(tab,cria_coordenada(i+1,j+1)) == 2:
                cont += 1       
                if cont == esp[0][i][cont]:
                    acc += 1
                    if acc == len(esp[0][acc]):
                        linhas = True
            elif tabuleiro_celula(tab,cria_coordenada(i+1,j+1)) == 1:
    for i in range(0,tamC):
        for j in range(0,tamL):
            acc = 0
            cont = 0
            esp = tabuleiro_especificacoes(tab)
            if tabuleiro_celula(tab,cria_coordenada(j+1,i+1)) == 2:
                cont += 1       
                if cont == esp[0][i][cont]:
                    acc += 1
                    if acc == len(esp[0][acc]):
                        colunas = True
            elif tabuleiro_celula(tab,cria_coordenada(j+1,i+1)) == 1:
           
    return linhas and colunas
                        
                
# -- Funcao Auxiliar -- #        

def maior_esp_aux(fim):
    '''Funcao maior_esp_aux: tuple -> int
       Recebe um tuplo de tuplos 
       Devolve o maior tuplo '''
    maior = 0
    for i in range(len(fim)):
        if len(fim[i]) >= maior:
            maior = len(fim[i])
    return maior   

# -- Fim: maior_esp_aux -- #j

def escreve_tabuleiro(tab):
    '''Funcao escreve_tabuleiro: tabuleiro -> {}
       Recebe como argumento um elemento t do tipo tabuleiro e escreve para 
       o ecra a representacao externa de um tabuleiro de Picross'''
    if not e_tabuleiro(tab):
        raise ValueError ('escreve_tabuleiro: argumento invalido')
    lista = list(tabuleiro_especificacoes(tab))
    linhas = list(lista[0])
    colunas = list(lista[1])
    maiorL = maior_esp_aux(linhas)
    maiorC = maior_esp_aux(colunas)
    cont = 0
    for i in range((len(linhas)+maiorC)):
        if i > 0:
            print () 
        for j in range(len(colunas)):
            if (len(colunas[j]) == (maiorC - i) or len(colunas[j]) > (maiorC-i)) and i < maiorC:
                print(' ',colunas[j][(i-maiorC)], end='  ')
            elif i >= maiorC:
                if tabuleiro_celula(tab,cria_coordenada(((i+1)-maiorC),j+1)) == 0:
                    print('[ %s ]' % ('?'),sep= '',end='')
                elif tabuleiro_celula(tab,cria_coordenada(((i+1)-maiorC),j+1)) == 1:
                    print('[ %s ]' % ('.'),sep= '',end='')
                else:
                    print('[ %s ]' % ('x'),sep= '',end='')
                    
            else: 
                print('  ', end= '   ')
        if i >= maiorC:
            indice = 0
            espaco = '  '
            fimL = linhas[cont]
            while indice < len(fimL):
                print(' ',fimL[indice], sep='', end='')
                indice += 1
            if maior_esp_aux(linhas) > len(linhas[cont]) :
                print (espaco*(maior_esp_aux(linhas)-len(linhas[cont])), end='')
            print('|', end='')
            cont += 1
        else:
            print('  ', end = '')
    print('\n')
    
# -- Fim: escreve_tabuleiro -- #

# Teste

def tabuleiros_iguais(tab1,tab2):
    ''' Funcao tabuleiros_iguais: tabuleiro x tabuleiro -> logico
        Recebe como argumentos dois elementos tab1, tab2 do tipo tabuleiro
        Devolve True caso t1 e t2 correspondam a dois tabuleiros com as mesmas especificacoes e quadros com o mesmo conteudo, e False em caso contrario'''
    if e_tabuleiro(tab1) and e_tabuleiro(tab2):
        for i in tab1:
            if tab1[i] != tab2[i]:
                return False
        return True
    
# -- Fim: tabuleiros_iguais -- #

#-############################################################################

# Construtor

def cria_jogada(c, j):
    '''Funcao cria_jogada: coordenada x int -> jogada
       Recebe como argumentos um elemento do tipo tabuleiro e um inteiro 1 ou 2.
       Devolve uma jogada'''
    if not(e_coordenada(c)):
        raise ValueError ('cria_jogada: argumentos invalidos')
    elif not (j == 1 or j== 2):
        raise ValueError ('cria_jogada: argumentos invalidos')
    else:
        return (c,j)
    
# -- Fim: cria_jogada -- #
    
# Seletor
    
def jogada_coordenada(jog):
    '''Funcao jogada_coordenada: jogada -> coordenada
       Recebe como argumento um elemento do tipo jogada.
       Devolve a coordenada respetiva.'''
    if not e_jogada(jog):
        raise ValueError ('jogada_coordenada: argumentos invalidos')
    else:
        return jog[0]
    
# -- Fim: jogada_coordenada -- #
    
# Seletor

def jogada_valor(jog):
    '''Funcao jogada_valor: jogada -> coordenada
       Recebe como argumento um elemento do tipo jogada.
       Devolve a coordenada respetiva.'''
    if not e_jogada(jog):
        raise ValueError ('jogada_valor: argumentos invalidos')
    else:
        return jog[1]
    
# -- Fim: jogada_valor -- #
    
# Reconhecedor
    
def e_jogada(jog):
    ''' Funcao e_jogada: universal -> logico
        Recebe como argumento um elemento do tipo jogada.
        Devolve a coordenada respetiva. '''
    return e_coordenada(jog[0]) and (jog[1] == 1 or jog[1] == 2)

# -- Fim: e_jogada -- #

# Teste

def jogadas_iguais(jog1, jog2):
    ''' Funcao jogadas_iguais: jogada x jogada -> logico 
        Recebe como argumentos dois elementos do tipo jogada.
        Devolve True caso esses argumentos correspondam a mesma jogada, e False caso contrario. '''
    if not(e_jogada(jog1) and e_jogada(jog2)):
        raise ValueError ('jogadas_iguais: argumentos invalidos')
    return jog1 == jog2

# -- Fim: jogadas_iguais -- #

def jogada_para_cadeia(jog):
    '''Funcao jogada_para_cadeia: jogada -> cad. caracteres
       Recebe como argumento um elemento do tipo jogada.
       Devolve uma cadeia de caracteres. '''
    return str('('+str(coordenada_linha(jogada_coordenada(jog)))+' : '+\
           str(coordenada_coluna(jogada_coordenada(jog)))+')'+' --> '+str(jogada_valor(jog)))

# -- Fim: jogada_para_cadeia -- #

# -- Funcoes Adicionais -- #

def le_tabuleiro(fich):
    '''Funcao le_tabuleiro: cad. caracteres -> tuplo
       Recebe uma cadeia de caracteres que corresponde ao nome do ficheiro com os dados de especificacao do jogo.
       Devolve um tuplo com dois tuplos com as especificacoes das linhas e colunas. '''
    le = open(fich,'r')
    lelinha = le.readline()
    le.close()
    return eval(lelinha)

#pede_jogada

def pede_jogada(tab):
    ''' Funcao pede_jogada: tabuleiro do jogo -> cria_jogada(c,j)
        Recebe o tabuleiro do jogo como argumento e devolve a jogada que o jogador pretende executar.'''
    dim = tabuleiro_dimensoes(tab)
    if e_tabuleiro(tab):
        print('Introduza a jogada')
        jog = input('- coordenada entre (1 : 1) e ('+str(dim[0])+' : '+str(dim[1])+') >> ')
        val = eval(input('- valor >> '))
        jog1 = jog.replace(':',',')
        jog2 = eval(jog1)
        if e_coordenada(jog2) and jog2[0] <= dim[0] and jog2[1] <= dim[1]:
            return cria_jogada(jog2, val)
        else:
            return False 
        
def jogo_picross(fich):
    jogo = cria_tabuleiro(le_tabuleiro(fich))
    jogada = pede_jogada(jogo)
    coord = jogada_coordenada(jogada)
    valor = jogada_valor(jogada)
    tabseg = tabuleiro_preenche_celula(jogo,coord,valor)
    escreve_tabuleiro(tabseg)
    while not tabuleiro_completo(tabseg):
        jogada = pede_jogada(tabseg)
        coord = jogada_coordenada(jogada)
        valor = jogada_valor(jogada)
        tabseg = tabuleiro_preenche_celula(tabseg,coord,valor)
        escreve_tabuleiro(tabseg)
        if tabuleiro_celulas_vazias(tabseg):
            return True
        else:
            continue        
    