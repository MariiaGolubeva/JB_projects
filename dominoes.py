import random

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def generate():
    stock = []
    computer_pieces = []
    player_pieces = []
    for i in range(0, 7):
        for j in range(0, 7):
            new_piece = []
            new_piece.extend([i, j])
            unique = True
            for p in stock:
                if p == [new_piece[1], new_piece[0]]:
                    unique = False
            if unique is True:
                stock.append(new_piece)

    for i in range(0, 7):
        ind = random.randrange(0, len(stock))
        player_pieces.append(stock[ind])
        stock.remove(stock[ind])

    for i in range(0, 7):
        ind = random.randrange(0, len(stock))
        computer_pieces.append(stock[ind])
        stock.remove(stock[ind])
    return stock, player_pieces, computer_pieces

def define_doubles(player_p, computer_p):
    doubles_player = []
    for i in player_p:
        if i[0] == i[1]:
            doubles_player.append(i[0])
    if len(doubles_player) > 0:
        snake_p = doubles_player[0]
        for i in doubles_player:
            if snake_p < i:
                snake_p = i
    else:
        snake_p = False

    doubles_computer = []
    for i in computer_p:
        if i[0] == i[1]:
            doubles_computer.append(i[0])
    if len(doubles_computer) > 0:
        snake_c = doubles_computer[0]
        for i in doubles_computer:
            if snake_c < i:
                snake_c = i
    else:
        snake_c = False
    return snake_p, snake_c

def define_snake(snake_p, snake_c):
    if type(snake_p) == int:
        if type(snake_c) == int:
            if snake_p > snake_c:
                final_snake = snake_p
            else:
                final_snake = snake_c
        else:
            final_snake = snake_p
    else:
        final_snake = snake_c
    if final_snake == snake_p:
        status = 'computer'
    elif final_snake == snake_c:
        status = 'player'
    return [final_snake, final_snake], status

stock, player_p, computer_p = generate()
player_snake, computer_snake = define_doubles(player_p, computer_p)
#print(player_snake, computer_snake)

repetitions = 0
while player_snake is False and computer_snake is False:
    repetitions += 1
    stock, player_p, computer_p = generate()
    player_snake, computer_snake = define_doubles(player_p, computer_p)
    continue

#print(repetitions)
#print(player_p, computer_p)

snake_l, status = define_snake(player_snake, computer_snake)
snake = []
snake.append(snake_l)

if status == 'computer':
    player_p.remove(snake_l)
elif status == 'player':
    computer_p.remove(snake_l)
while True:
    print('='*70)
    print('Stock size:', len(stock))
    print('Computer pieces:', len(computer_p))
    if len(snake) > 6:
        print(snake[0], snake[1], snake[2], '...', snake[-3], snake[-2], snake[-1])
    else:
        print(*snake)
    print('Your pieces:')
    ind = 1
    for i in player_p:
        print(str(ind)+':', i)
        ind += 1
    if len(player_p) == 0:
        print('Status: The game is over. You won!')
        break
    elif len(computer_p) == 0:
        print('Status: The game is over. The computer won!')
        break
    else:
        if snake[0][0] == snake[-1][-1]:
            number = 0
            for i in snake:
                number += i.count(snake[0][0])
            if number == 8:
                print('Status: The game is over. It\'s a draw!')
                break

    if status == 'computer':
        print('Status: Computer is about to make a move. Press Enter to continue...')
        #print(computer_p)
        if input():
            pass
        while status == 'computer':
            comp_dict = dict()
            for i in range(0,7):
                n = 0
                for j in computer_p:
                    n += j.count(i)
                for s in snake:
                    n += s.count(i)
                comp_dict[i] = n
            #print(comp_dict)
            scores = dict()
            k = 0
            for i in computer_p:
                scores[k] = comp_dict[i[0]] + comp_dict[i[1]]
                k += 1
            #print(scores)
            sorted_scores = {}
            sorted_keys = sorted(scores, key=scores.get)
            sorted_keys.reverse()
            for w in sorted_keys:
                sorted_scores[w] = scores[w]
            #print(sorted_scores)
            left = snake[0][0]
            right = snake[-1][-1]
            for i in sorted_scores:
                domino = computer_p[i]
                if left in domino:
                    computer_p.remove(domino)
                    domino.remove(left)
                    domino.append(left)
                    snake.insert(0, domino)
                    status = 'player'
                    break
                elif right in domino:
                    computer_p.remove(domino)
                    domino.remove(right)
                    domino.insert(0, right)
                    snake.append(domino)
                    status = 'player'
                    break
                else:
                    continue
            if status == 'computer':
                if len(stock) != 0:
                    ind = random.randrange(0, len(stock))
                    computer_p.append(stock[ind])
                    stock.remove(computer_p[-1])
                else:
                    pass
            status = 'player'

    else:
        print('Status: It\'s your turn to make a move. Enter your command.')
        while status == 'player':
            move = input()
            if is_number(move) is False:
                print('Invalid input. Please try again.')
                continue
            else:
                if int(move) == 0:
                    if len(stock) != 0:
                        ind = random.randrange(0, len(stock))
                        player_p.append(stock[ind])
                        stock.remove(player_p[-1])
                    else:
                        pass
                else:
                    if abs(int(move)) > len(player_p):
                        print('Invalid input. Please try again.')
                        continue
                    else:
                        domino = player_p[abs(int(move)) - 1]
                        if int(move) > 0:
                            if snake[-1][-1] in domino:
                                player_p.remove(domino)
                                domino.remove(snake[-1][-1])
                                domino.insert(0, snake[-1][-1])
                                snake.append(domino)
                            else:
                                print('Illegal move. Please try again.')
                                continue
                        else:
                            if snake[0][0] in domino:
                                player_p.remove(domino)
                                domino.remove(snake[0][0])
                                domino.append(snake[0][0])
                                snake.insert(0, domino)
                            else:
                                print('Illegal move. Please try again.')
                                continue
            status = 'computer'
