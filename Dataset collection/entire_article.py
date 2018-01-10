# import urllib
# from BeautifulSoup import BeautifulSoup

# link = "http://www.nytimes.com/2010/01/01/opinion/l01terror.html"
# print(link)
# f = urllib.urlopen(link)
# print(f)
# myfile = f.read()
# # print myfile
# VALID_TAGS = ['div', 'p']

# soup = BeautifulSoup(myfile)

# for tag in soup.findAll('p'):
#     if tag.name not in VALID_TAGS:
#         tag.replaceWith(tag.renderContents())

# print soup.renderContents()

from goose import Goose
from requests import get

response = get('https://query.nytimes.com/gst/fullpage.html?res=980DE7D7163EF932A05752C0A9669D8B63')
extractor = Goose()
article = extractor.extract(raw_html=response.content)
text = article.cleaned_text
print text