import random


def pemrtuate(text):  # returns permuted text
    lst_text = text.split()
    result = list()
    for word in lst_text:
        mix_word = list()
        new_word = list()
        if len(word) > 4:
            new_word.append(*word[0])
            word = word[1:]
            end_letter = word[-1]
            word = word[:-1]
            while True:
                if len(word) > 2:
                    three_ch = [word[0], word[1], word[2]]
                    mix_word = list(word)
                    mix_three_ch = three_ch.copy()
                    while mix_three_ch == three_ch:
                        random.shuffle(mix_three_ch)
                    new_word.append(''.join(mix_three_ch))
                    word = word[3:]
                else:
                    new_word.append(''.join(word))
                    break
            new_word.append(''.join(end_letter))
            result.append(''.join(new_word))
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
