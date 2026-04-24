from pathlib import Path
from string import ascii_uppercase

DICTIONARY_PATH = Path.home() / 'Documents' / 'Main' / 'English' / 'Dictionary'
LETTERS = list(ascii_uppercase)


def main():
    for letter in LETTERS:
        letter_path = DICTIONARY_PATH / f'{letter}.md'
        if not letter_path.exists():
            print(f'Path {letter_path} does not exist, skip it')
            continue

        data = letter_path.read_text(encoding='utf-8')
        for line in data.splitlines():
            if line.find('-') != -1:
                word = line.split('-')[0].strip()
                translate = line.split('-')[1].strip()
                if len(translate) == 0:
                    print(word)


if __name__ == '__main__':
    main()
