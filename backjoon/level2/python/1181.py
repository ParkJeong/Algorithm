test_cases = int(input())

dictionary = [input() for _ in range(test_cases)]

dictionary = set(dictionary)
dictionary = list(dictionary)
dictionary.sort()
dictionary.sort(key=lambda x: len(x))

for word in dictionary:
    print(word)