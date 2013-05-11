import sys
import json
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

	
def main():
    sent_file = open("AFINN-111.txt")
    tweet_file = open("tweets.txt")
    data = []
    for line in tweet_file:
       data.append(json.loads(line))
    print data[0]["text"].split()
    scores = {}
    for line in sent_file:
        term,score = line.split("\t")
        scores[term]=float(score)
    for i in range(len(data)):
        tweet_word = data[i]["text"].split()
        print tweet_word
        sent_score = 0
        for word in tweet_word:
            if word.encode('utf-8') in scores.keys():
                sent_score = sent_score + float(scores[word])
            else:
                sent_score = sent_score
    print float(sent_score)

if __name__ == '__main__':
    main()
