def return_infile():
    from PyPDF2 import PdfFileReader
    infile = "C:\\Users\\\mark.nations\\Desktop\\H-15\\h15.pdf"
    pdf = PdfFileReader(open(infile, "rb"), strict=False)
    fields = pdf.getFields()
    return PdfFileReader, fields, infile, pdf

PdfFileReader, fields, infile, pdf = return_infile()

