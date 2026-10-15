file_name = input('Enter the file name with the extension: ').strip()

if not file_name:
    file_name = 'school_prompt3.txt'

try:
    with open(file_name, 'w') as md:
        for i in range(20):
            md.write(f"{i}\n")
except Exception as e:
    print(f"Something went wrong: {e}")
    exit()

print(f"Success! Data written to {file_name}")
