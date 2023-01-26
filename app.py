import json, climage
from tqdm import tqdm
from time import sleep
import os
clear = lambda: os.system('cls')


with open("dados.json", encoding='utf-8') as meu_json1:
    perguntas = json.load(meu_json1)
with open("animals.json", encoding='utf-8') as meu_json2:
    animals = json.load(meu_json2)


Respostas = ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]

# -------  Início --------
clear()
print("TESTE DE PERSONALIDADE")
print()
print("Instruções")
print()
print(" - Para colocar as respostas, digite apenas A, B, C, D ou E;")
print(" - Caso queira voltar a questão para atualizar sua resposta, digite V")
print(" - Caso queira avançar digite N")
print(" - Após escolher a opção, clicar enter para enviar")
print()
sleep(2)
print("         Para começar aperte enter       ")
input()

pbar = tqdm(range(20))

def question(num_prgt):
    clear()
    """ Function to show the questions """

    pbar.n = num_prgt
    pbar.refresh()
    sleep(0.1)

    print()
    print(perguntas[num_prgt]["pergunta"])
    print()
    print(perguntas[num_prgt]['a'][0])
    print(perguntas[num_prgt]['b'][0])
    print(perguntas[num_prgt]['c'][0])
    print(perguntas[num_prgt]['d'][0])
    print(perguntas[num_prgt]['e'][0])
    print()

    escolha = input("Qual sua escolha? ").lower()

    while escolha not in 'abcdevn':
        print("Digite somente as opções disponibilizadas")
        escolha = input("Qual sua escolha? ").lower().strip()

    if escolha == "v":
        if num_prgt == 0:
            print("Não é possível voltar, não existe questão 0 :)")
            sleep(4)
            return num_prgt
        else:
            num_prgt -= 1
            return num_prgt
    elif escolha == "n":
        if Respostas[num_prgt] == "#":
            print("Para avançar, é necessário primeiramente responder essa pergunta")
            sleep(3)
            return num_prgt
        else:
            num_prgt += 1
            return num_prgt
    elif Respostas[num_prgt] != "":
        Respostas[num_prgt] = perguntas[num_prgt][escolha][1]
        print(Respostas[num_prgt])
        num_prgt += 1


    return num_prgt

def cont_animal(answers):
    """ Função que conta e retorno o animal definido"""

    coruja = [answers.count("Coruja"), "coruja"]
    leao = [answers.count("Leão"), "leão"]
    panda = [answers.count("Panda"), "panda"]
    tigre = [answers.count("Tigre"), "tigre"]
    tubarao = [answers.count("Tubarão"), "tubarão"]

    maior = max(coruja, leao, panda, tigre, tubarao)

    return maior[1]

i = 0

while i <= len(perguntas)-1:
    i = question(i)

def show_animal(animal):
    """ Função que mostra o animal resultado"""
    clear()
    print("Carregando...")
    sleep(1)
    clear()
    print('Seu animal é: ', animal.upper())
    print()
    output = climage.convert(f'{animals[animal]["local"]}', is_unicode= True, is_256color = True)
    print(output)
    print()
    print(animals[animal]["frase"])

show_animal(cont_animal(Respostas))
input()
clear()