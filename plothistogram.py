#!/usr/bin/env python

import os
import os.path as op
import pandas as pd
import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib import cm
from argparse import ArgumentParser
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

parser = ArgumentParser(description = 'A CSV reader + stats maker')
parser.add_argument('csvfile',
                     type = str,
                     help = 'path to the input csv file.')

parsed_args = parser.parse_args()
my_csv_file = parsed_args.csvfile

assert op.isfile(my_csv_file), "Please give us a real file, thx"
print('woot, the file exists')


#*********************************************************
# Load data, Organize dataset and Add header to the dataframe
#*********************************************************

data = pd.read_csv(my_csv_file, sep='\s+|,', header=None, engine='python', 
                names = ['ID number', 'Diagnosis','Radius_M', 'Texture_M', 'Perimeter_M', 'Area_M','Smoothness_M', 'Compactness_M', 'Concavity_M', 'ConcavePoints_M', 'Symmetry_M', 'FractalDimension_M',
                         'Radius_SE', 'Texture_SE', 'Perimeter_SE', 'Area_SE','Smoothness_SE', 'Compactness_SE', 'Concavity_SE', 'ConcavePoints_SE', 'Symmetry_SE', 'FractalDimension_SE',
                         'Radius_W', 'Texture_W', 'Perimeter_W', 'Area_W','Smoothness_W', 'Compactness_W', 'Concavity_W', 'ConcavePoints_W', 'Symmetry_W', 'FractalDimension_W'])
data.drop(['ID number'], axis=1, inplace=True)


def plot2DHistogram(data, folder):
      i = 1
      figIndex = 1
      #columncount = len(data.columns)
      columncount = 12  # To avoid having so many scatter     
      while i < columncount - 1:
            j = i + 1
            while j < columncount:
                  iv = data.iloc[:, i]
                  jv = data.iloc[:, j]
                  plt.figure(data.columns[i])
                  plt.hist2d(iv, jv, bins = 30, cmap = 'Blues')
                  cb = plt.colorbar()
                  cb.set_label('Counts in bin')
                  plt.title('BSWisconsin DataSet')
                  plt.xlabel(data.columns[i])
                  plt.ylabel(data.columns[j])
                  plt.savefig('./{0}/Hist2d_{1}.png'.format(folder, data.columns[i] + ' ' + data.columns[j]))
                  #plt.show()
                  plt.close("all")
                  j = j + 1
                  figIndex = figIndex + 1
            i = i + 1      

def plotGroupedHistogram(data, columns, gr_feature, folder):
	l = len(columns)
	n_cols = math.ceil(math.sqrt(l))		
	n_rows = math.ceil(l / n_cols)
	
	fig=plt.figure(figsize=(11, 6), dpi=100)
	for i, col_name in enumerate(columns):		
		if col_name != gr_feature:				
			ax = fig.add_subplot(n_rows,n_cols,i)
			ax.set_title(col_name)
			grouped = data.pivot(columns = gr_feature, values = col_name)
			for j, gr_feature_name in enumerate(grouped.columns):							
				grouped[gr_feature_name].hist(alpha = 0.5, label = gr_feature_name)
			plt.legend(loc = 'upper right')
	fig.tight_layout()
	plt.savefig('./{0}/HistGroupBy{1}.png'.format(folder,gr_feature))
	#plt.show()            

plot2DHistogram(data,'Figures')
plotGroupedHistogram(data.iloc[:,:11], data.iloc[:,:11].columns, 'Diagnosis', 'Figures')