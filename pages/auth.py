from playwright.sync_api import Page, expect

class Auth:
    def __init__(self, page):
        self.enterEmailtextBox = page.get_by_role("textbox", name="Enter mobile number or email")
        self.continueBtn =  page.get_by_role("button", name="Continue")
        self.password =  page.get_by_role("textbox", name="Password")
        self.signInBtn = page.get_by_role("button", name="Sign in")
        self.incorrectPw = page.get_by_text("Your password is incorrect")


    def enterEmail(self,userEmail):
         self.enterEmailtextBox.fill(userEmail)


    def clickOnContinueBtn(self):
        self.continueBtn.click()

    def fillPw(self,userPw):
         self.password.fill(userPw)

    def signInBtn(self):
         self.signInBtn.click()

    def validateIncorrectPwMsg(self):
         expect(self.incorrectPw).to_be_visible()