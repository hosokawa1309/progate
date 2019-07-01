import PyPDF2

merger = PyPDF2.PdfFileMerger()

merger.append('1705.07962.pdf',pages = PyPDF2.pagerange.PageRange(':6'))

merger.write('705.07962_split1.pdf')

merger.close()


merger = PyPDF2.PdfFileMerger()

merger.append('1705.07962.pdf',pages = PyPDF2.pagerange.PageRange('6:'))

merger.write('1705.07962_split2.pdf')

merger.close()

