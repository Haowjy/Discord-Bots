import json
import time
import feedparser

readinglist = 'https://www.scribblehub.com/rssfeed.php?type=global&uid=8363&unq=5cb7da71c7a88'
myfeed = feedparser.parse(readinglist)
print(myfeed.entries[0].title)
print(myfeed.entries[0].published)
timestamp = time.mktime(myfeed.entries[0].published_parsed)

user = {"discord_id": 193715976938717184,"feeds":[(readinglist,timestamp)]}
print(json.dumps(user, indent=2))

with open('data.txt', 'w') as outfile:
    json.dump(user, outfile)