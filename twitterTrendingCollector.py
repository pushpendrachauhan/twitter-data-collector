from config import api,india_woeid,mongo_twitter_db,mongo_trending_collection_name
import time

def isStartsWithHash(trendName):
	result=False
	if ((type(trendName) == str) or (type(trendName)== unicode)):
		result=trendName.startswith('#')
		return result

def removeHash(trendName):
	fixedString=trendName[1:]
	return fixedString

def getTimeInMillis():
	return int(round(time.time() * 1000))


def getTrendingDataFromTwitter():
	indiaTrend = api.trends_place(india_woeid)

	if indiaTrend:
		data = indiaTrend[0] 
		trends = data['trends']
		if trends:
			updatedTrendsList=[]
			for trend in trends:
				trendName=trend.get('name',None)
				if trendName:
					result=isStartsWithHash(trendName)

					if result:
						fixedTrendName=removeHash(trendName)
						if fixedTrendName:
							updatedTrendsList.append(fixedTrendName.lower())

					else:
						updatedTrendsList.append(trendName.lower())

			return updatedTrendsList


def saveTrendingToMongo(trendingList):
	try:
		if mongo_twitter_db:
			trendCollection=mongo_twitter_db[mongo_trending_collection_name]
			for trend in trendingList:
				mongoDataDict={}
				mongoDataDict['name']=trend
				mongoDataDict['timeStamp']=getTimeInMillis()
				trendCollection.insert(mongoDataDict)
			print "inserted to mongo successfully"
	except Exception as e:
		print "error in saving data to mongo"
		pass


if __name__=="__main__":
	trendingList=getTrendingDataFromTwitter()
	saveTrendingToMongo(trendingList)



	