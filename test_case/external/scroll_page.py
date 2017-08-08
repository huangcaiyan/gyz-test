
class ScrollPage:
    def setUp(self, driver):
        self.driver = driver

    def scroll_top():
        js = 'var q = document.body.scrollTop=0'
        return self.driver.execute_script(js)

    def scroll_foot():
        js = 'var q = document.body.scrollTop=10000'
        return self.driver.execute_script(js)
