file_name = input('Enter the file name: ')
if len(file_name) < 1:
     file_name = 'sample.txt'

dictionary1 = {}

try:
    with open(file_name, 'r') as md:
        text = md.read()
        words = text.split()

        for word in words:
                dictionary1[word] = dictionary1.get(word, 0) + 1
except Exception as e:
    print(f'Something went wrong: {e}')
    exit()

for key, value in dictionary1.items():
    print('Key:', key)
    print('Count:', value)
