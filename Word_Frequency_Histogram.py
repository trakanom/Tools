#import a text file and parse how many times each word was used in the text
import sys
def main(filename=None):
    #open the file
    file = open("Resume.txt" if filename is None else filename, "r")
    #create a dictionary to store the words and their counts
    word_count = {}
    #read the file
    for line in file:
        #split the line into words
        words = line.split()
        #loop through the words
        for word in words:
            #if the word is in the dictionary
            word = word.lower()
            #strip the word of punctuation
            word = word.strip(".,;:!?()[]{}")
            if word.lower() in word_count:
                #increment the count
                word_count[word] += 1
            #if the word is not in the dictionary
            else:
                #add the word to the dictionary
                word_count[word] = 1
    #print the dictionary
    #Order the dictionary by the number of times the word was used
    
    word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    #for each time a word was used, print the word and a character to represent the number of times it was used
    for word, count in word_count:
        print(word, "\n\t"+"⬛"*count) #TODO normalize to a maximum count
    
    # print(word_count)
    #close the file
    file.close()
#if the file is run directly, pick up any arguments. If no argument, run the main function with a parameter of None
arg = sys.argv[1] if len(sys.argv) > 1 else None
main(arg)
