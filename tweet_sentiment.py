import sys
import json
	
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    data = []									#Define an empty dict to store the tweets
    for line in tweet_file:
       data.append(json.loads(line))			#Parse the JSON input tweet file linewise
    
    scores = {}									#Define an empty dict to store the Sentiment of each term appearing in the AFINN-111.txt
    for line in sent_file:
        term,score = line.split("\t")			#Tab delimit the file AFIN-111.txt
        scores[term]=float(score)				#Assign each term the relevant score from the file mentioned above
    
    for i in range(len(data)):
        tweet = data[i]							#Tokenize each tweet metadata
        if len(tweet) > 1 :						#Filter out the tweets with the text field empty
            tweet_word = data[i]["text"].split()				#Tokenize each tweet and split the text field of the tweet by word 
            score = 0
            for word in tweet_word:
                if word.encode('utf-8') in scores.keys():		#Look up each token in the scores dict	
                    score = score + float(scores[word])			#If the term matches, assign the term score and calculate the total score of each tweet	
                else:
                    score = score
            print(score)
          
if __name__ == '__main__':
    main()
