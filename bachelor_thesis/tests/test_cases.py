from browsermobproxy import Server
from selenium import webdriver
import json
import time


class TestCasesAndCreateHAR():

    def __init__(self, mob_path):
        self.browser_mob = mob_path
        self.server = self.driver = self.proxy = None

    @staticmethod
    def __store_har_file(title, result):
        har_file = open(title + '.har', 'w')
        har_file.write(str(result))
        har_file.close()

    def __start_server(self):
        self.server = Server(self.browser_mob)
        self.server.start()
        self.proxy = self.server.create_proxy()

    def __start_driver(self):
        """ Firefox driver"""
        """
        profile = webdriver.FirefoxProfile()
        profile.set_proxy(self.proxy.selenium_proxy())
        self.driver = webdriver.Firefox(firefox_profile=profile)
        """

        """ Chrome driver """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--proxy-server={0}".format(self.proxy.proxy))
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        """ Opera driver """
        """
        opera_options = webdriver.ChromeOptions()
        opera_options.binary_location = '/usr/bin/opera'
        opera_options.add_argument("--proxy-server={0}".format(self.proxy.proxy))
        self.driver = webdriver.Opera(opera_options=opera_options)
        """

    def start_all(self):
        self.__start_server()
        self.__start_driver()

    def create_har(self, title, url):
        """start request and parse response"""
        self.proxy.new_har(title)
        self.driver.get(url)
        time.sleep(60)
        result = json.dumps(self.proxy.har, ensure_ascii=False)
        self.__store_har_file(title, result)

    def stop_all(self):
        """stop server and driver"""
        self.server.stop()
        self.driver.quit()

    def main(self):
        url = 'http://bachelor.dev/'

        # cases = ['http2/push', 'html_5/load/auto', 'html_5/load/metadata', 'html_5/load/none', 'html_5/fetch', 'javascript/client_loop?1', 'javascript/ajax', 'favicon', 'websocket']
        cases = ['websocket']

        for case in cases:
            name = case.replace("/", "-")
            self.start_all()
            self.create_har(name, url + case)
            self.stop_all()


if __name__ == '__main__':
    path = "Path/to/BrowserMob_Proxy"

    RUN = TestCasesAndCreateHAR(path)
    RUN.main()
