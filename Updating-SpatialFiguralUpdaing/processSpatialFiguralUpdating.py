import glob
import pandas as pd
import numpy as np

# list all data files from target folders
''' please add folders paths below '''
SFU_folders = [r'D:/PhD/study1/executive-function-tasks/Updating-SpatialFiguralUpdaing/Adaptive/data',
               r'D:/PhD/study1/executive-function-tasks/Updating-SpatialFiguralUpdaing/Standard/data',
               r'D:/PhD/study1/executive-function-tasks/Updating-SpatialFiguralUpdaing/Control/data']
SFU_filelist = [file for path in SFU_folders for file in glob.glob(path + '/*.csv')]

# create an empty list for storing data
data_list = []

# create the for loop to go through all data files
for files in range(0, len(SFU_filelist)):
    SFU = pd.read_csv(SFU_filelist[files])
    # create if condition to work with the data
    if 'experimentalBlock.thisN' in SFU.columns:
        # create variables for numbers of total trials and total sets for future calculation
        set_num = SFU['myExp.trial'].max()

        # create accuracy variables
        accuracy = ((SFU['myExp.Accuracy_Mean'] == 1).sum() / set_num) * 100 # only count when recall correctly for all colours in a set

        # create trial duration variables
        median_trialDuration = SFU['myExp.gridDuration'].median() * 1000

        # creat completion time variable
        completion_time = SFU['experimentalUpdateAccuracy_tot.stopped'].max() - SFU['experimentalTrial.started'].min()

    else:
        accuracy = median_trialDuration = None

    # append values into the list
    data_list.append({'participant': SFU.iloc[1]['participant'],
                      'task': SFU.iloc[1]['expName'],
                      'accuracy(%)': accuracy,
                      'median_trialDuration(ms)': median_trialDuration,
                      'completion_time(s)': completion_time})
SFU_data_long = pd.DataFrame(data_list)

# save as csv
SFU_data_long.to_csv("spatialFiguralUpdating_longFormat.csv", index=False)
