import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    data = []
    for line in tweet_file:
       data.append(json.loads(line))
    
    scores = {}
    for line in sent_file:
        term,score = line.split("\t")
        scores[term]=float(score)

    new_terms = {}
    
    for i in range(len(data)):
        tweet = data[i]
        if len(tweet) > 1 :
            tweet_word = data[i]["text"].split()
            score = 0
            for word in tweet_word:
                if word.encode('utf-8') in scores.keys():
                    score = score + float(scores[word])
                else:
                    score = score
            #print score                
            for word in tweet_word:
                if word.encode('utf-8') not in scores.keys():
                    n_w_score = float(score)
                    if word.encode('utf-8') in new_terms.keys():
                        new_terms[word.encode('utf-8')] = new_terms[word.encode('utf-8')] + n_w_score
                    else:
                        new_terms[word.encode('utf-8')] = n_w_score                   

    for w in new_terms:
        print w, new_terms[w]

    
if __name__ == '__main__':
    main()
