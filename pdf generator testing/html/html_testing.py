from xhtml2pdf import pisa             # import python module

# Define your data
source_html = ""
html_file = "html/demo.html"
output_filename = "html/test.pdf"

def read_from_file():
    file = open(html_file, "r")
    html_string = file.read()
    return html_string

def write_to_file(string):
    file = open(html_file, "a")
    file.write(string)
    file.close()

# Utility function
def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    source_html = read_from_file()

    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file)           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err

# Main program
if __name__ == "__main__":
    pisa.showLogging()
    convert_html_to_pdf(source_html, output_filename)
