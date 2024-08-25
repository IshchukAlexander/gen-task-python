from pages.base import Base
from data.constants import Constants
from data.assertions import Assertions
from datetime import datetime
from playwright.sync_api import Page

class Main(Base):

    UNVAILABLE_ROW = "//div[@title='Unavailable']"
    MONTH_YEAR_HEADER = "//span[@class='rbc-toolbar-label']"

    BOOKING_FIRST_NAME_INPUT = "//input[@name='firstname']"
    BOOKING_LAST_NAME_INPUT = "//input[@name='lastname']"
    BOOKING_EMAIL_INPUT = "//input[@name='email']"
    BOOKING_PHONE_INPUT = "//input[@name='phone']"

    CONFIRM_BOOK_BUTTON = "//button[contains(text(),'Book')]"

    SUCCESS_BOOKING_POPUP_HEADER = "//h3[contains(text(),'Booking Successful!')]"


    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def find_available_month(self):
        self.click_by_text("Next")
        while self.is_element_visiable(self.UNVAILABLE_ROW):
            self.click_by_text("Next")
        return self.get_text(locator=self.MONTH_YEAR_HEADER, index=0)
    
    def choose_calendar_dates(self, start_day: int, end_day: int):
        self.page.locator(f'//button[contains(text(),"{start_day - 1}")]').hover()
        self.page.mouse.down()
        for i in range(start_day, end_day + 1):
            self.page.locator(f'//button[contains(text(),"{i}")]').hover()
        self.page.mouse.up()
    
    def user_book_room(self, start_day, end_day):
        self.open("")
        self.click_by_text("Book this room")
        actual_date = self.find_available_month()
        actual_date_start = datetime.strptime(str(start_day) + " " + actual_date, '%d %B %Y').strftime('%Y-%m-%d')
        actual_date_end = datetime.strptime(str(end_day) + " " + actual_date, '%d %B %Y').strftime('%Y-%m-%d')
        nights_count = end_day - start_day

        self.input(locator=self.BOOKING_FIRST_NAME_INPUT, data=str(Constants.first_name))
        self.input(locator=self.BOOKING_LAST_NAME_INPUT, data=str(Constants.last_name))
        self.input(locator=self.BOOKING_EMAIL_INPUT, data=str(Constants.email))
        self.input(locator=self.BOOKING_PHONE_INPUT, data=str(Constants.phone))
        self.choose_calendar_dates(start_day, end_day)

        self.assertion.check_presence(f'//div[@title="{nights_count} night(s) - £{nights_count * 100}"]', "Days/nights not selected on callendar or unavailable")
        self.click("//button[contains(text(),'Book')]")

        self.assertion.check_presence(self.SUCCESS_BOOKING_POPUP_HEADER, "Room not booked")
        self.assertion.check_presence(f'//p[contains(text(),"{actual_date_start}")]', "First night date incorrect")
        self.assertion.check_presence(f'//p[contains(text(),"{actual_date_end}")]', "Last night date incorrect")