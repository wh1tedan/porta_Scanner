import os
import socket


# Função do scanner de portas
def port_Scanner():  
    prIp = input('Informe seu ip: ')
    prtfn = int(input('Informe sua porta inicial: '))
    prtfn2 = int(input('Informe sua porta final: '))

    for prtfn in range(prtfn, prtfn2 + 1):
        print('As portas disponiveis são ' , prtfn + prtfn2)
 
port_Scanner()


# Função que faz o teste em uma porta específica
def Scan_import(prIp, prtfn):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket TCP
    s.settimeout(5)
    print('Essa analise consta', prIp , prtfn)
    try:
        s.connect((prIp, prtfn))    # Tenta conexão na porta
        print('A porta está aberta', prtfn)
    except:
        print('A porta está fechada ')
    finally:
        s.close()  # Fecha o socket após o teste


