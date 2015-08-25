import os
import shutil

pwd=os.getcwd()

def move():
  source_files=[pwd+'/'+'tableStyle.css',pwd+'/'+'indexstyle.css',pwd+'/'+'pacific.gif']
  destination_folder=pwd+'/'+'htmlfiles'

  for i in source_files:
    shutil.copy(i,destination_folder)
