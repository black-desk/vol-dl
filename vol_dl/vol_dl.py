#!/usr/bin/env python3

"""
vol-dl - vol.moe manga downloader

Usage:
    vol-dl [-f format] [-d directory] <url> ...

Options:
    -h --help             Show this screen.
    --version             Show version.
    -f --format <format>  Specify format, "epub or mobi" [default: epub].
    -d --directory <dir>  Specify directory to save file [default: .].
"""

from .docopt import docopt
from selenium import webdriver

import time, os


def main():

    arguments = docopt(__doc__, version="vol-dl 0.1")

    urls = arguments["<url>"]
    path = arguments["--directory"]
    path = os.path.abspath(path)
    ext = arguments["--format"]

    divid = "div_cbz"

    options = webdriver.ChromeOptions()
    chrome_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": path}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.maximize_window()
    driver.get("https://vol.moe/login.php")
    driver.find_element_by_xpath('//input[@name="email"]').send_keys("814727823@qq.com")
    driver.find_element_by_xpath('//input[@name="passwd"]').send_keys("Rx3WafSsTVT1")
    driver.find_element_by_xpath('//button[contains(text(), "馬上登錄")]').click()
    time.sleep(5)

    for url in urls:
        print(url)
        driver.get(url)
        time.sleep(5)
        if ext == "epub":
            divid = "div_cbz"
        downloadBtns = driver.find_elements_by_xpath(
            "//div@id=" + divid + '/a[text()="下載"]'
        )
        cnt = 0
        for btn in downloadBtns:
            link = btn.get_attribute("href")
            driver.get(link)
            cnt += 1
            if cnt % 3 == 0:
                time.sleep(60 * 30)

