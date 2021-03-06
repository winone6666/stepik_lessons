from final.pages.product_catalog_page import ProductCatalogPage

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"


class TestUserFindProduct:
    def test_user_can_find_book(self, browser):
        # Arrange
        page = ProductCatalogPage(browser, link)
        page.open()
        # Act
        page.should_be_catalog_page()
        # Assert
        page.should_be_find_special_product("The shellcoder's handbook")

    def test_user_can_see_not_found_info(self, browser):
        # Arrange
        page = ProductCatalogPage(browser, link)
        page.open()
        # Act
        page.should_be_catalog_page()
        # Assert
        page.should_be_not_found_product_info("@#$%")