def sub_sequence(seq):
    if not seq: # пустая последовательность
        return seq

    index_for_loop = [None] * len(seq) # список из пустых значений по длине переданного списка
    previous_elem = [None] * len(seq) # т. е. если длина 3 то список = [None, None, None]
    
    # Минимальная длина списка если он не пуст = 1
    seq_loop = 1
    index_for_loop[0] = 0

    # Цикл сразу со второго элемента
    for i in range(1, len(seq)): # итерация по индексу
        lower = 0
        upper = seq_loop

        # Проверка верхней границы
        if seq[index_for_loop[upper - 1]] < seq[i]: 
            j = upper

        else:
            # цикл бинарного поиска
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[index_for_loop[mid - 1]] < seq[i]: 
                    lower = mid
                else: 
                    upper = mid

            j = lower # установка в 0 по дефолту

        previous_elem[i] = index_for_loop[j - 1] # обратный перебор, потом развернуть список

        if j == seq_loop or seq[i] < seq[index_for_loop[j]]: 
            index_for_loop[j] = i
            seq_loop = max(seq_loop, j + 1)

    result = []
    pos = index_for_loop[seq_loop - 1]
    for seq_loop in range(seq_loop):
        result.append(seq[pos])
        pos = previous_elem[pos]

    print(result[::-1]) # принт перевернутой версии результата
    
sub_sequence([9,3,7,4,6,9,3,13,5,0])


