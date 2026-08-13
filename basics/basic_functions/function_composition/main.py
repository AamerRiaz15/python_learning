def take_input() -> str:
    try:
        inp = input('Enter the sentence: ')
    except Exception as e:
        print(f'Something went wrong: {e}')
        quit()

    return lower_sentence(inp)

def lower_sentence(sentence: str):
    sentence = sentence.lower()
    return remove_punctuation(sentence)

def remove_punctuation(sentence: str) -> str:
    try:
        punc = ",.!?;:'\"-()[]{}"
        cleaned = ''

        for char in sentence:
            if char not in punc:
                cleaned += char
    except Exception as e:
        print(f'Something went wrong: {e}')
        quit()

    return split_words(cleaned)

def split_words(sentence: str) -> list:
    try:
        assert isinstance(sentence, str)
        words = sentence.split()
    except Exception as e:
        print(f'Something went wrong: {e}')
        quit()

    return count_words(words)

def count_words(words) -> int:
    assert isinstance(words, list)

    count = 0

    try:
        for word in words:
            count += 1
    except Exception as e:
        print(f'Something went wrong: {e}')
        quit()

    return display_result(count)

def display_result(count):
    assert isinstance(count, int)
    try:
        print(f'Word count: {count}')
    except Exception as e:
        print(f'Something went wrong: {e}')
        quit()

take_input()
