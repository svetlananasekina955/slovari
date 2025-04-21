
def sinonim():
    sinonims1 = input('Введите первое слово: ').title()
    sinonims2 = input('Введите второе слово: ').title()
    word_sinon = [sinonims1, sinonims2]
    return word_sinon

count_sinon = int(input('Введите количество пар слов: '))
dict_sinon = dict()

for i_count in range(1, count_sinon + 1):
    print(i_count, '-', 'я пара: ')
    dict_sinon[i_count] = sinonim()

while True:
    count = 0
    print()
    word = input('Введите слово:').title()
    if word == 'end'.title():
        break
    for i in dict_sinon:
        if word in dict_sinon[i]:
            for i_index in dict_sinon[i]:
                if i_index != word:
                    print('Синоним:', dict_sinon[i][dict_sinon[i].index(i_index)])
            count += 1
    if count == 0:
        print('Tакого слова нет')

