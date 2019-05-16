import sys
import readWords

def wordsInOrder(char1, char2, char3):
    allWords = readWords.load_words()
    filtered = []
    for word in allWords:
        # check if all characters appear in the word
        if char1 in word and char2 in word and char3 in word:
            # find first occurence of char1
            pos1 = 0
            for i, char in enumerate(word):
                if char == char1:
                    pos1 = i
                    break

            # find last occurence of char3
            pos3 = 0
            for i, char in enumerate(reversed(word)):
                if char == char3:
                    pos3 = len(word) - i
                    break

            # find if an occurence of char2 occurs between the first occurence of char1 and the last occurence of char3
            # if so append the word to filtered
            for i, char in enumerate(word[pos1:pos3]):
                if char == char2:
                    filtered.append(word)
    return filtered

if __name__ == "__main__":
    c1 = sys.argv[1]
    c2 = sys.argv[2]
    c3 = sys.argv[3]
    print(wordsInOrder(c1,c2,c3))
