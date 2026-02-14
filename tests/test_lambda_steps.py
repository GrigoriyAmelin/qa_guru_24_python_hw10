import allure
from selene import browser, by, have


def test_open_issue_tag_with_labda_steps():
    with allure.step('Открыть главную страницу github.com'):
        browser.open('/')

    with allure.step('В поисковой строке ввести название искомого репозитория'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').send_keys('qa_guru_24_python_hw9').submit()

    with allure.step('Перейти по найденной ссылке'):
        browser.element(by.partial_link_text('qa_guru_24_python_hw9')).click()

    with allure.step('Открыть вкладку Issues'):
        browser.element('[data-content="Issues"]').click()

    with allure.step('Проверка открытой вкладки Issues'):
        browser.element('.blankslate-heading').should(have.exact_text('No results'))