#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
import pandas as pd
import re
import os

binary = FirefoxBinary("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
driver = webdriver.Firefox(firefox_binary = binary)

def links():
    df = pd.read_csv('links.txt')
    l = df['links'].values.tolist()
    return l

def read_data(fname):
    df = pd.read_csv(f'{fname}.txt', sep='|')
    r = df['Cat/Rat'].values.tolist()
    return r

def get_info():    
    rate_nums = driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/main/div/article/div[*]/div/div/div[1]/span')
    movie_names = driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/main/div/article/div[*]/div/div/div[2]/a[1]')
    post_by = driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/main/div/article/div[*]/div/div/div[2]/a[2]')
    views = driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/main/div/article/div[*]/div/div/div[2]/div[1]/span[1]')
    votes = driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/main/div/article/div[*]/div/div/div[2]/div[1]/span[2]')
    return rate_nums, movie_names, post_by, views, votes

def name(lista):
    n = ''
    for x in lista:
        n+=x
    return n

def k_to_num(v):
    kilo = 1000
    mile = 100000
    if v[-1] == 'K':
        value = round(float(v[:-1])*kilo)
    elif v[-1] == 'M':
        value = round(float(v[:-1])*mile)
    else: #int(v[-1]) in range(0,10):
        value = v
    return value

def delete_files():
    l = os.listdir()
    for x in l:
        if x.endswith('.txt'):
            if 'links' not in x or 'READ' not in x:
                os.remove(x)
        else:
            pass

def main():

    writer=pd.ExcelWriter('BookData.xlsx')
    scroll_num = 0
    link = links()
    for l in link:
        count = 0
        driver.get(l)
        category = l.split('/')[-2]
        with open(f'{category}.txt', 'w') as f:
            f.write('Cat/Rat|Category|Rating|Names|Post by|Views|Votes\n')
        while True:
            ra = read_data(category)
            rn, mn, pb, vi, vo = get_info()
            for x in range(len(rn)):
                lname = mn[x].text.split('|')
                nam = ''.join(name(lname).split('"'))
                lpb = pb[x].text.split('|')
                postby = name(lpb)
                #sredi da k bude 1000
                views = k_to_num(vi[x].text)
                votes = k_to_num(vo[x].text)
                catrat = f'{category}-{rn[x].text}'
                if catrat in ra:
                    pass
                else:
                    count+=1
                    if count > 1000:
                        break
                    else:
                        with open(f'{category}.txt', 'a') as f:
                            f.write(f"{catrat}|{category}|{rn[x].text}|{nam}|{postby}|{views}|{votes}\n")

                        print(f"{catrat}|{rn[x].text}|{nam}|{postby}|{views}|{votes}\n")
            scroll_num += 20000
            driver.execute_script('window.scrollTo(0, {});'.format(scroll_num))
            ranew = read_data(category)
            stopscroll=0
            '''
            if len(ra)==len(ranew):
                print('no new data')
                stopscroll+=1
            if stopscroll>5:
                print('Seemes that no more data to entry in this category, going to the next one')
                break
            '''
            sleep(3)
            print(f'+++++++++++++++COUNT NUMBER {count}++++++++++++++++')
            if count > 1000 or len(ra)==len(ranew):
                df = pd.read_csv(f'{category}.txt', sep='|')
                df.to_excel(writer, category)
                break

    writer.save()

main()
sleep(2)
driver.close()
print('Deleting unnecessary files')
delete_files()
print('Finished')
