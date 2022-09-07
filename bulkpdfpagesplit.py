#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

# assign directory

input_Folder_Location = r'C:\Users\hnagavelli\Downloads\MountAnalysis_Example_Docs'
output_Folder_Location = r'C:/Users/hnagavelli/Downloads/MountAnalysis_Example_Docs/1PageDocs/'
No_of_pages = 1

# iterate over files in
# that directory

for filename in os.listdir(input_Folder_Location):
    f = os.path.join(input_Folder_Location, filename)

    # checking if it is a file

    if os.path.isfile(f):
        print (f)
        input_pdf = PdfFileReader(f)
        output = PdfFileWriter()
        output.addPage(input_pdf.getPage(0))
        with open(output_Folder_Location+os.path.basename(f), "wb") as output_stream:
            output.write(output_stream)
       
