score = input("Enter score between 0.0 and 1.0")

score = float(score)

if score<0.0 or score>1.0:
    print("Out of range")
    quit()
elif score>=0.9:
    print("A")
elif score>=0.8:
    print("B")
elif score>=0.7:
    print("C")
elif score>=0.6:
    print("D")
else:
    print("F")
