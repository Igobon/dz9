#start
# 1. Даний текстовий файл. Необхідно створити новий файл,
# який потрібно переписати з першого файлу всі слова,
# що складаються не менше ніж з семи літер.

import csv
FILENAME="user.csv"
FILENAME2="user1.csv"


with open("FILENAME","w",encoding="utf-8") as file:#encoding="utf-8" в разі написання слів кирилецею
    file.write("To be, or not to be, that is the question, \nWhether 'tis nobler in the mind to suffer \nThe slings and arrows of outrageous fortune, Or to take arms against a sea of troubles, \nAnd by opposing end them? To die: to sleep; No more; and by a sleep to say we end \nThe heart-ache and the thousand natural shocks \nThat flesh is heir to, 'tis a consummation Devoutly to be wish'd . \nTo die, to sleep")


with open("FILENAME", "r",encoding="utf-8") as file:
    with open("FILENAME2", "w",encoding="utf-8") as file2:
        for raw in file:
            words = raw.split()
            for word in words:
                if len(word) >= 7:
                    file2.write(word+"\n")


# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.
with open("FILENAME","r",encoding="utf-8") as file:
    text=file.read()
    words=text.split()
    count=len(words)
    print("Count of words",count)
