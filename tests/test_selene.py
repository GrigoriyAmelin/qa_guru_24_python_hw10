from selene import browser, by, have


def test_open_issue_tag():
    browser.open('/')
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys('qa_guru_24_python_hw9').submit()
    browser.element(by.partial_link_text('qa_guru_24_python_hw9')).click()
    browser.element('[data-content="Issues"]').click()
    browser.element('.blankslate-heading').should(have.exact_text('No results'))
