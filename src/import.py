import scipy 
import numpy as np  
import re  
import nltk  
from sklearn.datasets import load_files

#nltk.download('stopwords')
#nltk.download('wordnet')
import pickle  
from nltk.corpus import stopwords  


#Execute the following script to see load_files function in action:

movie_data = load_files(r"G:\4th year CSE\2nd Term\Database\DBproject\txt_sentoken")  
X, y = movie_data.data, movie_data.target  

##for i in range(0,3):
##    print(y[i])
##    print(X[i])
##    print("\n\n")

##we will remove all the special characters, numbers,
##and unwanted spaces from our text. Execute the following script
##to preprocess the data:
##    

documents = []
def remove_special_chars():
    from nltk.stem import WordNetLemmatizer

    stemmer = WordNetLemmatizer()

    for sen in range(0, len(X)):  
        # Remove all the special characters
        document = re.sub(r'\W', ' ', str(X[sen]))

        # remove all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

        # Remove single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document) 

        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)

        # Removing prefixed 'b' as the data is in byte format
        #so data is preceed by a 'b' char 
        document = re.sub(r'^b\s+', '', document)

        # Converting to Lowercase
        document = document.lower()

        # Lemmatization
        document = document.split()

        document = [stemmer.lemmatize(word) for word in document]
        document = ' '.join(document)

        documents.append(document)    


remove_special_chars()
#########################################################################################

#convert text into num using bag of words
def convert_to_num(X):
    from sklearn.feature_extraction.text import CountVectorizer  
    vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7,
                                 stop_words=stopwords.words('english'))  
    X = vectorizer.fit_transform(documents).toarray()
    return X

X = convert_to_num(X)
#print(X.shape())


##To convert values
##obtained using the bag of words model into TFIDF values, execute the following script:
####################################################################################333

def convert_to_TFIDF(X):
    from sklearn.feature_extraction.text import TfidfTransformer  
    tfidfconverter = TfidfTransformer()  
    X = tfidfconverter.fit_transform(X).toarray()  
    return X

X = convert_to_TFIDF(X)
#print(X)
print("done converting X to RFIDF %d" %len(X))

##Note:
##You can also directly convert text documents into TFIDF feature values
##(without first converting documents to bag of words features) using the following script:

##from sklearn.feature_extraction.text import TfidfVectorizer  
##tfidfconverter = TfidfVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))  
##X = tfidfconverter.fit_transform(documents).toarray()  


########################################################################3
# training and testing
#1- split data 
#divides data into 20% test set and 80% training set.
from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)  

