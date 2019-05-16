import filterWords
import sys

def allWordsInOrder(shouldPrint):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    words = []
    with open("noWordsExist.txt", "w") as f:
        for c1 in alphabet:
            for c2 in alphabet:
                if c1 != c2:
                    for c3 in alphabet:
                        if c1 != c3 and c2 != c3:
                            # the last lines make it so we loop through all characters
                            # but only those where none of c1,c2,c3 refer to the same character

                            # these next few lines check the number of words where the three letters occur in order
                            # and if there's none for those characters, we log them
                            words = filterWords.wordsInOrder(c1,c2,c3)
                            if len(words) == 0:
                                f.write(c1 + " " + c2 + " " + c3 + "\n")
                                if(shouldPrint):
                                    print(c1,c2,c3)
    

if __name__ == "__main__":
    allWordsInOrder(True)
else:
    allWordsInOrder(False)
