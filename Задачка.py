import datetime
import time

a = 2
b = 2
c = a + b
print('a = 2; b = 2')
time.sleep(1)
print('a+b = ???')
time.sleep(1)
start = time.time()
waitforanswer = 3
while True:
    answer = int(input('Введите ответ: '))
    if answer == c:
        print('Ты абсолютно прав!')
        finish = time.time()
        duringtime = int(finish - start)
        if duringtime < waitforanswer:
            print("А ты молодец, справился всего за " + str(duringtime) + ' секунд!')
        if duringtime > waitforanswer:
            print('Но ты все равно проиграл....((( \n Время закончилось, а ты и за '
                  + str(duringtime) + ' секунд не уложился')
            break
        break
    if answer != c:
        print('Не-а, попробуй еще раз')
        finish = time.time()
        duringtime = int(finish - start)
        if duringtime > waitforanswer:
            time.sleep(1)
            print('Ты проиграл ...((( \n Тебе даже ' + str(duringtime) + ' секунд не хватило(')
            time.sleep(1)
            tryto = str.upper(input('Хочешь попробовать угадать ответ? \n Ответь, ДА/НЕТ  \n '))
            if tryto != 'ДА':
                finish2 = time.time()
                duringtime2 = int(finish2 - start)
                time.sleep(1)
                print('Ну еще бы )) Такому как ты, с таким примером, точно не справиться! \n'
                      'ты на это и так убил уже ' + str(duringtime2) + 'Секунд)))')
                break
            if tryto == 'ДА':
                break
while tryto == 'ДА':
    time.sleep(1)
    answer2 = int(input('Введи ответ, который подсказывает интуиция)): \n  '))
    if answer2 == c:
        finish2 = time.time()
        duringtime2 = int(finish2 - start)
        time.sleep(1)
        print('Ну, если мозг не работает, то хоть интуиция должна! \n ПРАВИЛЬНО!')
        time.sleep(1)
        print('Тебе понадобилось всего-то ' + str(duringtime2) + ' секунд')
        break
    if answer2 != c:
        finish2 = time.time()
        duringtime2 = int(finish2 - start)
        time.sleep(1)
        print('Мдаа.... Дружище, тебе бы бирки в морге на большие пальцы вешать О_о')
        time.sleep(2)
        print('Спроси может у своей кошки, она точно умнее тебя. ')
        time.sleep(1)
        print(' Ты даже за ' + str(duringtime2) + ' секунд не справился *рукалицо*')
