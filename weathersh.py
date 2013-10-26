#!/usr/bin/env python
import json, urllib2, string, sys

class Color:
	HEADER = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	ENDC = '\033[0m'

def temp_color(temp):
	if temp < 32:
		return Color.BLUE
	elif 32 <= temp < 50:
		return Color.HEADER
	elif 50 <= temp < 79:
		return Color.GREEN
	elif 80 <= temp < 90:
		return Color.YELLOW 
	else:
		return Color.RED

def condition_color(cond):
	if cond == 'Rain':
		return Color.BLUE
	elif cond =='Fair':
		return Color.GREEN
	else:
		return Color.HEADER

location =  "'" + sys.argv[1] + "'"
woeidUrl = ("http://query.yahooapis.com/v1/public/yql?q="
						"select%20woeid%20"
						"from%20geo.places%20"
						"where%20text%3D{0}"
						"%20limit%201"
						"&format=json"
						).format(urllib2.quote(location))

woeidData = json.load(urllib2.urlopen(woeidUrl))
woeid = woeidData['query']['results']['place']['woeid']

weatherURL = ("http://query.yahooapis.com/v1/public/yql?q="
					    "select%20*%20"
					    "from%20weather.forecast%20"
					    "where%20woeid%3D2347597"
					    "&format=json")

data = json.load(urllib2.urlopen(weatherURL));
weather = data['query']['results']['channel']
current = weather['item']['condition']
forecast = weather['item']['forecast']

print "\nCurrently: {0}{1}{2}F and {3}{4}{5}.".format(
				temp_color(current['temp']), 
				current['temp'], 
				Color.ENDC, 
				condition_color(current['text']),
				current['text'], 
				Color.ENDC
			) 

print "Expected conditions: {0}{1}{2}{3}/{4}{5}F with conditions being {6}{7}{8}\n".format(
				temp_color(forecast[0]['high']),
				forecast[0]['high'],
				Color.ENDC,
				temp_color(forecast[0]['low']),
				forecast[0]['low'],
				Color.ENDC,
				condition_color(forecast[0]['text']),
				forecast[0]['text'],
				Color.ENDC
			)

for i in range(1, 5):
	print "{0} | {1}/{2}F {3}".format(
					forecast[i]['day'],
					forecast[i]['high'],
					forecast[i]['low'],
					forecast[i]['text']
				)








