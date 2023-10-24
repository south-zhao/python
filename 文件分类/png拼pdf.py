"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time :  2023/10/15 22:55
    @Author : south(南风)
    @File : png拼pdf.py
    Describe:
    -*- coding: utf-8 -*-
"""
import fitz

if __name__ == "__main__":
    num = int(input("输入总页数:"))
    doc = fitz.Document(filetype="pdf")
    for i in range(1, num):
        imagePath = f"./{i}.jpg"
        img = fitz.Document(imagePath)
        imgPdf = fitz.Document("pdf", img.convert_to_pdf())
        doc.insert_pdf(imgPdf)
    doc.save("./output.pdf")
    doc.close()
