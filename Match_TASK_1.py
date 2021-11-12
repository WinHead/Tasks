# Слету задачка не решилась, поэтому воспользуемся методом Монте-Карло и просто-напросто смоделируем данную ситуацию

from random import randint

n_tries = 1000000

total = 0
nice_try_count = 0
for _ in range(n_tries):

    # Задаем для секторов начальное положение. True - активен
    sectors = [True for _ in range(14)]
    n_rounds = 0
    
    # всего 6 раундов
    for _ in range(6):
        # Генерируем случайное число, определяющее какой сектор играет
        r_num = randint(0, 13)
        
        # Если сектор уже играл, берем следующий
        while sectors[r_num] == False:
            r_num += 1
            
            ## Если число оказалась больше 13, то устанавливаем его в ноль
            ## В нашем примере если 13 сектор уже играл, то автоматически сценарий счиатется проваленым,
            ## а значит, данного исхода не будет
            #if r_num > 13:
            #    r_num = 0
                
        # Если выбрали сектор не из нужного списка, автоматически выходим из цикла, так как сценарий провален
        if r_num > 6 or r_num < 1:
            break
            
        # В ином случае отмечаем, что сектор играл
        sectors[r_num] = False
        # И совершаем инкремент счетчика раундов
        n_rounds += 1
        
    # Увеличиваем занчение счетчика опытов
    total += 1
    # И если мы сделали 6 успешных раундов
    if n_rounds > 5:
        # Инкрементируем счетчик удачных попыток
        nice_try_count += 1
        
print(f"P = nice_try_count / total = {nice_try_count} / {total} = {nice_try_count / total}")

# Поличили ответ: 0.002295
