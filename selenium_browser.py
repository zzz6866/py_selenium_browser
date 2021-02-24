import argparse
import logging
import os

from selenium import webdriver
from selenium.webdriver.remote.remote_connection import LOGGER


class SeleniumBrowser:
    """
    Selenim Chrome Init
    크롬으로 파싱을 위한 초기화
    """
    options = webdriver.ChromeOptions()  # chromedriver option 설정

    def __init__(self, debug_mode=False):
        if debug_mode:  # debug : false
            self.options.add_argument('--headless')  # CLI 리눅스 사용을 위한 옵션 추가
            self.options.add_argument('--no-sandbox')  # CLI 리눅스 사용을 위한 옵션 추가
            self.options.add_argument('--disable-dev-shm-usage')  # CLI 리눅스 사용을 위한 옵션 추가
        # 크롬 창 사이즈
        # self.options.add_argument("--window-size=1000,500")

        # 파일 다운로드 설정
        self.options.add_experimental_option('prefs', {
            'download.default_directory': DOWNLOAD_DIR,
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            'safebrowsing.enabled': True
        })
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])  # DevTools log message disable

        self.driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=self.options)


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CHROMEDRIVER_PATH = BASE_DIR + r"\chromedriver"  # 프로그램 경로
    DOWNLOAD_DIR = BASE_DIR + r"\download"

    LOGGER.setLevel(logging.INFO)  # selenium log level

    parser = argparse.ArgumentParser()

    parser.add_argument('--debug-mode', action='store_true')
    args = vars(parser.parse_args())

    DEBUG_MODE = args['debug_mode']

    chromedriver = SeleniumBrowser(DEBUG_MODE).driver
    chromedriver.get('https://www.google.com')
    chromedriver.close()
