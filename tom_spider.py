import requests
from lxml import etree
import html2text as ht

text_maker = ht.HTML2Text()

url = 'https://www.cnblogs.com/TomXu/archive/2011/12/15/2288411.html'

r = requests.get(url)
HTML = etree.HTML(r.text)

all_a = HTML.xpath('//*[@id="cnblogs_post_body"]/p//a')

arr = []

for i in all_a:
    arr.append(
        {
            'name': i.xpath('text()')[0],
            'href': i.xpath('@href')[0]
        }
    )
for i in arr:
    r = requests.get(i['href'])
    HTML = etree.HTML(r.text)
    all_a = HTML.xpath('//div[@id="cnblogs_post_body"]')
    md = etree.tostring(all_a[0], encoding='utf-8', pretty_print=True, method='html').decode("utf-8")
    print(md)
    with open(f"./html/{i['name']}.md", 'w+', encoding='utf-8') as f:
        #
        text = text_maker.handle(md)
        f.write(text)
