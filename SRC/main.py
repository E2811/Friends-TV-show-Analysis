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

def reciebe_args():
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


if __name__=="__main__":
    main()