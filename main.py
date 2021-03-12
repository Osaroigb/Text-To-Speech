# import required modules
from playsound import playsound
import requests
import PyPDF2

# create a pdf file object
with open(file="outline.pdf", mode="rb") as pdfFileObj:

    # create a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(stream=pdfFileObj, strict=False)

    # get the number of pages in pdf file
    number_of_pages = pdfReader.numPages

    page_content = ""

    for n in range(number_of_pages):

        # create a page object for each page
        pageObj = pdfReader.getPage(n)

        # extract text from page
        page_content += pageObj.extractText()


# request parameters
parameters = {
    "key": "55f65527fff94400995b608b2278cbff",
    "src": page_content[:21],  # only the first three words in the pdf file because the API has a character limit
    "hl": "en-gb",
    "v": "Nancy",
    "r": 0,
    "c": "WAV",
    "f": "48khz_16bit_stereo"
}

# http GET request to convert textual content to speech
response = requests.get(url="http://api.voicerss.org/", params=parameters)
response.raise_for_status()

binary_data = response.content

# write and save binary data in an audio file
with open(file="speech.wav", mode="wb") as audio_file:

    audio_file.write(binary_data)

# play the audio file
playsound(sound="speech.wav")
