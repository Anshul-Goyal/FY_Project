<<<<<<< HEAD
from nytimesarchive import ArchiveAPI
from goose import Goose
from requests import get
import csv

api = ArchiveAPI('20fbb215e7d1461492487529241dd216')

term = open("terms.txt", "r")
lines = term.read().split('\n')

for year in range(2013,2014):
	for month in range(4,13):
		head = ""
		article = ""
		count = 1
		with open("./headlines/headline" + str(year) + str(month) + ".csv", "wb") as csv_head,open("./articles/article" + str(year) + str(month) + ".csv", "wb") as csv_art:
			head_writer = csv.writer(csv_head,dialect='excel',delimiter=',',quoting=csv.QUOTE_ALL)
			art_writer = csv.writer(csv_art)
			print(str(year) + str(month))
			value = api.query(year, month)
			val = value['response']['docs']
			# print(val)
			for v in val:
				for l in lines:
					try:
						if l.lower() in v['headline']['main'].lower():
							# head += ( + '\n')
							response = get(v['web_url'])
							extractor = Goose()
							article1 = extractor.extract(raw_html=response.content)
							text = article1.cleaned_text
							if text == "":
								article = ("\'"+str(count) + "','" + v['pub_date'][0:10] + "','" + v['snippet']+"\'")
							else:
								article = ("\'"+str(count) + "','" + v['pub_date'][0:10] + "','" + (text.encode('utf-8').strip()).decode('utf-8').strip() + "\'")
							print("\'"+str(count) +  "','" + v['pub_date'][0:10] + "','" + v['headline']['main'] + "\'")
							head_writer.writerow(["\'"+str(count) +  "','" + v['pub_date'][0:10] + "','" + v['headline']['main'] + "\'"])
							art_writer.writerow([article])
							count = count + 1
							break
					except:
						pass
		# text_file.write((head).encode('utf-8').strip())
		# text_file_arti.write((article).encode('utf-8').strip())
		# text_file.close()
		# text_file_arti.close()
=======
from nytimesarchive import ArchiveAPI
from goose import Goose
from requests import get
import csv

api = ArchiveAPI('20fbb215e7d1461492487529241dd216')

term = open("terms.txt", "r")
lines = term.read().split('\n')

for year in range(2013,2014):
	for month in range(1,13):
		head = ""
		article = ""
		count = 1
		with open("./headlines/headline" + str(year) + str(month) + ".csv", "wb") as csv_head,open("./articles/article" + str(year) + str(month) + ".csv", "wb") as csv_art:
			head_writer = csv.writer(csv_head,dialect='excel',delimiter=',',quoting=csv.QUOTE_ALL)
			art_writer = csv.writer(csv_art)
			print(str(year) + str(month))
			value = api.query(year, month)
			val = value['response']['docs']
			# print(val)
			for v in val:
				for l in lines:
					try:
						if l.lower() in v['headline']['main'].lower():
							# head += ( + '\n')
							response = get(v['web_url'])
							extractor = Goose()
							article1 = extractor.extract(raw_html=response.content)
							text = article1.cleaned_text
							if text == "":
								article = ("\'"+str(count) + "','" + v['pub_date'][0:10] + "','" + v['snippet']+"\'")
							else:
								article = ("\'"+str(count) + "','" + v['pub_date'][0:10] + "','" + (text.encode('utf-8').strip()).decode('utf-8').strip() + "\'")
							print("\'"+str(count) +  "','" + v['pub_date'][0:10] + "','" + v['headline']['main'] + "\'")
							head_writer.writerow(["\'"+str(count) +  "','" + v['pub_date'][0:10] + "','" + v['headline']['main'] + "\'"])
							art_writer.writerow([article])
							count = count + 1
							break
					except:
						pass
		# text_file.write((head).encode('utf-8').strip())
		# text_file_arti.write((article).encode('utf-8').strip())
		# text_file.close()
		# text_file_arti.close()
>>>>>>> ddf08c3a851fe04553a721ad3bf59480d062d19f
