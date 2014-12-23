import json
from itertools import groupby
from collections import Counter

data = []
with open('yelp_academic_dataset_user.json') as f:
    for line in f:
        data.append(json.loads(line))


print data[2]

allUserInfo = {}

for d in data:
	temp = {}
	temp['review_count'] = d.get('review_count')
	temp['yelping_since'] = d.get('yelping_since')
	temp['compliments'] = len(d.get('compliments'))
	temp['fans'] = d.get('fans')
	temp['friends'] = len(d.get('friends'))
	temp['votes'] = int(d.get('votes').get('funny')) + int(d.get('votes').get('cool')) + int(d.get('votes').get('useful'))
	allUserInfo[d.get('user_id')] = temp

#print allUserInfo.get('0vscrHoajVRa1Yk19XWdwA')

allFanCounts = []
allReviewCounts = []
allYelpingSince = []
allComplimentsCount = []
allFriends = []
allVotes = []

for user in allUserInfo.keys():
	temp = allUserInfo.get(user)
	allFanCounts.append(temp.get('fans'))
	allReviewCounts.append(temp.get('review_count'))
	allYelpingSince.append(temp.get('yelping_since'))
	allComplimentsCount.append(temp.get('compliments'))
	allFriends.append(temp.get('friends'))
	allVotes.append(temp.get('votes'))

maxFans = max(allFanCounts)
maxReviews = max(allReviewCounts)
maxCompliments = max(allComplimentsCount)
maxFriends = max(allFriends)
maxVotes = max(allVotes)

print maxVotes
print maxFriends
print maxCompliments
print maxReviews
print maxFans

for user in allUserInfo.keys():

	temp = allUserInfo.get(user)
	fans = temp.get('fans')
	votes = temp.get('votes')
	reviews = temp.get('review_count')
	compliments = temp.get('compliments')
	friends = temp.get('friends')
	yelpingSince = temp.get('yelping_since')

	#number of fans is high -> popular
	if fans>(2/3)*maxFans:
		if 'tags' not in temp:
			temp['tags'] = []
		temp.get('tags').append('Popular')

	year = int(yelpingSince.split('-')[0])
	month = int(yelpingSince.split('-')[1])

	#print yelpingSince, year, month
	yearsItHasBeen = 2014 - year

	#if the user is only 6 months old ->newbie
	if yearsItHasBeen==0:
		monthsItHasBeen = 12 - month
	
		if monthsItHasBeen<6:
			if 'tags' not in temp:
				temp['tags'] = []
			temp.get('tags').append('Newbie')


	#number of reviews is low and yelping since is old -> lazybones
	if reviews<(yearsItHasBeen):
		if 'tags' not in temp:
			temp['tags'] = []
		temp.get('tags').append('Lazybones')

	#number of reviews is more than 1 per year -> super active
	if reviews>24*(yearsItHasBeen):
		if 'tags' not in temp:
			temp['tags'] = []
		temp.get('tags').append('Super Active')

	print temp.get('tags')

	#number of votes is high -> dependable
	if votes>maxVotes/5:
		if 'tags' not in temp:
			temp['tags'] = []
		temp.get('tags').append('Dependable')

	#high number of friends -> social
	if friends>maxFriends/5:
		if 'tags' not in temp:
			temp['tags'] = []
		temp.get('tags').append('Social')

	allUserInfo[user] = temp
	print temp.get('tags')







#    print group
