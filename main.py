import pyttsx3
import PyPDF2

#Adding my book to the program's folder
book = open('yourbook.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
#This is a nice to have in case you wanna know the total number of pages your PDF has.
page = pdfReader.numPages
print(page)

#Starting with the audiobook
voice = pyttsx3.init()
#In order to read all pages we set a loop avoiding the filler pages and setting the initial page
for num in range(12, page):
    page = pdfReader.getPage(num)
    text = page.extractText()
    voice.say(text)
    #Start to Finish
    voice.runAndWait()