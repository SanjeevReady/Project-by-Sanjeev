import nltk

nltk.download('punkt')  
nltk.download('averaged_perceptron_tagger')  

import nltk


def tag_parts_of_speech(user):
    
    tokens = nltk.word_tokenize(user)
    
    
    tagged_tokens = nltk.pos_tag(tokens)
    
    return tagged_tokens
user= input("write your sentence here:")


if __name__ == "__main__":
    sentence = "user."
    print(sentence)
    tagged = tag_parts_of_speech(user)
    print(tagged)
