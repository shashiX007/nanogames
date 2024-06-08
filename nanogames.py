import random 
# Stone Paper scissor 
def stone_paper_scissor():
    list = ['stone','paper','scissor']
    w = 0
    l = 0
    dic = { '1':'stone','2': 'paper' , '3': 'scissor' }
    print('WELCOME to the Game ©©')
    print('your opponent has choosen something >>> ,   Choose one of the option to beat him ^•^')
    print('1 : stone')
    print('2 : paper')
    print('3 : scissor')
    while True:
        op1 = random.choice(list)
        userinpt  = str(input('Choose your option :  '))
        op2 = dic[userinpt]
        if(op2 == op1):
            print('ops ! its a draw ')
        elif (op1 == 'scissor' and op2 == 'stone'):
            print('You won  your opponent has chosen scissor')
            w += 1
            print ('Match won :  ' + str(w) + '    Match lose : ' + str(l))
        elif(op1 == 'scissor' and op2 == 'paper'):
            print('you lose your opponent has chosen scissor ')
            l += 1
            print ('Match won :  ' + str(w) + '    Match lose : ' + str(l))
        elif(op1 == 'stone' and op1 == 'paper'):
            print('you won your opponent has chosen stone ')
            w += 1
            print ('Match won :  ' + str(w) + '    Match lose : ' + str(l))
        elif(op1 == 'stone ' and op1 == 'scissor' ):
            print('you lose your opponent has choosen stone ')
            l += 1
            print ('Match won :  ' + str(w) + '    Match lose : ' + str(l))
        elif(op1 == 'paper ' and op2 == 'scissor'):
            print('you won your opponents has chosen paper')
            w += 1
            print ('Match won :  ' + str(w) + '    Match lose : ' + str(l))
        elif(op1 == 'paper' and op2 == 'stone'):
            print('you lose your opponent has choosen paper')
            l += 1
            print ('Match won :  '  + str(w) + '    Match lose : ' + str(l))
         
        
    
# Number Guessing Game 
def number_guessing_game():
    Gnumber = random.randint(1,100)
    a = 0
    print(' # welcome  to the number Guessing Game !!!!')
    print('i have selected a Number between 1 to 100' )
    data= []
    while True:
        userinp= input(('Guess the number or quit(Q) : '))
        a += 1 
        data.append(int(userinp))
        if(userinp == 'Q'):
            break
        
        userinp = int(userinp)
        if(userinp == Gnumber):
            print('::::::::Hurray!! You have guessed the     correct number :::::::::::                                                 Attempts:' + str(a))
            print('Your enteries are ' + str(data))
            break
        
        elif(userinp > Gnumber):
            print(f'Your guess is too big guess the smaller number ')
        else:
            print('Your Guess is too small guess the Bigger  number ')
    if userinp == 'Q':
        print('             !!!!You cannot even complete this game !!!!')       
    else:
        print('                    ___________GAME OVER ____________')
        
        
        
# initial Start         
print('1 : Number Guessing Game')
print('2 : stone-paper-scissor')
print('3 : Quit(Q)')

while True:
    selection = str(input('Choose one of the game : '))
    if(selection == '1'):
      number_guessing_game()
      break 
    elif(selection == '2'):
      stone_paper_scissor()
    elif(selection == 'Q'):
        print('Thank you ')
        break
    else:
      print('invalid option')

