
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller

# Check if the current version of chromedriver exists
# and if it doesn't exist, download it automatically,
# then add chromedriver to path
chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions() 
options = [
    "--headless",
    "--disable-gpu",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)
    chrome_options.add_argument("--proxy-server=https://112.194.90.218:4231")

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.yun316.net/')
print(driver.title)







