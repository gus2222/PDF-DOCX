import os

import pdf2docx

Converter = pdf2docx.Converter


# convert pdf to docx
def pdf_docx(file_in,file_out):
    cv = Converter(file_in)
    cv.convert(file_out)

    return file_out # all pages by default
    cv.close()



def save_uploadedfile(uploadedfile):
    clean()
    with open(os.path.join(".", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return "Arquivo {} Salvo".format(uploadedfile.name)

def clean():# check arquives .docx and .pdf  then clean.
    f_in_dir = os.listdir(".")
    fil_f = [file for file in f_in_dir if file.endswith(".docx") or file.endswith(".pdf")]
    if len(fil_f) >= 4 :
        for file in fil_f:
            os.remove(file)
