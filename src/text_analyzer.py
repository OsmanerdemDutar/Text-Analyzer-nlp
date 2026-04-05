import locale
locale.setlocale(locale.LC_ALL, "en_US")
from sys import argv

#Calculating number of words =
def num_words(f_in,f_out):
    f_in.seek(0)
    total = 0

    for line in f_in:
        if line.strip():
            line = line.split()
        total = total + len(line)

    f_out.write("{:24}{:2}{}\n".format("#Words", ":", total))
    return total


#Calculating number of sentences =
def num_sentences(f_in,f_out):
    f_in.seek(0)
    content = f_in.read()
    total = 0

    for i in content:
        if i in [".","?","!"]:
            total +=1

    three_points = content.count("...")    # 3 sentences are counted because of the "..."
    total = total - (2*three_points)       # exception was fixed with this operation

    f_out.write("{:24}{:2}{}\n".format("#Sentences",":",total))

    return total


#Calculating average Number of Words per Sentence =
def average(num_word,num_sentence,f_out):

    f_out.write("{:24}{:2}{:.2f}\n".format("#Words/#Sentences",":",num_word/num_sentence))

#Calculating number of Characters (Excluding the Punctuations and White-Spaces)
def all_characters(f_in,f_out):
    f_in.seek(0)
    total = 0

    for line in f_in:
        for character in line:
            a = len(character)
            total += a

    f_out.write("{:24}{:2}{}\n".format("#Characters",":",total))

#Calculating number of Characters =
def js_characters(f_in,f_out):
    f_in.seek(0)
    total = 0

    for line in f_in:
        if line.strip():    #skips empty lines
            for js_chrctr in line.split():
                js_chrctr = js_chrctr.strip(".,!?;:'()[]{}<>-_/*\\=+&|^%$#@`~")
                a = len(js_chrctr)
                total += a

    f_out.write("{:24}{:2}{}\n".format("#Characters (Just Words)",":",total))


#Calculating Frequencies of all words
#Calculating The Shortest and Longest Word(s)
def sorting_by_freq(f_in,f_out):
    f_in.seek(0)

    content = f_in.read()
    content = content.split()  #list of words
    a = []                     #list of clean words
    b = []                     #list of words and words frequency

   #cleaning the words
    for word in content:
        word = word.lower()
        word = word.strip(".,!?;:'()[]{}<>-_/*\\=+&|^%$#@`~")
        a.append(word)

    #finding frequency
    def frequency(word):
        x = a.count(word)
        y = len(a)
        return x / y

    #creat a List of words and words frequency
    for word in set(a):
        l = [word, frequency(word)]
        b.append(l)

    #Finding the shortest words
    b = sorted(b, key=lambda x: (len(x[0]), -x[1], x[0]))  #sorted for the shortest and the longest words
    c = []    #list of shortest words
    shortest = min(b, key=lambda x: (len(x[0]), -x[1], x[0]))

    for [words,freq] in b:
        if len(words) == len(shortest[0]):
            c.append([words, freq])

    if len(c) == 1:
        words , freq = c[0]   #we have to change current value of words and freq
        f_out.write("{:24}{:2}{:25}({:.4f})\n".format("The Shortest Word", ":", words, freq))

    elif len(c) > 1:
        f_out.write("{:24}{}\n".format("The Shortest Words",":"))
        for [words,freq] in c:
            f_out.write("{:25}({:.4f})\n".format(words, freq))

    #Finding the longest words
    longest = max(b, key=lambda x: (len(x[0]), -x[1] , x[0]))
    d = []     #list of longest words
    for [words,freq] in b:
        if len(words) == len(longest[0]):
            d.append([words, freq])

    if len(d) == 1:
        words , freq = d[0]
        f_out.write("{:24}{:2}{:25}({:.4f})\n".format("The Longest Word", ":", words, freq))

    elif len(d) > 1:
        f_out.write("{:24}{}\n".format("The Longest Words",":"))
        for [words,freq] in d:
            f_out.write("{:25}({:.4f})\n".format(words, freq))

    #sorting by frequency
    f_out.write("{:24}{}\n".format("Words and Frequencies", ":"))

    #sorting by frequency in b
    b = sorted(b, key=lambda x: (-x[1],x[0]) )

    for [words, freq] in b[:-1]:   #writing until the end except the last one
        f_out.write("{:24}{:2}{:.4f}\n".format(words, ":", freq))
    #writing the last one
    f_out.write("{:24}{:2}{:.4f}".format(b[-1][0], ":",b[-1][1] ))


def main():
    f_in = open(argv[1], 'r')
    f_out = open(argv[2], 'w')

    f_out.write("Statistics about {} :\n".format(argv[1]))

    words = num_words(f_in, f_out)           # function called once and I assigned the value to use for average
    sentences = num_sentences(f_in, f_out)   # function called once and I assigned the value to use for average
    average(words,sentences,f_out)
    all_characters(f_in, f_out)
    js_characters(f_in, f_out)
    sorting_by_freq(f_in, f_out)

    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()

