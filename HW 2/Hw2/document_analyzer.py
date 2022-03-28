from collections import Counter
def parseFile():
    with open("E:\School stuff\Code\cmpe 131\HW 2\Hw2\q2\SampleText.txt", "r") as file:
        
        words=[None] * 1

        for line in file:
            for word in line.split():
                words.append(word)
    words.sort()
    word_counts = Counter(words)
    top_five = word_counts.most_common(5)
    print(top_five)



parseFile()
