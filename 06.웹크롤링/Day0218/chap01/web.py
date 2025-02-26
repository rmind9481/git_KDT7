from urllib.request import urlopen

html = urlopen('https://www.daangn.com/hot_articles')

print(type(html))
print()
print(html.read())