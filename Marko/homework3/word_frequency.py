#nacin1
from collections import Counter

def word_frequency(fruit_names):
    name_count = Counter(fruit_names)
    name_count.items()
    return name_count.items()


words_list = ['apple', 'banana', 'apple', 'cherry', 'banana', 'banana',
'apple', 'date']

print(word_frequency(words_list))

#nacin2
from collections import Counter

def word_frequency(fruit_names):
    name_count = Counter(fruit_names)
    name_count.most_common()
    return name_count.most_common()


words_list = ['apple', 'banana', 'apple', 'cherry', 'banana', 'banana',
'apple', 'date']

print(word_frequency(words_list))