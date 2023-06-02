import click
import requests

@click.command()
@click.argument('query')
def searchdatabooks(query):
  
    url = 'https://openlibrary.org/search.json'
    params = {'q': query}
    response = requests.get(url, params=params)
    data = response.json()

    # Extract relevant book information
    books = data.get('docs', [])
    for book in books:
        title = book.get('title', '')
        author = ', '.join(book.get('author_name', []))
        print("Title: " + title)
        print("Author(s): " + author)

        print("---")

if __name__ == '__main__':
    searchdatabooks()

