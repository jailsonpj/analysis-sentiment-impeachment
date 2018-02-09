from twython import Twython
import pandas as pd

CONSUMER_KEY="QR5fsBnBCqD3Rda6szBchJCdW"
CONSUMER_SECRET="13FYl5BN0QGd43X1qNhMPSZrjH2Virgo7uHKREv3aKPO3tmBKL"

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET)
search = {}

#procura por tweets contendo a palavra python
for status in twitter.search(q='"python"')["statuses"]:
    user = status["user"]["screen_name"]
    text = status["text"]
    print(user,":",text)
    print()


'''for status in twitter.search(q='"presidio manaus"')["statuses"]:
    search = status

df = pd.DataFrame(search)
print(search)'''
