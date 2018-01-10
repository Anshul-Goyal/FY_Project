from nytimesarchive import ArchiveAPI
from goose import Goose
from requests import get

api = ArchiveAPI('20fbb215e7d1461492487529241dd216')

term = open("terms.txt", "r")
lines = term.read().split('\n')

for year in range(2006,2007):
	for month in range(1,13):
		head = ""
		article = ""
		count = 1
		text_file = open("./headlines/headline" + str(year) + str(month) + ".txt", "w")
		text_file_arti = open("./articles/article"+ str(year) + str(month) + ".txt", "w")
		print(str(year) + str(month))
		value = api.query(year, month)
		val = value['response']['docs']
		for v in val:
			for l in lines:
				try:
					if l.lower() in v['headline']['main'].lower():
						head += (str(count) +  " " + v['pub_date'][0:10] + " " + v['headline']['main'] + '\n')
						response = get(v['web_url'])
						extractor = Goose()
						article1 = extractor.extract(raw_html=response.content)
						text = article1.cleaned_text
						if text == "":
							article = article + (str(count) + " " + v['pub_date'][0:10] + " " + v['snippet'] + '\n')
						else:
							article = article + (str(count) + " " + v['pub_date'][0:10] + " " + (text.encode('utf-8').strip()).decode('utf-8').strip() + '\n')
						print(str(count))
						count = count + 1
						break
				except:
					pass
		text_file.write((head).encode('utf-8').strip())
		text_file_arti.write((article).encode('utf-8').strip())
		text_file.close()
		text_file_arti.close()
