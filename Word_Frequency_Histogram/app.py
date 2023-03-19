import sys

def main(filename=None):
    # Open the file
    file = open("Resume.txt" if filename is None else filename, "r")
    # Create a dictionary to store the words and their counts
    word_count = {}
    # Read the file
    for line in file:
        # Split the line into words
        words = line.split()
        # Loop through the words
        for word in words:
            # If the word is in the dictionary
            word = word.lower()
            # Strip the word of punctuation
            word = word.strip(".,;:!?()[]{}")
            if word.lower() in word_count:
                # Increment the count
                word_count[word] += 1
            # If the word is not in the dictionary
            else:
                # Add the word to the dictionary
                word_count[word] = 1
    
    # Order the dictionary by the number of times the word was used
    word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    # Normalize the output based on the maximum bar length
    MAX_BAR_LENGTH = 50
    max_count = max(word_count, key=lambda x: x[1])[1]
    normalization_factor = MAX_BAR_LENGTH / max_count

    # For each time a word was used, print the word and a character to represent the number of times it was used
    for word, count in word_count:
        normalized_count = int(count * normalization_factor)
        print(word, "\n\t" + "⬛" * normalized_count)

    # Close the file
    file.close()

# If the file is run directly, pick up any arguments. If no argument, run the main function with a parameter of None
arg = sys.argv[1] if len(sys.argv) > 1 else None
main(arg)
