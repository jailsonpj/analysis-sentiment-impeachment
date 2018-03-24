
from twython import Twython
APP_KEY ="QR5fsBnBCqD3Rda6szBchJCdW"
APP_SECRET = "13FYl5BN0QGd43X1qNhMPSZrjH2Virgo7uHKREv3aKPO3tmBKL"
OAUTH_TOKEN = "231448840-l12SVUES8llIvk136fktswGHUvCOl6UbYCW5CLz7"
OAUTH_TOKEN_SECRET = "vJpuj4jvzKA7DhyQmucxfWRntyF4jDMvDhEmM0EfiTntG"


twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN,
    OAUTH_TOKEN_SECRET)

results = twitter.cursor(twitter.search, q='impeachment')
for result in results:
    print(result)