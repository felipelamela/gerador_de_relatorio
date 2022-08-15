def conversao(valor: int) -> int:
    valor /= 1048576
    return valor


def porcentagem(valor: int, total: int) -> int:
    numero = (100*float(valor))/total
    return f'{numero:.2f}'


total = 0
tamanho_medio = 0
usuario = []
tamanho = []
porcent = []

with open('./usuario.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.split()
        usuario.append(linha[:][0])
        numero = int(linha[:][1])
        tamanho.append(conversao(numero))
        total += conversao(numero)
    for numero in tamanho:
        porcent.append(f'{porcentagem(numero,total)} %'.replace('.', ','))
arquivo.close()
tamanho_medio = total/len(usuario)

with open('./relatorio.txt', 'w') as arquivo:
    arquivo.writelines(
        f"{f'ACNE Inc.':<30} Uso do espaço em disco pelos usuários\n")
    arquivo.writelines('-'*70)
    arquivo.writelines('\n')
    arquivo.writelines(
        f"{f'Nr.':<5}{f'Usuário':<20}{f'Espaço utilizado':<35}{f'% do uso'}\n")
    for n in range(len(usuario)):
        arquivo.writelines(
            f"{n:<5}{usuario[n]:<25}{f'{tamanho[n]:9.2f} MB':<35}{porcent[n]}\n")
    arquivo.writelines(f"Espaço total ocupado: {total:.2f} MB\n")
    arquivo.writelines(f'Espaço médio ocupado: {tamanho_medio:.2f}MB\n')
arquivo.close()
