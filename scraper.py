import scraperwiki
import lxml.html

html = scraperwiki.scrape("https://www.sdlauctions.co.uk/property-list/")

root = lxml.html.fromstring(html)
root.cssselect("li p a")
matchedlinks=root.cssselect("li p a")
print(matchedlinks)

record = {}

for li in matchedlinks[:20]:
  listtext = li.text_content()
  print(listtext.encode('utf-8'))
  record['address'] = listtext
  record['link']="https://www.sdlauctions.co.uk"+li.attrib['href']
  scraperwiki.sqlite.save(['address'],record)
  
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
