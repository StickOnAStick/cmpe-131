from collections import Counter

#opens the file. the with statement here will automatically close it afterwards.
with open("E:\School stuff\Code\cmpe 131\HW 2\Hw2\q2\SampleText.txt") as input_file:
    #builds a counter object for each line, then further by each word using line.split() which breaks words up by white spacing
    count = Counter(word for line in input_file
                         for word in line.split())
    return count

print(count.most_common(5))