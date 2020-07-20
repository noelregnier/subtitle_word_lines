import re
import argparse

#take a word for seach from a user
parser = argparse.ArgumentParser()
parser.add_argument("--word", help="Enter a word you want to look up in the combined file", required=True)
args = parser.parse_args()

#how many times each word happens in the the TV series

all_lines = []   #list with text lines from subtitles
words = []    #list with separate words from all_lines
counts = {}   #dictionary to count word's frequencies


try:
    with open("combined_file.txt", "r") as file:
        line = file.readline()
        while line !='':
            if not (re.findall('[0-9]', line) or re.findall('^\n', line)):
                # line = line.strip().lstrip("<i>").rstrip("</i>")
                all_lines.append(line)
            line = file.readline()
except:
    print("combined_file.txt is not found. Please run create_combined_file.py first")
    quit()

# make separated words
for item in all_lines:
    separated_items = item.split()
    for m in separated_items:
        words.append(m)

for word in words:
    word = word.lower().strip().lstrip("<i>").rstrip("</i>").strip('"').rstrip(",").rstrip(".").rstrip("!").rstrip("?")
    counts[word] = counts.get(word, 0) + 1


# #Result1 - print all words with frequencies
# for b in sorted([(v,k) for k,v in counts.items()], reverse=True):
#     print(b)

# Result2 - how many times a word happens in the subtitles and exact lines with it
# check if the word entered by a user is among lines
guess_input = args.word
guess = guess_input.lower()
if guess not in counts:
    print("The word is not found.")
    quit()
print("For '{}' we have these results: {}".format(guess_input, counts[guess]))


#print all lines with the desired word guess
index = []
for i, line in enumerate(all_lines):
    line = line.lower()
    strict = re.findall('^'+guess+'[^a-z]', line)
    if len(strict) == 0:
        strict = re.findall('[^a-z]' + guess + '[^a-z]', line)
    if len(strict) > 0:
        index.append(i)


#print found lines
print("The results are:"+"\n")
number = 0

for i in index:
    number = number+1
    sentence = []
    k = i
    ss = True
    while ss:
        line = all_lines[k]
        sentence.append(line)
        line = line.strip()
        k = k+1
        if (line.endswith(".") or line.endswith("!") or line.endswith("?") or line.endswith("?!")):
            ss = False
    k = i
    while True:
        k = k - 1
        line = all_lines[k]
        line1 = line.strip()
        if (line1.endswith(".") or line1.endswith("!") or line1.endswith("?") or line1.endswith("?!")):
            break
        sentence.insert(0, line)

    sen = ""

    for m in sentence:
        sen = sen + m
    print("Result {}:".format(number))
    print(sen)
    print("----------------------------")




        


