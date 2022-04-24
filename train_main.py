#----------------- 2  calling training fuction from facenet classifer to train the model on our dataset
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys
from classifier import training

datadir = './ProcessedFaces'
modeldir = './model/trained_facenet_model.pb'
#modeldir = './model/20180408-102900.pb'
classifier_filename = './class/RamdanModel4MorePhotos.pkl'
print ("Training Start")
obj=training(datadir,modeldir,classifier_filename) #fix this 
get_file=obj.main_train()
print('Saved classifier model to file "%s"' % get_file)
sys.exit("All Done")
