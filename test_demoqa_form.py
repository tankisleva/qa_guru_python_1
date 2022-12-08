from selene.support.shared import browser
from selene import be, have, command
import os


def test_submit_positive():
    browser.open('/automation-practice-form').should(have.title("ToolsQA"))
    browser.element("#firstName").should(be.blank).should(have.attribute("placeholder", "First Name")).type("Oleg")
    browser.element("#lastName").should(be.blank).should(have.attribute("placeholder", "Last Name")).type("Malyshev")
    browser.element("input#userEmail").should(be.blank).should(have.attribute("placeholder", "name@example.com")).type("test@test.ru")
    browser.element('[for="gender-radio-1"]').click()
    browser.element("#userNumber").should(be.blank).should(have.attribute("placeholder", "Mobile Number")).type("1234567890")

    ads = browser.all('[id^=google_ads_][id$=container__]')
    ads.should(have.size_less_than_or_equal(3))
    ads.perform(command.js.remove)

    checkboxes = browser.elements(".custom-checkbox label")
    for checkbox in checkboxes:
        checkbox.click()

    browser.element(".react-datepicker__input-container").click()
    browser.element(".react-datepicker__month-select").click()
    browser.element("[value='4']").click()
    browser.element(".react-datepicker__year-select").click()
    browser.element("[value='1986']").click()
    browser.element("[class='react-datepicker__day react-datepicker__day--016']").click()
    browser.element("input#subjectsInput").should(be.blank).type("hello").press_enter()

    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'tests/6289.jpg')))
    browser.element("#currentAddress").should(be.blank).should(have.attribute("placeholder", "Current Address")).type("pirogova 5")
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Merrut').press_enter()
    browser.element("[id='submit']").should(be.clickable).click()
    browser.all(".modal-body tr td + td").should(have.texts("Oleg", "Malyshev", "test@test.ru", "Male", "1234567890",
                                                            "6 April,1986", "Hello", "Sports, Reading, Music", "image_2022-11-29_12-59-44.png",
                                                            "pirogova 5", "Uttar Pradesh Merrut"))




    # brows
    # browser.element(".react-datepicker__year-select").click().set(value=1986)





