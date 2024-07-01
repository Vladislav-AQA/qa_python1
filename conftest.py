import pytest
from main import BooksCollector

@pytest.fixture
def books_collector():
    book = BooksCollector()

    return books_collector