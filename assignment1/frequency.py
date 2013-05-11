import sys
import json

def main():
    tweet_file = open(sys.argv[1])
    data = []
    for line in tweet_file:
       data.append(json.loads(line))
    
    term_freq = {}

    for i in range(len(data)):
        tweet = data[i]
        if len(tweet) > 1 :
            tweet_word = data[i]["text"].split()
            for word in tweet_word:
                if word.encode('utf-8') in term_freq.keys():					#Build up a term frequency dict
                    term_freq[word.encode('utf-8')] = term_freq[word.encode('utf-8')] + 1
                else :
                    term_freq[word.encode('utf-8')] = 1
    total = sum(term_freq.values())
    

    for key in term_freq.keys():
        freq = term_freq[key]/float(total)
        print key+' '+str(round(freq,6)) 

if __name__ == '__main__':
    main()
