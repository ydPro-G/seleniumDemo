from selenium import webdriver
import os
os.chdir('E:\\strong')

wb = webdriver.Chrome()

wb.get('https://www.soundonsound.com/sound-advice/glossary-technical-terms?amp')


filename = 'a.txt'
with open(filename, 'w') as web_strong:
    elements = wb.find_elements_by_tag_name('strong')
    for element in elements:
        web_strong.write(element.text + '\n')


# python strong_string.py > output.txt
