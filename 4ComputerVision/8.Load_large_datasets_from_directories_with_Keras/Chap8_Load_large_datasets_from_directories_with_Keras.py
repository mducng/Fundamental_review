

#------------------------------------------------------------------------------
# to load library
#------------------------------------------------------------------------------
from keras.preprocessing.image import ImageDataGenerator

#------------------------------------------------------------------------------
# SUBMODULES
#------------------------------------------------------------------------------
def load_images():
    # create generator
    datagen = ImageDataGenerator()
    # prepare an iterators for each dataset
    train_it = datagen.flow_from_directory('data/train/', class_mode='binary')
    val_it = datagen.flow_from_directory('data/validation/', class_mode='binary')
    test_it = datagen.flow_from_directory('data/test/', class_mode='binary')
    # confirm the iterator works
    batchX, batchy = train_it.next()
    print('Batch shape=%s, min=%.3f, max=%.3f' % (batchX.shape, batchX.min(), batchX.max()))
    
#------------------------------------------------------------------------------ 
# TOP-MODULES
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# TESTBENCHS
#------------------------------------------------------------------------------

# testbench for load_images()
def tb_load_images():
    load_images()


#------------------------------------------------------------------------------
# MAIN FUNCTIONS
#------------------------------------------------------------------------------
if __name__ == "__main__":
    tb_load_images()
    
    