import random


def pemrtuate(text):  # returns permuted text
    lst_text = text.split()
    result = list()
    for word in lst_text:
        mix_word = list()
        if len(word) > 4:
            three_ch = [word[1], word[2], word[3]]
            mix_word = list(word)
            mix_three_ch = three_ch.copy()
            while mix_three_ch == three_ch:
                random.shuffle(mix_three_ch)
            mix_word[1], mix_word[2], mix_word[3] = mix_three_ch[0], mix_three_ch[1], mix_three_ch[2]
            result.append(''.join(mix_word))
        else:
            result.append(word)

    return result
def main():
    my_text = 'За результатами дослідження одного англійського університету, не має значення,' \
              ' в якому порядку розташовані букви в слові. Головне, щоб перша і остання букви були на місці. ' \
              'Решта букв можуть слідкувати в повному безладі, все одно текст читається без проблем. ' \
              'Причиною цього є те, що ми не читаємо кожну букву окркмо, а все слово цілком.'
    print(*pemrtuate(my_text), sep=' ')


if __name__ == '__main__':
    main()
