import json
import sys

def main():

    tweet_file = open(sys.argv[1])
    data = []
    for line in tweet_file:
       data.append(json.loads(line))
    
	hash_list = []
    for i in range(len(data)):
        tweet = data[i]
        if len(tweet) > 1 :
            tweet = data[i]['entities']					#Parse the entities field of each tweet 
            hashtag = tweet['hashtags']					#Parse the hashtags field and store it hashtag variable
            
            if len(hashtag)>0:							#Filter out the tweets with the empty hashtag field
                for i in range(0,len(hashtag)):					#Check whether a single tweet has multiple hashtags
                    tag = hashtag[i]['text'].encode('utf-8')	#Store the text of the hash tag in the variable tag	
                    hash_list.append(tag)						#Append the tag variable to the list hash_list
     

    hash_dict = {}										#Initialize a new dictionary to store the hashtags and their frequencies
    for i in hash_list:
        if i in hash_dict.keys():						
            hash_dict[i] = hash_dict[i]+1
        else :
            hash_dict[i] = 1
    sorted_hash_list = []
    
    for w in sorted(hash_dict, key=hash_dict.get,reverse=True)[0:10]:			#Sort the hashtags dictionary by frequency and get the top ten hashtags
        print str(w), float(hash_dict[w]) 


if __name__ == '__main__':
    main()
