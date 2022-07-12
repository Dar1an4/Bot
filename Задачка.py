import time
import random

a = random.randint(1, 10)
b = random.randint(1, 10)
a1 = str(a)
b1 = str(b)
c = a + b
print(a1 + '+' + b1 + '= ????')
time.sleep(0.5)
start = time.time()
waitforanswer = 5
while True:
    answer = int(input('Введите ответ: '))
    if answer == c:
        finish = time.time()
        time.sleep(0.5)
        print('Ты абсолютно прав!')
        time.sleep(0.5)
        duringtime = int(finish - start)
        if duringtime < waitforanswer:
            time.sleep(0.5)
            print("А ты молодец, справился всего за " + str(duringtime) + ' секунд!')
        if duringtime > waitforanswer:
            time.sleep(0.5)
            print('Но ты все равно проиграл....(((')
            time.sleep(0.5)
            print('Время закончилось, а ты и за '
                  + str(duringtime) + ' секунд не уложился')
            time.sleep(0.5)
            break
        time.sleep(0.5)
        break
    if answer != c:
        time.sleep(0.5)
        print('Не-а, попробуй еще раз')
        finish = time.time()
        duringtime = int(finish - start)
        if duringtime > waitforanswer:
            time.sleep(0.5)
            print('Ты проиграл ...((( \n Тебе даже ' + str(duringtime) + ' секунд не хватило(')
            time.sleep(0.5)
            tryto = str.upper(input('Хочешь попробовать угадать ответ? \n Ответь, ДА/НЕТ  \n '))
            if tryto == 'НЕТ':
                finish2 = time.time()
                duringtime2 = int(finish2 - start)
                time.sleep(0.5)
                print('Ну еще бы )) Такому как ты, с таким примером, точно не справиться! \n'
                      'ты на это и так убил уже ' + str(duringtime2) + 'Секунд)))')
                break
            if tryto == 'ДА':
                while True:
                    time.sleep(0.5)
                    answer2 = int(input('Введи ответ, который подсказывает интуиция)): \n  '))
                    if answer2 == c:
                        finish2 = time.time()
                        duringtime2 = int(finish2 - start)
                        time.sleep(0.5)
                        print('Ну, если мозг не работает, то хоть интуиция должна! \n ПРАВИЛЬНО!')
                        time.sleep(0.5)
                        print('Тебе понадобилось всего-то ' + str(duringtime2) + ' секунд')
                        break
                    if answer2 != c:
                        finish2 = time.time()
                        duringtime2 = int(finish2 - start)
                        time.sleep(0.5)
                        print('Мдаа.... Дружище, тебе бы бирки в морге на большие пальцы вешать О_о')
                        time.sleep(0.5)
                        print('Спроси может у своей кошки, она точно умнее тебя. ')
                        time.sleep(0.5)
                        print(' Ты даже за ' + str(duringtime2) + ' секунд не справился *рукалицо*')
