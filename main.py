import PyPDF2
import sys
from selenium import webdriver

class pdf_translate():
    def __init__(self):
        #print(args[1])
        self.FILE_PATH  = '/Users/hosokawa/Documents/paper/1705.07962.pdf'
        #FILE_PATH = args[1]


    def file_open(self):
        with open(self.FILE_PATH , mode = 'rb') as f:
            render = PyPDF2.PdfFileReader(f)
            for page in render.pages:
                #print(str(type(page)))
                print(page.extractText())
                print(str(page.extractText()))

    def make_driver(self , path):
        driver = webdriver.Chrome()
        driver.get(path)




if __name__ == '__main__':
    args = sys.argv
    if 2 == len(args):
        instance = pdf_translate()
        instance.file_open()
    else:
        print("Error")
        print("Usage : python main.py 'FILE_PATH'")
