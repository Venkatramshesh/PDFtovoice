# importing the modules
import PyPDF2
import pyttsx3

# path of the PDF file
path = open('C:/Users/venka/Python100days/PDFtovoice/VenkatRamsheshCV2022.pdf', 'rb')

# # creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)
#
# # the page with which you want to start

from_page = pdfReader.getPage(0)
#
# # extracting the text from the PDF
text = from_page.extractText()
#
# # reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()