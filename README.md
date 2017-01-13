# twitter-data-collector
This scripts collects trending data for a specific country (based on woeid) and save this data it to mongo db

  1. Make Sure mongo db is up & running on your env.
  2. install tweepy lib - pip install tweepy
  3. install pymongo lib - pip install pymongo
  4. update your twitter credentials in config.py
  5. update woeid for a country/city for which you want to extract trending data, By default it will fetch for india
