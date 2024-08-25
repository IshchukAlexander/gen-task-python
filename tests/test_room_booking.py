import pytest
from pages.main_page import Main


@pytest.mark.regression
class TestRoomBooking:
    def test_user_book_2_night_room(self, browser):
        m = Main(browser)
        m.user_book_room(17, 19)
