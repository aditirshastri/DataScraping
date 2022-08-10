
from newspaper import Article



url = input('Enter url of a substack article: ')
article = Article(url)
article.download()
article.parse()
print(article.text)


