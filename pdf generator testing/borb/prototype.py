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
csvFilePath = 'borb/prototype.csv'
jsonFilePath = 'borb/prototype.json'

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

# define size of sticky note
# horizontal, vertical
sticky_size = 170
r: Rectangle = Rectangle(Decimal(0), Decimal(0), Decimal(sticky_size*1.20), Decimal(sticky_size))
sticky: Shape = brb.Shape(
                    LineArtFactory.sticky_note(r),
                    stroke_color=brb.X11Color("Black"),
                    fill_color=brb.X11Color("White"),
                    line_width=Decimal(1),
                    horizontal_alignment=Alignment.CENTERED
                )

row_nmb_float = math.ceil(len(data)/2)
row_nmb = int(row_nmb_float)
print("Rows: ", row_nmb)

# set padding on all (implicit) TableCell objects in the FixedColumnWidthTable
# top, right, bottom, left
table: brb.FixedColumnWidthTable = brb.FixedColumnWidthTable(number_of_columns=2, number_of_rows=row_nmb)

for row in data:
    #brb.Paragraph("Hello World!", horizontal_alignment=Alignment.CENTERED).layout(page, r)
    table.add(sticky)

if row_nmb*2 > len(data):
    print("Filling up empty table cell")
    table.add(brb.TableCell(brb.Paragraph(" "), border_color=brb.X11Color("White")))

table.set_padding_on_all_cells(Decimal(0), Decimal(0), Decimal(50), Decimal(0)).no_borders()

layout.add(table)      

# add a Paragraph object
#layout.add(brb.Paragraph("Hello World!"))

#layout.add(brb.Paragraph(str(data)))
    
# store the PDF
with open(Path("borb/output.pdf"), "wb") as pdf_file_handle:
    brb.PDF.dumps(pdf_file_handle, pdf)
