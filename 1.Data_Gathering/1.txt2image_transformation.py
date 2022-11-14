# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 21:49:37 2022

@author: msara
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


#import os
import time
import sys
import pandas as pd

import tkinter as tk
from tkinter import filedialog

def open_url(driver, address,outFile):
    print(f'Started \t {outFile}')
    try:
        driver.get(address)
        driver.set_window_size(1920, 1080)  # to set the screenshot width
        save_screenshot(driver, outFile)
    except:
        print(f'Failed downloading \t {outFile}')

def save_screenshot(driver, file_name):
    height, width = scroll_down(driver)
    driver.set_window_size(width, height)
    driver.get_screenshot_as_file(file_name)
    print(f"Screenshot saved for \t {file_name}")

def scroll_down(driver):
    total_width = driver.execute_script("return document.body.offsetWidth")
    total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
    viewport_width = driver.execute_script("return document.body.clientWidth")
    viewport_height = driver.execute_script("return window.innerHeight")

    rectangles = []

    i = 0
    while i < total_height:
        ii = 0
        top_height = i + viewport_height

        if top_height > total_height:
            top_height = total_height

        while ii < total_width:
            top_width = ii + viewport_width

            if top_width > total_width:
                top_width = total_width

            rectangles.append((ii, i, top_width, top_height))

            ii = ii + viewport_width

        i = i + viewport_height

    previous = None
    #part = 0

    for rectangle in rectangles:
        if not previous is None:
            driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
            time.sleep(0.5)
        # time.sleep(0.2)

        if rectangle[1] + viewport_height > total_height:
            offset = (rectangle[0], total_height - viewport_height)
        else:
            #offset = (rectangle[0], rectangle[1])

            previous = rectangle

    return total_height, total_width

#%% Main program starts here
if __name__== "__main__":
    root = tk.Tk()
    root.withdraw()

    outPath = filedialog.askdirectory(title='Select the directory to save output files')
    
    if not outPath:
        print('No output path specified. Exiting..')
        sys.exit()
        
    filePath = filedialog.askopenfilename(title='Select the input csv file', filetypes=(("csv files","*.csv"),("All files","*.*")))
    if not filePath:
        print('No input file')
        sys.exit()
    inptFile = filePath
    
    # SELENIUM SETUP
    options = Options()
    options.binary_location = r'D:\FirefoxPortable\App\Firefox64\firefox.exe'
    driver =webdriver.Firefox(options=options)
    #driver =webdriver.Firefox()
    driver.implicitly_wait(2)
    driver.maximize_window()
    
    urlsList = pd.read_csv(inptFile)
    #urlsList['outFileName'] = urlsList.agg('{outPath}/{0[rec_id]}.PNG'.format, axis=1)
    urlsList['outFileName'] = outPath + '/' + urlsList['rec_id'].astype(str) + '.PNG'
    print(urlsList['outFileName'])
    for index, row in urlsList.iterrows():
        open_url(driver,row['url'], row['outFileName'])
        
    driver.quit()