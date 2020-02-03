#!/usr/local/bin/python3
import argparse
import sys
import functions as f
import graphs as G
import imageandquotescraping as I
from fpdf import FPDF
import matplotlib.pyplot as plt
import pandas as pd
import sendemail as E

# Define args

def recibe_args():
    parser = argparse.ArgumentParser(description='Evaluate Friends TV show')
    parser.add_argument('--Phoebe', help = 'Evaluate Phoebe of Friends TV show', action='store_true') 
    parser.add_argument('--Joey',  help = 'Evaluate Joey of Friends TV show', action='store_true')
    parser.add_argument('--Monica', help = 'Evaluate Monica of Friends TV show', action='store_true')
    parser.add_argument('--Chandler',  help = 'Evaluate Chandler of Friends TV show' , action='store_true') 
    parser.add_argument('--Ross',   help = 'Evaluate Ross of Friends TV show' , action='store_true')
    parser.add_argument('--Rachel',  help = 'Evaluate Rachel of Friends TV show', action='store_true')
    parser.add_argument('--mailto',  default="elisammontalvo28@gmail.com", type=str ,help = 'Obtain an email with the report of Friends TV show to the email you provide')
    return parser.parse_args()

def main():
    config = recibe_args()
    pdf = FPDF()
    quotes = I.QuoteAndImage()
    G.plots()
    f.createPdf(pdf)
    if config.Phoebe:
        f.addImagesPdf(pdf,"OUTPUT/Phoebe.jpg",quotes[' Phoebe'],'Phoebe')
    elif config.Joey:
        f.addImagesPdf(pdf,"OUTPUT/Joey.jpg",quotes[' Joey'],'Joey')
    elif config.Monica :
        f.addImagesPdf(pdf,"OUTPUT/Monica.jpg",quotes[' Monica'],'Monica')
    elif config.Rachel :
        f.addImagesPdf(pdf,"OUTPUT/Rachel.jpg",quotes[' Rachel'],'Rachel')
    elif config.Ross :
        f.addImagesPdf(pdf,"OUTPUT/ross.jpg",quotes[' Ross'],'Ross')
    elif config.Chandler :
        f.addImagesPdf(pdf,"OUTPUT/Chandler.jpg",quotes[' Chandler'],'Chandler')
    else:
        pdf.image('OUTPUT/lines_episode.png', x = 30 ,y=50, w= 150)
        pdf.ln(160)
        pdf.cell(170, 20,txt="Rachel is the most talkative one", align= 'C' )
        pdf.add_page()
        pdf.image('OUTPUT/mean_lines.png', x = 10 , y = 20 , w = 150 )
        pdf.ln(150)
        pdf.image('OUTPUT/mean_lines_season.png', x = 20,y = 120, w = 150 )
        pdf.add_page()
        pdf.image('OUTPUT/mean_words.png', x = 20 , y = 30,w = 150)
        pdf.cell(170, 20,txt="Phoebe says more words per line", align= 'C' )
        pdf.ln(150)
        pdf.image('OUTPUT/Rating.png', x = 20 , y = 130,w = 150)

    print('Pdf report with results saved in the Output folder')
    f.save(pdf)

    if config.mailto:
        E.SendEmail(config.mailto)
        print('Sending Email')


if __name__=="__main__":
    main()