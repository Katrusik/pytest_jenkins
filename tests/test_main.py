import pytest
import allure

class TestMain:

    @allure.feature('Фича - Главный тест')
    @allure.story('Стори - Главный тест')
    @allure.title('Заголовок - Главный тест')
    def test_main(self, get_name):
        name = get_name
        with allure.step(f'Проверить имя: {name}'):
            assert 'Test' == 'Test'
