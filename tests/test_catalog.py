from pages.CatalogPage import CatalogPage
from pages.elements.MainMenu import MainMenu


def test_catalog(browser, url):
    main_menu_page = MainMenu(browser, url)
    main_menu_page.browser.get(url)
    main_menu_page.click_tablet_menu_item()
    catalog_page = CatalogPage(browser, url)
    catalog_page .verify_tablets_title()
    catalog_page .should_be_greed_view_button()
    catalog_page .should_be_list_view_button()
    catalog_page.should_be_select_for_items_limit()
    catalog_page .should_be_select_for_sort_by()