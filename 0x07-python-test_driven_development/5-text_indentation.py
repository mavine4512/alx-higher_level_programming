#!/usr/bin/python3
'''Contains a text_indentation function a TDD project.
'''


def text_indentation(text):
    '''Print a text with 2 new line after each of 
    these characters: '.','?' and ':'
    Args:
        text(str): The text to print.
    Raises:
        TypeError: If the text is not a string.
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
