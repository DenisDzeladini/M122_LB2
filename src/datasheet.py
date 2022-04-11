from mailmerge import MailMerge
from docx2pdf import convert
import os

datasheet_template_path = 'datasheet/Datasheet Template.docx'
datasheet_template = MailMerge(datasheet_template_path)
print(datasheet_template.get_merge_fields())


def populate_datasheet(price):
    datasheet_template.merge(
        Title='Datasheet Template',
        Price='Bitcoin Price: ' + price)
    datasheet_template.write('datasheet/Datasheet.docx')
    convert('datasheet/Datasheet.docx', 'datasheet/Datasheet.pdf')
    os.remove('datasheet/Datasheet.docx')
