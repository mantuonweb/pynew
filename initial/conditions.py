num = input("Plz enter number: \n")
x = int(num)
if x < 0:
    print("Negative number")
elif x == 0:
    print("Zero")
elif x > 0:
    print("Positive number")

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))