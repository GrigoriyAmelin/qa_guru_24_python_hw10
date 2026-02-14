import allure
from allure_commons.types import Severity
from selene import browser, by, have


@allure.tag('web')
@allure.severity(Severity.TRIVIAL)
@allure.label('owner', 'gamelin')
@allure.feature('Задачи вне личного репозитория')
@allure.story('Пользователь может найти репозиторий через строку поиска')
@allure.link('https://github.com', name='Testing')
@allure.title('Тест без описания шагов')
def test_open_issue_tag():
    browser.open('/')
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys('qa_guru_24_python_hw9').submit()
    browser.element(by.partial_link_text('qa_guru_24_python_hw9')).click()
    browser.element('[data-content="Issues"]').click()
    browser.element('.blankslate-heading').should(have.exact_text('No results'))
