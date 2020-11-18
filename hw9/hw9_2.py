import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 
from helper import remove_punc
import numpy as np


#Clean and stem the contents of a document
#Takes in a file name to read in and clean
#Return a list of words, without stopwords and punctuation, and with all words stemmed
# NOTE: Do not append any directory names to doc -- assume we will give you
# a string representing a file name that will open correctly
def readAndCleanDoc(doc) :
    #1. Open document, read text into *single* string
    with open(doc, 'r') as f:
        data = f.read()
    data = data.lower()
    #2. Tokenize string using nltk.tokenize.word_tokenize
    word_tokens = word_tokenize(data, language='english')
    #3. Filter out punctuation from list of words (use remove_punc)
    word_tokens = remove_punc(word_tokens)
    #4. Make the words lower case
    #word_tokens = word_tokens.lower()
    #5. Filter out stopwords
    stop_words = set(stopwords.words('english'))
    words = [w for w in word_tokens if not w in stop_words] 
    #6. Stem words
    ps = PorterStemmer()
    for index, w in enumerate(words): 
        words[index] = ps.stem(w)
    
    return words
    
#Builds a doc-word matrix for a set of documents
#Takes in a *list of filenames*
#
#Returns 1) a doc-word matrix for the cleaned documents
#This should be a 2-dimensional numpy array, with one row per document and one 
#column per word (there should be as many columns as unique words that appear
#across *all* documents. Also, Before constructing the doc-word matrix, 
#you should sort the wordlist output and construct the doc-word matrix based on the sorted list
#
#Also returns 2) a list of words that should correspond to the columns in
#docword
def buildDocWordMatrix(doclist) :
    #1. Create word lists for each cleaned doc (use readAndCleanDoc)
    wordlist = []
    wordlists = []
    for doc in doclist:
        rcd = readAndCleanDoc(doc)
        wordlists.append(rcd)
        wordlist += rcd
    wordlist = sorted(list(set(wordlist)))
    print(wordlist)
    #2. Use these word lists to build the doc word matrix
    docword = np.zeros((len(doclist), len(wordlist)))
    for index, wl in enumerate(wordlists):
        for word in wl:
            docword[index][wordlist.index(word)] += 1
    return docword, wordlist
    
#Builds a term-frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns a term-frequency matrix, which should be a 2-dimensional numpy array
#with the same shape as docword
def buildTFMatrix(docword) :
    sums = docword.sum(axis=1)
    print(sums)
    tf = docword / sums[:, np.newaxis]
    
    return tf
    
#Builds an inverse document frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns an inverse document frequency matrix (should be a 1xW numpy array where
#W is the number of words in the doc word matrix)
#Don't forget the log factor!
def buildIDFMatrix(docword) :
    #fill in
    idf = np.log10(len(docword) / np.sum(docword>0, axis=0)).reshape(1,-1)
    return idf
    
#Builds a tf-idf matrix given a doc word matrix
def buildTFIDFMatrix(docword) :
    #fill in
    tfidf = buildTFMatrix(docword) * buildIDFMatrix(docword)
    return tfidf
    
#Find the three most distinctive words, according to TFIDF, in each document
#Input: a docword matrix, a wordlist (corresponding to columns) and a doclist 
# (corresponding to rows)
#Output: a dictionary, mapping each document name from doclist to an (ordered
# list of the three most common words in each document
def findDistinctiveWords(docword, wordlist, doclist) :
    distinctiveWords = {}
    #fill in
    #you might find numpy.argsort helpful for solving this problem:
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html
    tfidf = buildTFIDFMatrix(docword)
    for index in range(len(doclist)):
        indices = np.argsort(tfidf[index])[-3:]
        distinctiveWords[doclist[index]] = [wordlist[indices[2]], wordlist[indices[1]], wordlist[indices[0]]]


    
    
    return distinctiveWords


if __name__ == '__main__':
    from os import listdir
    from os.path import isfile, join, splitext
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    ### Test Cases ###
    directory='lecs'
    path1 = join(directory, '1_vidText.txt')
    path2 = join(directory, '2_vidText.txt')
    
    # Uncomment and recomment ths part where you see fit for testing purposes
    print("*** Testing readAndCleanDoc ***")
    print(readAndCleanDoc(path1)[0:5])
    print("*** Testing buildDocWordMatrix ***") 
    doclist =[path1, path2]
    docword, wordlist = buildDocWordMatrix(doclist)
    print(docword.shape)
    print(len(wordlist))
    print(docword[0][0:10])
    print(wordlist[0:10])
    print(docword[1][0:10])
    print("*** Testing buildTFMatrix ***") 
    tf = buildTFMatrix(docword)
    print(tf[0][0:10])
    print(tf[1][0:10])
    print(tf.sum(axis =1))
    print("*** Testing buildIDFMatrix ***") 
    idf = buildIDFMatrix(docword)
    print(idf[0][0:10])
    print("*** Testing buildTFIDFMatrix ***") 
    tfidf = buildTFIDFMatrix(docword)
    print(tfidf.shape)
    print(tfidf[0][0:10])
    print(tfidf[1][0:10])
    print("*** Testing findDistinctiveWords ***")
    print(findDistinctiveWords(docword, wordlist, doclist))
