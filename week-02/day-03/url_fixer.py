# Accidentally I got the wrong URL for a funny subreddit. It's probably "odds" and not "bots"  # nopep8
# Also, the URL is missing a crutial component, find out what it is and insert it too!  # nopep8

url = "https//www.reddit.com/r/nevertellmethebots"

url = url.replace('bots', 'odds')
url = url[:5] + ":" + url[5:]
print(url)
