from playwright.sync_api import Page, TimeoutError, Response
from data.environment import host


class Base:
    def __init__(self, page: Page):
        self.page = page

    def open(self, uri) -> Response | None:
        return self.page.goto(f"{host.get_base_url()}{uri}", wait_until='domcontentloaded')

    def click(self, locator: str) -> None:
        self.page.click(locator)

    def input(self, locator: str, data: str) -> None:
        self.page.locator(locator).fill(data)

    def get_text(self, locator: str, index: int) -> str:
        return self.page.locator(locator).nth(index).text_content()

    def wait_for_element(self, locator, timeout=12000) -> None:
        self.page.wait_for_selector(locator, timeout=timeout)

    def current_url(self) -> str:
        return self.page.url

    def click_by_text(self, text: str):
        self.page.get_by_text(text).click()

    def is_element_present(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator, timeout=10000)
        except TimeoutError as e:
            return False
        return True
    
    def is_element_visiable(self, locator: str) -> bool:
        return self.page.locator(locator).nth(0).is_visible()
        

    def drag_and_drop(self, source, target):
        self.page.drag_and_drop(source, target)

    def refresh(self) -> Response | None:
        return self.page.reload(wait_until='domcontentloaded')
