from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from more_itertools import chunked
from os import makedirs


def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    makedirs('pages', exist_ok=True)
    for page_num, page_books_pairs in enumerate(books_pairs_split, 1):
        rendered_page = template.render(
            books_pairs=page_books_pairs,
            pages_quantity=pages_quantity,
            page_num=page_num
        )
        with open(f'pages/index{page_num}.html', 'w', encoding="utf8") as f:
            f.write(rendered_page)


def get_books():
    with open("books.json", "r") as file:
        books_json = file.read()
    parsed_books = json.loads(books_json)
    books_information = []
    for parsed_book in parsed_books:
        book = {
            'genres': parsed_book['genres'],
            'book_path': '../' + '/'.join(map(str, parsed_book['book_path'].split('/')[-2:])),
            'title': parsed_book['title'],
            'author': parsed_book['author'],
            'image_src': '../' + '/'.join(map(str, parsed_book['image_src'].split('/')[-2:]))
        }
        books_information.append(book)
    return books_information


if __name__ == '__main__':
    book_cards = get_books()
    chunk_size = 2
    books_pairs = list(chunked(book_cards, chunk_size))
    pairs_html = 10
    books_pairs_split = list(chunked(books_pairs, pairs_html))
    pages_quantity = len(books_pairs_split)

    on_reload()

    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.', default_filename='./pages/index1.html')
