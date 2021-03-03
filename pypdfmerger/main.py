import argparse
import webbrowser 
import os
from PyPDF2 import PdfFileMerger
import time


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--files',
                        help='the pdf files to merge', default=[],
                        nargs='+')

    parser.add_argument('--output',
                        help='the name of the output (merged pdfs)',
                        default='merged.pdf')

    args = parser.parse_args()
    
    if len(args.files) != 0:
        pdf_source = args.files

    else:
        pdf_source = None
        print('No pdf files supplied to merge')

    if pdf_source is not None:
        pdfs = [f for f in pdf_source if os.path.splitext(f)[1] == '.pdf']
        merge_pdfs(pdfs, output=args.output)

    complete()


def merge_pdfs(pdfs, output):
    print('Beginning pdf merging...', end="", flush=True)
    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(output)
    merger.close()
    print('Complete')


def complete():
    y = input('Press any key to continue   ')

    if y == 'dmt':
        url = 'https://youtu.be/XwvmpVbggCU?t=37'
        webbrowser.open(url)

    elif 'rick' not in y and 'roll' not in y:
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        webbrowser.open(url)


if __name__ == '__main__':
    exit(main())
