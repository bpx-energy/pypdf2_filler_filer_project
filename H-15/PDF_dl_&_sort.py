#! python3
# mark.nations@bpx.com
'''
This is going to be a short program that puts the pdf's
in my downloads into folders sorted by date
'''
import os
from datetime import datetime

#this is a variable to hold our dowloads ghpath
downloads = r'C:\Users\mark.nations\Downloads'

#This makes our directory the downloads folder
os.chdir(downloads)

#This is a list of the contents of the downloads foler as strings
DL_folder_contents = os.listdir()

#this creates a folder in the downloads with the named for the current date
today = datetime.now()
folder_title = today.strftime("%m-%d-%Y")
os.makedirs(folder_title)


def move_files():
    #this is going to be a function that tranfers the pdfs into the dated folder
    for file in DL_folder_contents:
        if file.lower().endswith('pdf'):
            current = downloads + '\\' + file
            new = downloads + '\\' + folder_title + '\\' + file
            os.rename(current, new)


move_files()