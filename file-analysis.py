################################################################################
# Author: Atharva Gunda
# Date: 11/22/2020
# This program prints the word frequency, common words, and uncommon words of two given text files.
################################################################################

from string import punctuation

def main():
    file1 = readFile('xian_1.txt')
    file2 = readFile('xian_2.txt')
    lib1 = toLibrary(file1)
    lib2 = toLibrary(file2)
    writeOutput(lib1, 'xian_1_word_frequency.txt')
    writeOutput(lib2, 'xian_2_word_frequency.txt')
    commonWords(lib1, lib2, 'common_words.txt')
    uncommonWords(lib1, lib2, 'eitherbutnotboth.txt')

def readFile(txt):
    fid = open(txt, 'r')
    lines = fid.readlines()
    lines = [sorted(i.split()) for i in lines]
    fid.close()

    return lines

def toLibrary(list):
    temp = []
    for i in range(len(list)):
        for j in range(len(list[i])):
            list[i][j] = list[i][j].lower().strip(punctuation)
            temp.append(list[i][j])
    temp = sorted(set(temp))
    counts = [0] * len(temp)
    for i in range(len(temp)):
        c = 0
        for j in range(len(list)):
            for k in range(len(list[j])):
                if(list[j][k] == temp[i]):
                    c += 1
        counts[i] = c

    return dict(zip(temp, counts))

def writeOutput(lib, txt):
    fid = open(txt, 'w')
    keys = lib.keys()
    for key in keys:
        fid.write(f'{key}: {lib.get(key)}\n')
    fid.close()

def commonWords(words1, words2, txt):
    fid = open(txt, 'w')
    common = sorted(set(words1.keys()) & set(words2.keys()))
    for word in common:
        fid.write(word + "\n")
    fid.close()

def uncommonWords(words1, words2, txt):
    fid = open(txt, 'w')
    common = sorted(set(words1.keys()) ^ set(words2.keys()))
    for word in common:
        fid.write(word + "\n")
    fid.close()

main()
