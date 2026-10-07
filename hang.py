
import random

lists = ("hero", "honda", "ronaldo", "yoyo")
penalty = ("head gone", "body gone", "leg gone")

w = random.choice(lists)
l = len(w)
b = ["_"] * l
trys = 2
count = l

print(" ".join(b))

while trys >= 0:
    letter = input("Enter the letter: ").lower()
    start = 0
    ind = w.count(letter)

    if ind == 0:
        print(penalty[trys])
        trys -= 1
    else:
        for i in range(ind):
            pos = w.find(letter, start)
            if pos == -1:
                break

            if b[pos] == "_":
# we can access each index of string or letter by just doing  string[x]=somin "x being position of letter"
                b[pos] = letter
                count -= 1

            start = pos + 1

        print(" ".join(b))

        if count == 0:
            print("You won!")
            break

if trys < 0:
    print("You lost! The word was:", w)
