import re

dict_word = {}
with open("slovar_new.txt", "r", encoding="utf-8") as file:
    data = file.readlines()
    for words in data:
        if " — 1)" not in words and "1)" in words:
            patt = re.compile('1\)')
            word_list = re.split(patt, words, maxsplit=0)
            if len(word_list) > 1:
                key_word = word_list[0][:-1]
                value_word = "— 1)" + word_list[1]
                patt_2 = re.compile('2\)')
                word_list_2 = re.split(patt_2, value_word, maxsplit=0)
                value_word_1 = word_list_2[0][:-2]
                value_word_2 = "— 2)" + word_list_2[1][:-1]
                dict_word.setdefault(key_word, []).append(value_word_1)
                dict_word.setdefault(key_word, []).append(value_word_2)
        elif "/" in words:
            patt = re.compile("(/.{1,12}/|I.{2,12}J)")
            word_list = re.split(patt, words, maxsplit=0)
            if len(word_list) > 2:
                key_word = word_list[0][:-1]
                value_word = " ".join(word_list[1:])
                dict_word.setdefault(key_word, []).append(value_word)
        else:
            word_list = re.split(" — ", words, maxsplit=0)
            if len(word_list) > 1:
                key_word = word_list[0]
                value_word = " ".join(word_list[1:])
                dict_word.setdefault(key_word, []).append(value_word)
request = input()
punct = ';,'

u = 0
print('Точные совпадения: ')
for word, definition in dict_word.items():
    new_definition = ''
    for d in definition:
        new_definition += str(d)
    newnew_def = re.split(';|,', new_definition)
    for b in newnew_def:
        if b == request:
            u += 1
            for elem in definition:
                print(word)
                pr_def = elem.split(';')
                for e in pr_def:
                    print(e)
if u == 0:
    print('Точных совпадений не найдено.')

k = 0
print('Слова, содержащие ваш запрос: ')
for word, definition in dict_word.items():
    for w in definition:
        if request in w:
            k += 1
            for elem in definition:
                print(word)
                pr_def = elem.split(';')
                for e in pr_def:
                    print(e)
if k == 0:
    print('Такого слова нет в словаре.')
