actually = float(input ("Сколько км спортсмен пробежал в первый день?"))
purpose = float(input ("Не менее скольки км спортсмен хочет пробегать за 1 тренировку?"))
days = 1
if actually <= 0 or purpose < 0:
    print ("Результат в первый день должен быть больше нуля, а желаемый больше или равен 0 ")
else:
    while actually < purpose:
        actually = actually * 1.1
        days = days + 1
print (f"На {days} день спортсмен достигнет своего результата")