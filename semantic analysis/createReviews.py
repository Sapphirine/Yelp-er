import json

data = []
with open('/home/naman/Downloads/yelp_dataset_challenge_academic_dataset/code/yelp_academic_dataset_review.json') as f:
    for line in f:
        data.append(json.loads(line))


categories = []
locations = {}

i = 0

for d in data:
    i= i+1;
    if i > 10000:
        break;
    review_id = d.get('review_id')
    text = d.get('text')
    text = text.replace('\n','. ');
    try:
        nfile = open('review/' + review_id, 'w+')
        nfile.write(text);
    except UnicodeError:
        print 'a'

