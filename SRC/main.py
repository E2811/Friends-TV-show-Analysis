#!/usr/local/bin/python3
import argparse
import sys
import functions as f
import graphs as G
import calculations as C
from fpdf import FPDF
#from pandas.plotting import table
import matplotlib.pyplot as plt
import pandas as pd

# Define args

def recibe_args():
    parser = argparse.ArgumentParser(description='Evaluate Friends TV show')
    parser.add_argument('--character',
                        choices = ['Phoebe','Joey','Monica','Rachel','Ross','Chandler']      
                        default= 'Joey'   
                        )  
    parser.add_argument('-
    return parser.parse_args()

def main():
    config = recibe_args()
    mypdf = pdf.FPDF()
    pdf.createPdf(mypdf)
    
    if config.character == 'Phoebe' :
        im_pdf("../OUTPUT/Phoebe.png")
    elif config.character == 'Joey' :
        im_pdf("../OUTPUT/Joey.png")
    elif config.character == 'Monica' :
        im_pdf("../OUTPUT/Monica.png")
    elif config.character == 'Rachel' :
        im_pdf("../OUTPUT/Rachel.png")
    elif config.character == 'Ross' :
        im_pdf("../OUTPUT/ross.png")
    elif config.character == 'Chandler' :
        im_pdf("../OUTPUT/Chandler.png")

    print('Pdf report with results saved in the Output folder')
    pdf.addImagesToPdf(mypdf)
    pdf.save(mypdf)


if __name__=="__main__":
    main()