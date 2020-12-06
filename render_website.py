from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from more_itertools import chunked
from os import makedirs
from pathlib import PurePath, Path


def on_reload():
    for page_num, page_books_pairs in enumerate(books_pages, 1):
        rendered_page = template.render(
            books_pairs=page_books_pairs,
            pages_quantity=pages_quantity,
            page_num=page_num
        )
        with open(f'pages/index{page_num}.html', 'w', encoding="utf8") as f:
            f.write(rendered_page)


def get_books():
    with open("books.json", "r", encoding='utf-8') as file:
        books_json = file.read()
    parsed_books = json.loads(books_json)
    books_information = []
    for parsed_book in parsed_books:
        book_path_parts = PurePath(parsed_book['book_path']).parts
        book_path = Path('..', book_path_parts[0], book_path_parts[1])
        image_src_parts = PurePath(parsed_book['image_src']).parts
        image_src = Path('..', image_src_parts[0], image_src_parts[1])
        book = {
            'genres': parsed_book['genres'],
            'book_path': book_path,
            'title': parsed_book['title'],
            'author': parsed_book['author'],
            'image_src': image_src
        }
        books_information.append(book)
    return books_information


def remove_old_pages():
    for file in Path('./pages').glob('*.html'):
        try:
            file.unlink()
        except OSError:
            continue


if __name__ == '__main__':
    remove_old_pages()
    book_cards = get_books()
    chunk_size = 2
    books_pairs = list(chunked(book_cards, chunk_size))
    pairs_html = 10
    books_pages = list(chunked(books_pairs, pairs_html))
    pages_quantity = len(books_pages)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    makedirs('pages', exist_ok=True)

    on_reload()

    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.', default_filename='./pages/index1.html')
