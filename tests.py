import pytest

from main import BooksCollector

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

    # проверяем, что книга существует в колекции и жанр является допустимым
    @pytest.mark.parametrize(
        'name,genre',
        [
            ('Гордость и предубеждение и зомби', 'Комедии'),
            ('Что делать, если ваш кот хочет вас убить', 'Мультфильмы')
        ]
    )
   
    def test_set_book_genre_two_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert name in collector.books_genre and collector.books_genre[name] == genre

    # проверяем, что по названию книги можно получить жанр
    @pytest.mark.parametrize(
        'name,genre',
        [
            ('Гордость и предубеждение и зомби', 'Комедии'),
            ('Что делать, если ваш кот хочет вас убить', 'Мультфильмы')
        ]
    )

    def test_get_book_genre_defining_a_genre_by_name(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        result = collector.get_book_genre(name)
        assert result == genre
 
    # проверяем, что книга без жанра 
    def get_book_genre_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга без жанра')
        result = collector.get_book_genre('Книга без жанра')
        assert result == ''
    
    # проверяем, что по жанру "Комедии" выводится всего 2 книги из 3-х
    def test_get_books_with_specific_genre_two_books_of_the_same_genre(self): 
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
    
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
    
        collector.add_new_book('Смешарики')
        collector.set_book_genre('Смешарики', 'Мультфильмы')

        result = collector.get_books_with_specific_genre('Комедии')
        assert len(result) == 2

    # проверяем, что в списке книг для детей не будет жанров из списка genre_age_rating
    def test_get_books_for_children_two_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Детективы')
    
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
    
        collector.add_new_book('Смешарики')
        collector.set_book_genre('Смешарики', 'Мультфильмы')

        result = collector.get_books_for_children()
        assert 'Смешарики' in result and \
       'Гордость и предубеждение и зомби' not in result and \
       'Что делать, если ваш кот хочет вас убить' not in result

    # проверяем, что книга есть в списке избранного
    def test_add_book_in_favorites_add_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == ['Гордость и предубеждение и зомби']

   # проверяем, что книга 'Что делать, если ваш кот хочет вас убить' удалена из списка избранного 
    def test_delete_book_from_favorites_delete_one_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.favorites == ['Гордость и предубеждение и зомби']

    # проверяем удаление книги, которой нет в списке избранного 
    def test_delete_book_from_favorites_delete_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        collector.delete_book_from_favorites('Книги нет в избранном') 
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']  
