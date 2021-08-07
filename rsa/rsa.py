# Nome: Leon Tenório da Silva
# T12 - Exercício 5 RSA

def tabela_converter(letra):
    ascii = ord(letra)
    if(ascii >= 65 and ascii <= 90):
        return ascii - 55  # tabela comeca em 10
    if(ascii == 32):
        return 99
    return -1


def tabela_reverter(codigo):
    if(codigo == 99):
        return " ", None
    elif(codigo+55 >= 65 and codigo+55 <= 90):
        return chr(codigo+55), None
    return 'X', codigo


def criptografia(frase, chave_b, chave_m):
    criptografado = []
    for letra in frase:
        conversao = tabela_converter(letra)
        cripto = (conversao**chave_b) % chave_m
        criptografado.append(cripto)
    return criptografado


def decriptografia(mensagem, chave_a, chave_m, tabela=tabela_reverter, condicao_horario=None, conversao_horario=None):
    descriptografado = []
    falta = []
    codigo_horario = None
    for codigo in mensagem:
        if(codigo_horario != None):
            print(codigo)
            codigo_horario.append(codigo)
        else:
            decripto = (codigo**chave_a) % chave_m
            letra, falta_conversao = tabela(decripto)
            descriptografado.append(letra)
            if(falta_conversao != None):
                falta.append(codigo)
                descriptografado.pop()
            if(condicao_horario != None and condicao_horario(descriptografado) and conversao_horario != None):
                codigo_horario = []
    if(codigo_horario != None):
        list = conversao_horario(codigo_horario)
        for x in list:
            descriptografado.append(x)
    return descriptografado, falta


def padrao_horario(descriptografando):
    comparar = "AS "
    if(len(descriptografando) > len(comparar)):
        horario = True
        for i in range(len(comparar)):
            if(comparar[(-1)*i] != descriptografando[(-1)*i]):
                horario = False
        return horario
    return False


def conversao_horario(codigo):
    numero = int("-".join(str(x) for x in codigo))
    return [str(numero % 24)]


def mostrar_criptografia(lista_dados):
    return "-".join(str(x) for x in lista_dados)


def mostrar_descriptografia(lista_dados):
    texto = "".join(lista_dados)
    return texto


chave_m = 247
chave_b = 173
chave_a = 5

frase = "TINIA"
print('Atividade 1: Criptografar "' + frase+'"')
criptografado = criptografia(frase, chave_b, chave_m)
print("Saída: "+mostrar_criptografia(criptografado))

mensagem = [147, 9, 140, 18, 147, 73, 207, 215, 140,
            214, 215, 140, 73, 122, 222, 225, 23, 147, 29]
print('\nAtividade 2: Descriptografar "' + mostrar_criptografia(mensagem)+'"')
descriptografado, falta_conversao = decriptografia(
    mensagem, chave_a, chave_m)
print("Saída: "+mostrar_descriptografia(descriptografado))
print('Enviado no dia '+str(2630 % 30)+' às '+str(1431 % 24))


def tabela_sequia(codigo):
    if(codigo == 11):
        return " ", None
    elif(codigo >= 65 and codigo <= 90):
        return chr(codigo), None
    return 'X', codigo


chave_m_sequia = 253
chave_a_sequia = 7

mensagem = [175, 134, 175, 89, 175, 48, 176, 134, 176, 243, 228, 176,
            185, 101, 243, 223, 241, 176, 206, 228, 176, 212, 115, 48, 175, 228]
print('\nAtividade 3: Descriptografar "' + mostrar_criptografia(mensagem)+'"')
descriptografado, falta_conversao = decriptografia(
    mensagem, chave_a_sequia, chave_m_sequia, tabela=tabela_sequia)
print("Saída: "+mostrar_descriptografia(descriptografado))

mensagem = [147, 29, 147, 225, 23, 147, 73, 147, 214, 73, 3033]
print('\nAtividade 4: Descriptografar "' + mostrar_criptografia(mensagem)+'"')
descriptografado, falta_conversao = decriptografia(
    mensagem, chave_a, chave_m, condicao_horario=padrao_horario, conversao_horario=conversao_horario)
print("Saída: "+mostrar_descriptografia(descriptografado))
