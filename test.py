from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.nytimes.com")
headlines = driver.find_element_by_xpath("story-heading")
for headline in headlines:
    print(headline.text.strip())