from pathlib import Path
import borb.pdf as brb
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.canvas.layout.shape.shape import Shape
from borb.pdf.canvas.line_art.line_art_factory import LineArtFactory
from borb.pdf.canvas.layout.layout_element import Alignment
from decimal import Decimal
import csv
import json
import math

# create a dictionary
data = {}

# Decide the two file paths according to your
# computer system
csvFilePath = 'borb2/prototype2.csv'
jsonFilePath = 'borb2/prototype2.json'

# Open a csv reader called DictReader
with open(csvFilePath, encoding='utf-8') as csvf:
    csvReader = csv.DictReader(csvf)

    # Convert each row into a dictionary
    # and add it to data
    for row in csvReader:

        # Assuming a column named 'No' to
        # be the primary key
        key = row["No"]
        data[key] = row

# Open a json writer, and use the json.dumps()
# function to dump data
with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=4))

# create an empty Document
pdf = brb.Document()

# add an empty Page
page = brb.Page()
pdf.add_page(page)

# use a PageLayout (SingleColumnLayout in this case)
layout = brb.SingleColumnLayout(page)

row_nmb_float = math.ceil(len(data)/2)
row_nmb = int(row_nmb_float)
print("Rows: ", row_nmb)

# set padding on all (implicit) TableCell objects in the FixedColumnWidthTable
# top, right, bottom, left
table: brb.FixedColumnWidthTable = brb.FixedColumnWidthTable(number_of_columns=2, number_of_rows=row_nmb)

for row in data:
    data_string = ""

    for attribute in data[row].keys():
        data_string += attribute
        data_string += ": " + data[row][attribute] + "\n"

    #subtable: brb.FixedColumnWidthTable = brb.FixedColumnWidthTable(number_of_columns=2, number_of_rows=1)

    pic_path = Path("pictures/profile_pic.jpg")

    #table.add(brb.Image(
        #pic_path,
        #width=Decimal(128),        
        #height=Decimal(128)
    #))

    table.add(brb.Paragraph(
        data_string,
        respect_newlines_in_text=True
    ))

    
    
    #table.add(brb.Paragraph("Hello World!", horizontal_alignment=Alignment.CENTERED))
    #table.add(subtable)

if row_nmb*2 > len(data):
    print("Filling up empty table cell")
    table.add(brb.TableCell(brb.Paragraph(" "), border_color=brb.X11Color("White")))

table.set_padding_on_all_cells(Decimal(0), Decimal(0), Decimal(50), Decimal(0)).no_borders()

layout.add(table)      

#layout.add(sticky.add(brb.Paragraph("Hello World")))


# add a Paragraph object
#layout.add(brb.Paragraph("Hello World!"))

#layout.add(brb.Paragraph(str(data)))
    
# store the PDF
with open(Path("borb2/output2.pdf"), "wb") as pdf_file_handle:
    brb.PDF.dumps(pdf_file_handle, pdf)
