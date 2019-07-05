#coding:utf-8
import PyPDF2
import sys
from selenium import webdriver
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
class pdf_translate():
    def __init__(self):
        #print(args[1])
        self.FILE_PATH  = '/Users/hosokawa/Documents/paper/1705.07962.pdf'
        #self.FILE_PATH = args[1]


    def file_open(self):
        with open(self.FILE_PATH , mode = 'rb') as f:
            render = PyPDF2.PdfFileReader(f)
            for page in render.pages:
                print(str(type(page)))
                print(page.extractText())
                #print(str(page.extractText()))

    def make_driver(self , path):
        self.driver = webdriver.Chrome()
        self.driver.get(path)

    def



if __name__ == '__main__':
    args = sys.argv
    if 2 == len(args):
        #instance = pdf_translate()
        #instance.file_open()
        input_path = "/Users/hosokawa/Documents/paper/1705.07962.pdf"
        output_path = "/Users/hosokawa/Documents/paper/out.txt"
        rsrcmgr = PDFResourceManager()
        codec = 'utf-8'
        params = LAParams()
        with open(output_path, "wb") as output:
            device = TextConverter(rsrcmgr, output, codec=codec, laparams=params)
            with open(input_path, 'rb') as input:
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                for page in PDFPage.get_pages(input):
                    interpreter.process_page(page)
            device.close()
    else:
        print("[Error]")
        print("Usage : python main.py 'FILE_PATH'")
