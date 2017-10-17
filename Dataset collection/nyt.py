from nytimesarchive import ArchiveAPI
api = ArchiveAPI('20fbb215e7d1461492487529241dd216')
text_file = open("Output.txt", "w")
term = open("terms.txt", "r")	
count = 47955
lines = term.read().split('\n')
head = ""

for year in range(2010,2015):
	for i in range(1,13):
		print(str(year) + str(i))
		value = api.query(year, i)
		val = value['response']['docs']
		for v in val:
			for l in lines:
				try:
					if l.lower() in v['headline']['main'].lower():
						head += (str(count) + " " + v['headline']['main'] + '\n')
						count = count + 1
				except:
					pass

text_file.write(str(head))
text_file.close()