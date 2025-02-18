from pyfiglet import *
print(figlet_format("Ascii Art Generator"))
text = input("text: ")
font = input("font: ")
print(figlet_format(text, font=font))
