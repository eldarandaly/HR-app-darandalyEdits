#   1 run this python file to preprocess the dataset faces and crop them 
from preprocess import preprocesses

input_datadir = './TrainFolder'
output_datadir = './ProcessedFaces'
try:
    obj=preprocesses(input_datadir,output_datadir)
    nrof_images_total,nrof_successfully_aligned=obj.collect_data()
    
    print('Total number of images: %d' % nrof_images_total)
    print('Number of successfully aligned images: %d' % nrof_successfully_aligned)      
except:
    print("error")




