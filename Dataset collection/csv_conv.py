import csv
import re
import traceback

year = 2006
month = 1
for year in range(2006,2013):
	for month in range(1,13):
		with open("./articles_csv/article" + str(year) + str(month) + ".csv", "wb") as csv_art, open("HistoricalPrices.csv", "rb") as djia:
			values = list(csv.reader(djia, delimiter=',', quotechar='|'))
			art_writer = csv.writer(csv_art,dialect='excel',delimiter=',',quoting=csv.QUOTE_ALL)

			article_file = open("./articles/article" + str(year) + str(month) + ".txt", "r").read()
			count = 0
			article_file = article_file[2:]
			try:
				text = re.split('\n[0-9]{3}\s20|\n[0-9]{2}\s20|\n[0-9]\s20',article_file)
			except:
				traceback.print_exc()
			text[0] = text[0][2:]
			try:
				for i in range(len(text)):
					article =  "\'" + text[i] 
					article = article.replace(" ", "','",1)
					article = article.replace("\n", "")
					n=0
					for k in values:
						# print(k[0][0:2] + k[0][3:5] + k[0][6:8] + " " + article[1:3] + article[4:6] + article[7:9])
						if(article[1:3]==k[0][6:8]):
							if(article[4:6]==k[0][0:2]):
								if(article[7:9]==k[0][3:5]):
									print(k[4]+k[1])
									if(k[4]>k[1]):
										n=1
										
					article = article[:9] + ",'" + str(n) + article[9:] 
					article = article + "\'"
					
					art_writer.writerow([article])
					count = count+1
			except:
				traceback.print_exc()
