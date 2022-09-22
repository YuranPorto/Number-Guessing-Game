import random


def main():
    print("Para inciar o jogo, você deve selecionar de qual número a qual numero o programa deve sortear\n"
          "Exemplo de 1 á 10")
    continue_choice = 'sim'
    win = 0
    lose = 0

    while continue_choice.upper() == 'SIM':
        min_number = int(input('Selecione o primeiro número: '))
        max_number = int(input('Selecione o segundo número: '))
        guesser = random.randrange(min_number, max_number)
        player_guess = int(input('Qual o número você acha que foi escolhido? '))
        if player_guess == guesser:
            print(f'Você escolheu o número {player_guess} e a maquina o número {guesser}\nParabéns, você venceu')
            win += 1
        else:
            print(f'Você escolheu o número {player_guess} e a maquina o número {guesser}\nVocê Perdeu')
            lose += 1
        print(f'Resultado do jogo:\nVocê {win} X Maquina: {lose}')
        continue_choice = input('Deseja continuar? (Sim/Não): ')
    if win > lose:
        print(f'Obrigado por jogar!!\nVocê venceu o jogo por {win} a {lose}')
    elif win == lose:
        print(f'O jogo terminou emptado em {win} á {lose}')
    else:
        print(f'Obrigado por jogar!!\nA maquina venceu o jogo por {lose} a {win}')


main()
