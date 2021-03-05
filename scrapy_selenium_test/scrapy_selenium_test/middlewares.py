import json
from logging import getLogger

from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SeleniumDownloaderMiddleware(object):
    def __init__(self):
        self.logger = getLogger(__name__)
        self.timeout = 60
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("prefs",
                                                    {"profile.managed_default_content_settings.images": 2})  # 禁止图片
        # self.chrome_options.add_argument("--proxy-server=http://proxy.domain.cn:6666") # 加代理
        self.chrome_options.add_argument(
            'user-agent=' + 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36')
        self.chrome_options.add_argument('--headless')  # 无头模式
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

        self.d = DesiredCapabilities.CHROME
        self.d['loggingPrefs'] = {'performance': 'ALL'}
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options, desired_capabilities=self.d)
        # self.browser.set_window_size(1400, 700)
        self.browser.set_page_load_timeout(self.timeout)
        self.browser.set_script_timeout(self.timeout)
        # self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):
        """
        用selenium抓取页面
        :param request: Request对象
        :param spider: Spider对象
        :return: HTMLResponse
        """
        # self.logger.debug('Selenium is Starting')
        http_status_ignore = [521, 429]
        try:
            self.browser.get(request.url)
            http_status = self.getHttpStatus(self.browser)
            self.logger.info(f"{request.url} 我在这,http_status={http_status}")
            if str(http_status).startswith(('2', '3')) or http_status in http_status_ignore:
                return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                                    status=200)
            else:
                return HtmlResponse(url=request.url, status=500, request=request)
        except TimeoutException:
            # self.browser.execute_script('window.stop()')
            self.logger.info(f"{request.url} error了")
            return HtmlResponse(url=request.url, status=500, request=request)

    def getHttpStatus(self, browser):
        """
        获取http status
        :param browser: browser对象
        :return: 状态码or''
        """
        get_log = browser.get_log('performance')
        for responseReceived in get_log:
            try:
                response = json.loads(responseReceived['message'])['message']['params']['response']
                if response['url'] == browser.current_url:
                    return response['status']
            except:
                pass
        return ''
