import pytest
from main import BooksCollector

class TestBookCollector:

    def test_add_new_book(self):
        book.add_new_book('Буратино')
        assert len(book.get_books_genre()) == 1

    def test_set_book_genre_check_book_in_books_genre(self):
       book.add_new_book('Буратино')
       book.set_book_genre('Буратино', 'Мультфильмы')
       assert 'Буратино' and 'Мультфильмы' in book.books_genre == {'Буратино': 'Мультфильмы'}

    def test_get_book_genre(self):
        book.add_new_book('Буратино')
        book.set_book_genre('Буратино', 'Мультфильмы')
        assert book.books_genre.get('Буратино') == 'Мультфильмы'

    def test_get_books_with_specific_genre_true(self, genre):
        book.add_new_book('Буратино')
        book.set_book_genre('Буратино', 'Мультфильмы')
        assert book.books_genre and genre in book.genre == True

    def test_get_books_with_specific_genre_false(self, genre):
        book.add_new_book('Буратино')
        book.set_book_genre('Буратино', 'Сказка')
        assert book.books_genre and genre not in book.genre == True

    def test_get_books_genre(self):
        book.add_new_book('Буратино')
        book.set_book_genre('Буратино', 'Мультфильмы')
        assert book.get_books_genre() == {'Буратино': 'Мультфильмы'}

    @pytest.mark.parametrize('genre_age_rating', ['Ужасы', 'Детективы'])
    def test_get_books_for_children(self, genre_age_rating):
        book.add_new_book('Буратино')
        book.set_book_genre('Буратино', 'Мультфильмы')
        assert book.genre not in book.genre_age_rating == True

    def test_add_book_in_favorites(self):
        book.add_new_book('Буратино')
        book.add_book_in_favorites('Буратино')
        assert len(book.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        book.add_book_in_favorites('Буратино')
        book.delete_book_from_favorites('Буратино')
        assert len(book.get_list_of_favorites_books()) == 0

