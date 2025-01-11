from collections import Counter
from itertools import count


def analyzeTest(text):
    text = text.strip()
    paragraphs = text.split('\n')
    sentences = text.split('.')
    sentences.remove('')
    words = text.replace('\n', ' ').split(' ')

    print(f"Liczba akapitow: {len(paragraphs)}")
    print(f"Liczba zdan: {len(sentences)}")
    print(f"Liczba slow: {len(words)}")

    stop_words = {'a', 'w', 'z', 'i', 'o', 'the', 'or', 'to'}
    filtered_words = filter(lambda word: word not in stop_words, words)

    word_count = Counter(filtered_words)
    most_common = word_count.most_common(5)
    print(f"Najczestsze slowa: {most_common}")

    reversAWords = [word[::-1] if word.startswith('a') else word for word in words]
    print(f"Odwrocone slowo na a: {' '.join(reversAWords)}")


# text = """
# apple
# apple
# apple
# apple
# apple
# apple
# apple
# apple
# ala ma kota
# kot ma ale
# Lorem Ipsum is simply dummy text of the printing and typesetting industry.
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
# when an unknown printer took a galley of type and scrambled it to make
# a type specimen book. It has survived not only five centuries,
# but also the leap into electronic typesetting,
# remaining essentially unchanged. It was popularised in the 1960s with
# the release of Letraset sheets containing Lorem Ipsum passages,
# and more recently with desktop publishing software like Aldus PageMaker
# including versions of Lorem Ipsum.
# """

text = """
apple. apple
apple
apple
apple
apple
apple
ala ma kota
kot ma ale
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
"""

analyzeTest(text)