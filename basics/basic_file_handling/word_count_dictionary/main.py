words = ["cat", "car", "dog", "door", "apple", "arc", "dune", "cave"]
dictionary1 = {}

for word in words:
    dictionary1[word] = dictionary1.get(word, 0) + 1

print(dictionary1)
