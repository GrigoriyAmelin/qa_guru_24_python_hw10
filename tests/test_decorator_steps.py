import allure
from allure_commons.types import Severity
from selene import browser, by, have


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'gamelin')
@allure.feature('Задачи в репозитории')
@allure.story('Пользователь может найти репозиторий через строку поиска')
@allure.link('https://github.com', name='Testing')
@allure.title('Тест на основе шагов c декораторами')
def test_open_issue_tag_with_decorator_steps():
    open_main_page()
    search_repository('qa_guru_24_python_hw9')
    open_repository('qa_guru_24_python_hw9')
    open_issue_tag()
    assert_issue_tag_is_open_with_text('No results')

@allure.step('Открыть главную страницу github.com')
def open_main_page():
    browser.open('/')

@allure.step('В поисковой строке ввести название искомого репозитория')
def search_repository(search_text):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys(search_text).submit()

@allure.step('Перейти по найденной ссылке')
def open_repository(link_search_text):
    browser.element(by.partial_link_text(link_search_text)).click()

@allure.step('Открыть вкладку Issues')
def open_issue_tag():
    browser.element('[data-content="Issues"]').click()

@allure.step('Проверка открытой вкладки Issues')
def assert_issue_tag_is_open_with_text(text_to_check_on_tag):
    browser.element('.blankslate-heading').should(have.exact_text(text_to_check_on_tag))
