from playwright.sync_api import Page, expect

from utils.allure_steps import test_step


class Auth:
    def __init__(self, page):
        self.enterEmailtextBox = page.get_by_role("textbox", name="Enter mobile number or email")
        self.continueBtn =  page.get_by_role("button", name="Continue")
        self.password =  page.get_by_role("textbox", name="Password")
        self.signInBtnLocator = page.get_by_role("button", name="Sign in")
        self.incorrectPw = page.get_by_text("Your password is incorrect")

    def enterEmail(self,userEmail):
        with test_step("enterEmail"):
            self.enterEmailtextBox.fill(userEmail)

    def clickOnContinueBtn(self):
        with test_step("clickOnContinueBtn"):
            self.continueBtn.click()

    def fillPw(self,userPw):
        with test_step("fillPw"):
            self.password.fill(userPw)

    def signInBtn(self):
        with test_step("signInBtn"):
            self.signInBtnLocator.click()
         
    def validateIncorrectPwMsg(self):
        with test_step("validateIncorrectPwMsg"):
            expect(self.incorrectPw).to_be_visible()