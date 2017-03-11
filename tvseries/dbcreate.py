from tvseries.models import Serie
import requests


data = requests.get('http://api.tvmaze.com/shows')
tasks = data.json()

for task in tasks:
	try:
		newpost = Serie(
			title=task['name'],
			country=task['network']['country']['name'],
			tvpartners=task['network']['name'],
			language=task['language'],
			summary=task['summary'],
			premiered=task['premiered'],
			runtime=task['runtime'],
			genres=task['genres'],
			status=task['status'],
			image_med=task['image']['medium'],
			image_org=task['image']['original'],
			imdblink='http://www.imdb.com/title/%s' %task['externals']['imdb'],
			raiting=task['rating']['average']
			)
		newpost.save()
	except Exception as e:
		print(e)	
