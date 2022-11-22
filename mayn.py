import json
#import yaml
import csv

from pprint import pprint

countries = [
	{'name':'Russia'},
	{'name':'USA'},
]

with open('example_save.json','w') as example_save:
	json.dump(countries,example_save)

with open('example_save.json') as exampl_load:
	move = json.load(exampl_load)
	pprint(move)

with open('(Заполненный)Список направлений к Реестру ГК 713 ф1.csv') as csvfile:
	country_reader = csv.reader(csvfile,delimiter=';')
	for row in country_reader:
		pprint (row[4])