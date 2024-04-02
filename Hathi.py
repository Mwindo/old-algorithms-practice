from bs4 import BeautifulSoup
import requests
import re
import os
from pathlib import Path
from PyPDF2 import PdfFileMerger
import progressbar
import shutil


def PDFDownload(output_line):
    PDF_download = requests.get(output_line, stream=True, timeout=300)
    with open(path_folder + 'page' + str(actual_page) + '.pdf', 'wb') as f:
        f.write(PDF_download.content)


# Get hathitrust book link
link = "https://babel.hathitrust.org/cgi/pt?id=mdp.39015008633896"
id_book = re.findall('id=(\w*\.\d*)|$', link)[0]
r = requests.get(link)
soup = BeautifulSoup(r.text, "html.parser")

# Number of the book pages and name
pages_book = 424  # int(soup.find("span", {"data-slot": "total-seq"}).text)
name_book = soup.find('meta', {'property': 'og:title'})['content']

if len(name_book) > 55:
    name_book = name_book[:40]

print("1")

# Remove invalid characters
remove_character = "[],/\\:.;\"'?!*"
name_book = name_book.translate(
            str.maketrans(remove_character, len(remove_character)*" ")).strip()
print("2")
# Create a new folder
local = os.getcwd()
Path(local + "/" + name_book).mkdir(parents=True, exist_ok=True)
path_folder = local + "/" + name_book + "/"

# Download pdf file
begin_page = 1
last_page = pages_book + 1
print("3")

for actual_page in range(begin_page, last_page):
    print(actual_page)
    output_line = f"https://babel.hathitrust.org/cgi/imgsrv/image?id=mdp.39015008633896;seq={actual_page};size=225;rotation=0"
    r = requests.get(output_line, stream=True)
    r.raw.decode_content = True
    with open(path_folder + 'page' + str(actual_page), 'wb') as f:
        shutil.copyfileobj(r.raw, f)
    #output_line = f'https://babel.hathitrust.org/cgi/imgsrv/download/pdf?id={id_book};orient=0;size=100;seq={actual_page};attachment=0'
