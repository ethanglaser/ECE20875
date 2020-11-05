import string
import nltk
import nltk.tokenize as tk
    

#Input: words -- a list of words, including some words that might be punctuation
#Output: list of words *without* the words that might be punctuation
def remove_punc(words) :
    nltk.download("punkt")

    return [w for w in words if w not in string.punctuation]
    
if __name__ == "__main__" :
    
    teststring = "Tyger Tyger, burning bright, In the forests of the night; What immortal hand or eye, Could frame thy fearful symmetry?"
    words = tk.word_tokenize(teststring)
    
    print(words)
    
    print(remove_punc(words))
