import wikipedia

while True:
    try:
        print(wikipedia.summary(input("Q: ")))
    except:
        continue
