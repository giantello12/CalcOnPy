# CalcOnPy
while(True):
    action = ''
    while(True):
        print("Выберите действие: ", 
            "'+' - сложение",
            "'-' - вычитание",
            "'*' - умножение",
            "'/' - деление", sep="\n")
        action = input()
        if action not in "+-*/":
            print("Введено некорректное действие")
            continue
        else:
            break

    num1, num2 = 0, 0
    while(True):
        print("Введите первое число")
        num1 = int(input())
        print("Введите второе число")
        num2 = int(input())
        if action == '/' and num2 == 0:
            print("Делить на ноль нельзя!")
            continue
        break

    match action:
        case '+':
            print(f'{num1} + {num2} = {num1 + num2}')
        case '-':
            print(f'{num1} - {num2} = {num1 - num2}')
        case '/':
            print(f'{num1} / {num2} = {num1 / num2}')
        case '*':
            print(f'{num1} x {num2} = {num1 * num2}')
    
    print("Продолжить работу программы?",
          "(Введите 'да' если желаете продолжить)", sep='\n')
    answ = input()
    
    if answ.lower().strip() == 'да':
        continue
    else:
        print("До встречи!")
        break