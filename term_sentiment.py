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

    new_terms = {}								#Define an empty dict to store the tweet terms not found in AFINN-111.txt
    
    for i in range(len(data)):
        tweet = data[i]							#Tokenize each tweet metadata
        if len(tweet) > 1 :						#Filter out the tweets with the text field empty
            tweet_word = data[i]["text"].split()			#Tokenize each tweet and split the text field of the tweet by word 
            score = 0
            for word in tweet_word:
                if word.encode('utf-8') in scores.keys():	#Look up each token in the scores dict	
                    score = score + float(scores[word])		#If the term matches, assign the term score and calculate the total score of each tweet	
                else:
                    score = score
            #print score                
            for word in tweet_word:
                if word.encode('utf-8') not in scores.keys():		#Look up each token which is not present in the scores dict
                    n_w_score = float(score)						#Define a variable that would contain the tweet score
                    if word.encode('utf-8') in new_terms.keys():		#Check whether the term is present in the new_terms dict
                        new_terms[word.encode('utf-8')] = new_terms[word.encode('utf-8')] + n_w_score		
                    else:
                        new_terms[word.encode('utf-8')] = n_w_score                   

    for w in new_terms:
        print w, new_terms[w]								#Print the new terms and their scores

    
if __name__ == '__main__':
    main()
