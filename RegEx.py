import re

with open("row.txt","r", encoding="utf-8") as file:
    cnt = file.read()

#Exercise 1-------------------------------------------------------------------------- * means 0 or more of things (can be empty)
ptrn = r"ab*"

with open("row.txt","r", encoding="utf-8") as file:
    for num_line, line in enumerate(file, start=1):
        words = line.split()
        for w in words:
            if re.fullmatch(ptrn, w):
                print(w)
#Exercise 2--------------------------------------------------------------------------
ptrn1 = r"abb"
ptrn2 = r"abbb"

with open("row.txt","r", encoding="utf-8") as file:
    for num_line, line in enumerate(file, start=1):
        words = line.split()
        for w in words:
            if re.fullmatch(ptrn1, w) or re.fullmatch(ptrn2, w):
                print(w)
#Exercise 3-------------------------------------------------------------------------- [a-z] uses alphabet i suppose
ptrn = r"[a-z]_[a-z]"

with open("row.txt","r", encoding="utf-8") as file:
    for num_line, line in enumerate(file, start=1):
        words = line.split()
        for w in words:
            if re.fullmatch(ptrn, w):
                print(w)
#Exercise 4-------------------------------------------------------------------------- [A-Z] uses alphabet but now uppercase
ptrn = r"[A-Z]_[a-z]+"

with open("row.txt","r", encoding="utf-8") as file:
    for num_line, line in enumerate(file, start=1):
        words = line.split()
        for w in words:
            if re.fullmatch(ptrn, w):
                print(w)
#Exercise 5-------------------------------------------------------------------------- ^ ensures it starst with a, $ ensures it ends with b, .* means whatever even nothing counts
ptrn = r"^a.*b$"

with open("row.txt","r", encoding="utf-8") as file:
    for num_line, line in enumerate(file, start=1):
        words = line.split()
        for w in words:
            if re.fullmatch(ptrn, w):
                print(w)
#Exercise 6-------------------------------------------------------------------------- [ .,] everything inside [] is counted, its quite useful
cnt = re.sub(r"[ .,]", ":", cnt)

with open("row.txt", "w", encoding="utf-8") as file:
    file.write(cnt)
#Exercise 7--------------------------------------------------------------------------
cnt = re.sub(r"(_[a-z])", lambda x: x.group(1)[1].upper(), cnt)

with open("row.txt", "w", encoding="utf-8") as file:
    file.write(cnt)
#Exercise 8--------------------------------------------------------------------------
cnts = re.split(r"([A-Z][^A-Z]*)", cnt)
# Exercise 9-------------------------------------------------------------------------- () captures the whole things \1 is first part, \2 is second part
cnt = re.sub(r"([a-z])([A-Z])", r"\1 \2", cnt)

with open("row.txt", "w", encoding="utf-8") as file:
    file.write(cnt)

# Exercise 10-------------------------------------------------------------------------
cnt = re.sub(r"([a-z])([A-Z])", r"\1_\2", cnt).lower()

with open("row.txt", "w", encoding="utf-8") as file:
    file.write(cnt)
