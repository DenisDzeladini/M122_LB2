import ftplib
import datetime
from mailmerge import MailMerge
from docx2pdf import convert
import os
import mailtrap as mt

datasheet_template = MailMerge('datasheet/Datasheet Template.docx')


def populate_datasheet(price, price_change, price_change_percent):
    datasheet_template.merge(
        current_price=price,
        price_change=price_change,
        price_change_percent=price_change_percent)
    datasheet_template.write('datasheet/Crypto Datasheet.docx')

    convert('datasheet/Crypto Datasheet.docx', 'datasheet/Crypto Datasheet.pdf')  # Convert from word to pdf
    os.remove('datasheet/Crypto Datasheet.docx')  # remove word
    ftp_upload()


def ftp_upload():
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")

    session = ftplib.FTP('denisdzeladini.bplaced.net', 'denisdzeladini', 'DenisTBZ123')
    file = open('datasheet/Crypto Datasheet.pdf', 'rb')  # Define file to send
    session.storbinary('STOR Crypto Datasheets/Crypto Datasheet_' + current_date + '.pdf',
                       file)  # Send datasheet to FTP
    file.close()  # Close file and FTP
    session.quit()
    mt.send_mail()
