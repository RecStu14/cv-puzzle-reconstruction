#PATHS 
"""
In order for cleaner code and to accommadate changes in the future, depening on the task, 
relative paths are all declared in 1 file and then called.
"""
#Imports
import os

#Getting the Current Working Directory
#/Users/sankeerthana/Documents/Lauretta
PARENT_DIR = "/Users/sankeerthana/Documents/Lauretta"

#Folders with Images
TEST_DATA = os.path.join(PARENT_DIR, 'Test_Data')
VAL_TEST =  os.path.join(PARENT_DIR, 'Validation_Test')

#Subfolders in Test Data in Folder
FUMO_DIR = os.path.join(TEST_DATA, 'fumo')
GALAXY_DIR = os.path.join(TEST_DATA, 'galaxy')
SIMPLE_DIR = os.path.join(TEST_DATA, 'simple')

#Subfolders in Validation Test Folder
MAP_DIR = os.path.join(VAL_TEST, 'map')
SATURN_DIR = os.path.join(VAL_TEST, 'saturn')
XRAY_DIR = os.path.join(VAL_TEST, 'xray')


