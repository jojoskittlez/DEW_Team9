# drawing_polygons.py
'''
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, PageBreak, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet
import random

def draw_shapes():
    doc = BaseDocTemplate('basedoc.pdf',showBoundary=1)

    words = "lorem ipsum dolor sit amet consetetur sadipscing elitr sed diam nonumy eirmod tempor invidunt ut labore et".split()

    styles=getSampleStyleSheet()
    Elements=[]

    c = canvas.Canvas("testing_output.pdf", pagesize=A4)
    c.setStrokeColorRGB(0.2, 0.5, 0.3)
    c.rect(50, 50, 100, 80, stroke=1, fill=0)
    c.ellipse(10, 680, 100, 630, stroke=1, fill=1)
    c.wedge(10, 600, 100, 550, 45, 90, stroke=1, fill=0)
    c.circle(300, 600, 50)
    c.save()

    #Two Columns
    

    #Elements.append(Paragraph(" ".join([random.choice(words) for i in range(1000)]),styles['Normal']))
    Elements.append(c)
   
    doc.addPageTemplates([PageTemplate(id='TwoCol',frames=[frame1,frame2]), ])

    #start the construction of the pdf
    doc.build(Elements)

if __name__ == '__main__':
    draw_shapes()
'''

'''
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Frame
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']
story = []

#add some flowables
story.append(Paragraph("This is a Heading",styleH))
story.append(Paragraph("This is a paragraph in <i>Normal</i> style.",
    styleN))
c  = Canvas('mydoc.pdf')

frame1 = Frame(inch, inch, inch, 6*inch, 9*inch, showBoundary=1, id='col1')
frame2 = Frame(inch, inch, 6*inch, 9*inch, showBoundary=1, id='col2')
#f = Frame(inch, inch, 6*inch, 9*inch, showBoundary=1)
#doc = SimpleDocTemplate('mydoc.pdf',pagesize = letter)
frame1.addFromList(story,c)
c.save()
#doc.build(story)
'''

"""
examples of reportlab document using
BaseDocTemplate with
2 PageTemplate (one and two columns)

"""
'''
import os
from tkinter import Canvas
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet


styles=getSampleStyleSheet()
Elements=[]

doc = BaseDocTemplate('basedoc.pdf',showBoundary=1)

def foot1(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',19)
    canvas.drawString(cm, 0.75 * cm, "Page %d" % doc.page)
    canvas.restoreState()
def foot2(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(cm, 0.75 * cm, "Page %d" % doc.page)
    canvas.restoreState()

#normal frame as for SimpleFlowDocument
frameT = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')

#Two Columns
print(doc.height)
columnWidth = 540
columnHeight = 697
yPosition = 117
spacing = 12
frame1 = Frame(cm, yPosition, columnWidth/2-spacing, columnHeight, id='col1')
frame2 = Frame(cm+columnWidth/2+spacing, yPosition, columnWidth/2-spacing, columnHeight, id='col2')

#Elements.append(Paragraph("Frame one column, "*500,styles['Normal']))
Elements.append(NextPageTemplate('TwoCol'))
#Elements.append(PageBreak())
Elements.append(Paragraph("Frame one column, "*500,styles['Normal']))
#Elements.append(NextPageTemplate('OneCol'))
#Elements.append(PageBreak())
#Elements.append(Paragraph("Une colonne",styles['Normal']))

frame1.addFromList(Elements, canvas)

#doc.addPageTemplates([#PageTemplate(id='OneCol',frames=frameT,onPage=foot1),
                      
                      #PageTemplate(id='TwoCol',frames=[frame1,frame2],onPage=foot2),
                      #])
#start the construction of the pdf
doc.build(Elements)
# use external program xpdf to view the generated pdf
#os.system("py -m xpdf basedoc.pdf")

'''

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table

from reportlab.lib.units import cm
from reportlab.graphics import shapes
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))

# setup your platypus document
pdf = SimpleDocTemplate("sample.pdf",
                        pagesize=A4,
                        rightMargin=1*cm,
                        leftMargin=1*cm,
                        topMargin=1*cm,
                        bottomMargin=1*cm)

# create your table from data
data = [
['a', 'b', 'c'],
['where I want to import rectangles', '', ''],
['some data', '', '']]

table = Table(data)

# draw your shapes and add to the platypus doc which is letter 8.5x11 inch
x = 0
y = 0
width = (18.5/2)*cm # object in points, so we multiply by inch (72 points)
height = (27/4)*cm # object in points, so we multiply by inch (72 points)
spacing = 0.5*cm

text_position = (width-spacing)/2-25

print(text_position)
elements = []

# Create your drawing with rectangle 
drawing = shapes.Drawing(width,height)
elements.append(shapes.Rect(x, y, width-spacing, height, fillColor=None, strokeColor=colors.black))
elements.append(shapes.Rect(width+spacing, y, width-spacing, height, fillColor=None, strokeColor=colors.black))
#sr = shapes.Rect((width-spacing)/2-50, y, (width-spacing)/2, height, fillColor=None, strokeColor=colors.blue)
elements.append(shapes.String(text_position, height-25, "Name", fontName="Vera", fontSize=10))
elements.append(shapes.String(text_position, height-50, "Apartment No. 1", fontName="Vera", fontSize=8))
elements.append(shapes.String(text_position, height-75, "Hobbies: Lorem, ipsum, dolor, sit, amet, consectetur, adipiscing, elit", fontName="Vera", fontSize=8))
# add the rectangle to your Drawing
#d.add(sr)
img_height = 75
elements.append(shapes.Image(x+20, height-img_height, img_height-20, img_height-20, "pictures/profile_pic.jpg"))

for element in elements:
    drawing.add(element)


# Setup your Story
Story = []
#Story.append(table)
# add the Drawing (i.e. the drawn rectangle) to the platypus doc
Story.append(drawing)

# Export to PDF
pdf.build(Story)
