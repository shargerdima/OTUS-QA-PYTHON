from pages.MainPage import MainPage


def test_main_page(browser, url):
    main_page = MainPage(browser, url)
    main_page.open_browser()
    main_page.verify_logo_store()
    main_page.should_be_input_search()
    main_page.should_be_top_navbar()
    main_page.should_be_search_button()
    main_page.should_be_button_cart()