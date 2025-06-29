from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name,expected', [
        ('Книга с нормальным названием', True),
        ('', False),  # пустое название
        ('x'*41, False),  # слишком длинное название (41 символ)
        ('x'*40, True)  # пограничное значение (40 символов)
    ])
    def test_add_new_book_name_validation(self, name, expected):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert (name in collector.books_genre) == expected

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Мгла')
        collector.set_book_genre('Мгла', 'Ужасы')
        assert collector.books_genre['Мгла'] == 'Ужасы'

    def test_set_book_genre_invalid(self):
        collector = BooksCollector()
        collector.add_new_book('Мгла')
        collector.set_book_genre('Мгла', 'Несуществующий жанр')
        assert collector.books_genre['Мгла'] == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Фантастика')
        result = collector.get_books_with_specific_genre('Фантастика')
        assert len(result) == 2
        assert 'Книга 1' in result
        assert 'Книга 2' in result

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Детская книга')
        collector.add_new_book('Взрослая книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        collector.set_book_genre('Взрослая книга', 'Ужасы')
        result = collector.get_books_for_children()
        assert 'Детская книга' in result
        assert 'Взрослая книга' not in result

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Избранная книга')
        collector.add_book_in_favorites('Избранная книга')
        assert 'Избранная книга' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.add_book_in_favorites('Книга')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert 'Книга 1' in favorites
        assert 'Книга 2' in favorites

    def test_get_book_genre_nonexistent(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_add_duplicate_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дубликат')
        collector.add_new_book('Дубликат')
        assert len(collector.books_genre) == 1