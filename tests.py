import pytest
from main import BooksCollector


class TestBookCollector:

    def test_add_new_book(self):
        book = BooksCollector()
        book.add_new_book('Буратино')
        assert len(book.get_books_genre()) == 1


class TestBookCollector:

    def test_set_book_genre_check_book_in_books_genre(self):
       book = BooksCollector()
       book.add_new_book('Буратино')
       book.set_book_genre('Буратино', 'Мультфильмы')
       assert 'Буратино' in book.books_genre == {'Буратино': 'Мультфильмы'}

class TestBookCollector:
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_check_in_genre(self, genre):

        book = BooksCollector()
        book.add_new_book('Буратино')
        book.set_book_genre('Буратино', 'Мультфильмы')
        assert 'Мультфильмы' in book.genre == book.genre

class TestBookCollector:

    def test_get_book_genre(self):
        book = BooksCollector()
        book.add_new_book('Буратино')
        book.set_book_genre('Буратино', 'Мультфильмы')
        assert book.books_genre.get('Буратино') == 'Мультфильмы'

class TestBookCollector:

    def test_get_books_with_specific_genre(self):
        book = BooksCollector()
        book.add_new_book('Буратино')
        book.set_book_genre('Буратино', 'Мультфильмы')
        assert book.get_books_with_specific_genre('Мультфильмы') == ['Буратино']

class TestBookCollector:

    def test_get_books_genre(self):
        book = BooksCollector()
        book.add_new_book('Буратино')
        book.set_book_genre('Буратино', 'Мультильмы')
        book.books_genre['Буратино'] = book.genre
        assert book.get_books_genre() == {'Буратино': ''}

class TestBookCollector:
    @pytest.mark.parametrize('genre_age_rating', ['Ужасы', 'Детективы'])
    def test_get_books_for_children(self, genre_age_rating):
        book = BooksCollector()
        book.add_new_book('Буратино')
        book.set_book_genre('Буратино', 'Мультфильмы')
        assert book.genre not in book.genre_age_rating == book.genre_age_rating

class TestBookCollector:
   def test_add_book_in_favorites(self):
        book = BooksCollector()
        book.add_new_book('Буратино')
        book.add_book_in_favorites('Буратино')
        assert len(book.get_list_of_favorites_books()) == 1

class TestBookCollector:
    def test_delete_book_from_favorites(self):
        book = BooksCollector()
        book.add_book_in_favorites('Буратино')
        book.delete_book_from_favorites('Буратино')
        assert len(book.get_list_of_favorites_books()) == 0