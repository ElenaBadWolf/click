import time


class RegistHelper:
    def __init__(self, app):
        self.app = app

    def registration_individual(self):
        wd = self.app.wd
        wd.get("https://ssp.clickadu.com/#/app/auth/signUp")
        wd.find_element_by_css_selector(
            ".signup__form >div:nth-child(1)>div>label:nth-child(1)").click()
        self.contact_info()
        self.ad_details()

    def registration_company(self):
        wd = self.app.wd
        wd.get("https://ssp.clickadu.com/#/app/auth/signUp")
        wd.find_element_by_css_selector(
            ".signup__form >div:nth-child(1)>div>label:nth-child(2)").click()
        wd.find_element_by_id("companyName").send_keys("Company Name")
        wd.find_element_by_id("_value").send_keys("Russian Federation")
        wd.find_element_by_id("address").send_keys("Tverskaya street")
        self.contact_info()
        self.ad_details()

    def contact_info(self):
        wd = self.app.wd
        wd.find_element_by_id("firstName").send_keys("Name")
        wd.find_element_by_id("lastName").send_keys("Last Name")
        wd.find_element_by_id("_value").send_keys("Russian Federation")
        wd.find_element_by_id("city").send_keys("Moscow")
        wd.find_element_by_id("address").send_keys("Tverskaya street")
        wd.find_element_by_id("email").send_keys("gqmznxoz@emlpro.com")
        wd.find_element_by_name("messengerNickname").send_keys("test")
        wd.find_element_by_id("signupSubmit").click()
        time.sleep(1)

    def ad_details(self):
        wd = self.app.wd
        wd.find_element_by_id("companyBudget").send_keys("500")
        wd.find_element_by_css_selector(
            "#companyTargetCountries .input").send_keys("Russian Federation")
        wd.find_element_by_id("website").send_keys("https://test.com")
        wd.find_element_by_id("companyDesc").send_keys(
            "Short description of your advertising campaign")
        wd.find_element_by_id("acceptTerms").click()
        wd.find_element_by_id("signupAction").click()
        time.sleep(5)
        status = wd.find_element_by_css_selector(".title.title_size-1").text
        if "Please activate your account" not in status:
            raise Exception("There is no message about activation account")
        time.sleep(5)

    def black_list(self):
        wd = self.app.wd
        wd.get("https://ssp.clickadu.com/#/app/auth/signUp")
        wd.find_element_by_css_selector(
            ".signup__form >div:nth-child(1)>div>label:nth-child(1)").click()
        wd.find_element_by_id("firstName").send_keys("Name")
        wd.find_element_by_id("lastName").send_keys("Last Name")
        wd.find_element_by_id("_value").send_keys("Afghanistan")
        wd.find_element_by_id("city").send_keys("Moscow")
        wd.find_element_by_id("address").send_keys("Tverskaya street")
        wd.find_element_by_id("email").send_keys("blacklist@test.test")
        wd.find_element_by_name("messengerNickname").send_keys("test")
        wd.find_element_by_id("signupSubmit").click()
        wd.find_element_by_css_selector(".form-group__input-errors").click()
        status = wd.find_element_by_css_selector(
            ".form-group__input-error").text
        if "Unfortunately our service isn't available in your country" \
                not in status:
            raise Exception("There is no message about chosen country")

    def registration_europe(self):
        wd = self.app.wd
        wd.get("https://ssp.clickadu.com/#/app/auth/signUp")
        wd.find_element_by_css_selector(
            ".signup__form >div:nth-child(1)>div>label:nth-child(1)").click()
        wd.find_element_by_id("firstName").send_keys("Name")
        wd.find_element_by_id("lastName").send_keys("Last Name")
        wd.find_element_by_id("_value").send_keys("Belgium")
        wd.find_element_by_id("city").send_keys("Bruges")
        wd.find_element_by_id("address").send_keys("Bilkske")
        wd.find_element_by_css_selector("#vatExist .checkbox").click()
        wd.find_element_by_id("email").send_keys("europe@test.test")
        wd.find_element_by_name("messengerNickname").send_keys("test")
        wd.find_element_by_id("signupSubmit").click()
        self.ad_details()
