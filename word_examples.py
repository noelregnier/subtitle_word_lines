import re

all_lines = []

# get rid of lines which start with a digit or a whitespace and add the rest to all_lines
def refine_lines():
    try:
        with open("combined_file.txt", "r") as file:
            for line in file:
                if (re.search('^[0-9]+', line) or re.search('^\n', line)):
                    continue
                all_lines.append(line)

    except:
        print("combined_file.txt is not found. Please run create_combined_file.py first")
        quit()

#store index fore lines in which the searched word occurs.
def check_word(word):
    guess = word
    for i, line in enumerate(all_lines):
        line = line.lower()
        #word should not be a part of another word in a line
        if (re.search('^' + guess + '[^a-z]+', line) or re.search('[^a-z]+' + guess + '[^a-z]+', line)):
            index.append(i)

def print_picked_lines():
    if len(index) == 0:
        print("No results found")
    else:
        print("The results are:" + "\n")
        number = 0

        for i in index:
            number = number + 1
            sentence = []
            big = i
            while True:
                if big == (len(all_lines)-1): break
                line = all_lines[big]
                sentence.append(line)
                line = line.strip()
                if re.search("[.!?>]$", line): break

                # if (line.endswith(".") or line.endswith("!") or line.endswith("?") or line.endswith(".</i>") or line.endswith("?</i>") or line.endswith("!</i>") or line.endswith(")</i>")):
                #     break
                big = big + 1

            small = i - 1
            while True:
                if small < 0 : break
                line_raw = all_lines[small]
                line = line_raw.rstrip()
                if re.search("[.!?>]$", line): break

                # if (line.endswith(".") or line.endswith("!") or line.endswith("?") or line.endswith(".</i>") or line.endswith("?</i>") or line.endswith("!</i>") or line.endswith(")</i>")):
                #     break
                sentence.insert(0, line)
                small = small - 1


            sen = ""

            for m in sentence:
                sen = sen + m
            print("Result {}:".format(number))
            print(sen)
            print("----------------------------")

#execution
refine_lines()
while True:
    word = input("Please enter a word or 'quit' to exit ")
    word = word.lower()
    if word == "quit": quit()
    index = []
    check_word(word)
    print_picked_lines()







