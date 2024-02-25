import winsound
import time

MORSE_CODES: dict = {
    "A": "._",
    "B": "_...",
    "C": "_._.",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "O": "___",
    "P": ".__.",
    "Q": "__._",
    "R": "._.",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__..",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    "0": "_____",
    " ": "/",
    '.': '._._._',
    ',': '__..__',
    '?': '..__..',
    '\'': '.___.',
    '!': '_._.__',
    '/': '_.._.',
    '(': '_.__.',
    ')': '_.__._',
    '&': '._...',
    ':': '___...',
    ';': '_._._.',
    '=': '_..._',
    '+': '._._.',
    '-': '_...._',
    '_': '..__._',
    '"': '._.._.',
    '$': '..._.._',
    '@': '.__._.',
}


def text_to_morse(txt: str) -> str:
    output: str = ""
    for char in txt:
        try:
            output += MORSE_CODES[char] + " "
        except KeyError:
            output = f"{char} can't be translated to morse code."

    return output


def morse_to_text(morse: str) -> str:
    # Create a new dictionary where key is morse code and value is the character
    codes: dict = {morse: char for char, morse in MORSE_CODES.items()}
    morse = morse.split()
    output: str = ""
    for m in morse:
        try:
            output += codes[m]
        except KeyError:
            output += f"\n {m} is a invalid morse code."
    return output


def play_sound(morse: str) -> None:
    print(f"{'Morse Code':<20}: ", end="")
    for m in morse:
        if m == "_":
            print(m, end="")
            winsound.Beep(700, 600)
        elif m == ".":
            print(m, end="")
            winsound.Beep(700, 200)
        else:
            print(m, end="")
            time.sleep(0.3)


def main():
    print(f"\n{'Welcome to the Morse Code Translator':-^50}\n")
    process = input("Select Mode:\nText to Morse / Morse to Text (1/2). ")

    match process:
        case "1":
            text: str = input(f"\n{'Enter Text':<20}: ").upper()
            translated_code = text_to_morse(text)
            play_sound(translated_code)

        case "2":
            # Replace dash with underscore if there are any
            text: str = input(f"\n{'Enter Morse Code':<20}: ").replace("-", "_")
            print(f"{'Message':<20}: {morse_to_text(text)}")

        case _:
            print("Invalid Selection!")


if __name__ == '__main__':
    main()
