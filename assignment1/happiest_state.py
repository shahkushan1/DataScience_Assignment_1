import json
import sys
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
    us_tweets = {}
    for i in range(len(data)):
        tweet = data[i]
        if len(tweet) > 1 :
            place = data[i]['place']
            if place != None: 
                if place['country_code'] == 'US':
                    tweet_word = data[i]["text"].split()
                    sent_score = 0
                    for word in tweet_word:
                        if word.encode('utf-8') in scores.keys():
                            sent_score = sent_score + float(scores[word])
                        else:
                            sent_score = sent_score
                    state = place['full_name'][-2:].encode('utf-8')
                    if state in us_tweets.keys():
                        us_tweets[state]= us_tweets[state] +sent_score
                    else:
                        us_tweets[state] = sent_score
    
    for w in sorted(us_tweets, key=us_tweets.get,reverse=True)[0:1]:
        print w     
    

if __name__ == '__main__':
    main()
