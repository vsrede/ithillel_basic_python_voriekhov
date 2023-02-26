import random


def pemrtuate(text):  # returns permuted text
    text = text.lower()
    text_lst = text.split()  #
    text_new = list()  # for add element from text_lst
    # add element and mix first 3 character in word
    for i in range(len(text_lst)):
        if len(text_lst[i]) > 3:
            first_three_ch = [text_lst[i][0], text_lst[i][1], text_lst[i][2]]
            mix_three_ch = first_three_ch.copy()
            while mix_three_ch[0] == first_three_ch[0]:
                random.shuffle(mix_three_ch)
            text_new.extend(mix_three_ch)
            text_new.extend(text_lst[i][3:])
        else:
            text_new.extend(text_lst[i])
        text_new.extend(' ')
    # capitalize after dot
    for i in range(len(text_new) - 2):
        if text_new[i] == '.':
            text_new[i + 2] = text_new[i + 2].upper()
    # capitalize first character
    text_new[0] = text_new[0].upper()
    result = ''.join(text_new)
    return result


def main():
    my_text = 'За результатами дослідження одного англійського університету, не має значення,' \
              ' в якому порядку розташовані букви в слові. Головне, щоб перша і остання букви були на місці. ' \
              'Решта букв можуть слідкувати в повному безладі, все одно текст читається без проблем. ' \
              'Причиною цього є те, що ми не читаємо кожну букву окркмо, а все слово цілком.'
    print(*pemrtuate(my_text), sep='')
