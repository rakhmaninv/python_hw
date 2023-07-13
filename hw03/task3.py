# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
# препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
import string


def word_count(words: list) -> list:
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return list(result.items())


def n_most_common(lst: list, n: int) -> list:
    return sorted(lst, key=lambda x: x[1], reverse=True)[0:n]


with open('big_string.txt', 'r') as file:
    text = ' '.join(line.strip().lower() for line in file)

TOP_RESULTS = 10

text = text.translate(str.maketrans('', '', string.punctuation))
word_list = list(filter(None, text.split()))
counter = word_count(word_list)

print(n_most_common(counter, TOP_RESULTS))
