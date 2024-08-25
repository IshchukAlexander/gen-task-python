from playwright.sync_api import Page
from data.environment import host
from playwright.sync_api import expect
from pages.base import Base


class Assertions(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def check_URL(self, uri, msg):
        expect(self.page, msg).to_have_url(f"{host.get_base_url()}{uri}", timeout=10000)


    def have_text(self, locator, text: str, msg):
        loc = self.page.locator(locator)
        expect(loc, msg).to_have_text(text)


    def check_presence(self, locator, msg):
        loc = self.page.locator(locator).nth(0)
        expect(loc, msg).to_be_visible(visible=True, timeout=12000)


    def check_absence(self, locator, msg):
        loc = self.page.locator(locator)
        expect(loc, msg).to_be_hidden(timeout=700)


    def check_url_content(self, uri,msg):
        assert f"{uri}" in self.page.url, msg

    def contain_text(self, locator, text: str, msg):
        loc = self.page.locator(locator)
        expect(loc, msg).to_contain_text(text)
