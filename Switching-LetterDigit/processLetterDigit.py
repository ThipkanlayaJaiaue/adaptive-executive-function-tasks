import glob
import pandas as pd
import numpy as np

# list all data files from target folders
''' please add folders paths below '''
switching_folders = [r'D:/PhD/study1/executive-function-tasks/Switching-LetterDigit/Adaptive/data',
                     r'D:/PhD/study1/executive-function-tasks/Switching-LetterDigit/Standard/data',
                     r'D:/PhD/study1/executive-function-tasks/Switching-LetterDigit/Control/data']
switching_filelist = [file for path in switching_folders for file in glob.glob(path + '/*.csv')]

# create an empty list for storing data
data_list = []

# create the for loop to go through all data files
for files in range(0, len(switching_filelist)):
    switching_data = pd.read_csv(switching_filelist[files])
    # create if condition to work with the data
    if 'myExp.trial' in switching_data.columns:
        # create variables for numbers of switch/repeat/total trials for future calculation
        switch_num = len(switching_data[switching_data['myExp.condition'] == 'switch'])
        repeat_num = len(switching_data[switching_data['myExp.condition'] == 'repeat'])
        total_trials = switching_data["myExp.trial"].max()
        correctTrials_all = switching_data["myExp.RT_correctTrials"]
        correctTrials_switch = switching_data.loc[switching_data['myExp.condition'] == 'switch', "myExp.RT_correctTrials"]
        correctTrials_repeat = switching_data.loc[switching_data['myExp.condition'] == 'repeat', "myExp.RT_correctTrials"]

        # create medianRT variables
        medianRT_all = correctTrials_all.median() * 1000
        medianRT_switch = correctTrials_switch.median() * 1000
        medianRT_repeat = correctTrials_repeat.median() * 1000
        medianRT_diff = medianRT_switch - medianRT_repeat

        # create accuracy variables
        accuracy_all = (switching_data["myExp.Accuracy"].sum() / total_trials) * 100
        accuracy_switch = (switching_data.loc[switching_data['myExp.condition'] == 'switch', "myExp.Accuracy"].sum() / switch_num) * 100
        accuracy_repeat = (switching_data.loc[switching_data['myExp.condition'] == 'repeat', "myExp.Accuracy"].sum() / repeat_num) * 100

        # create trial duration variables
        median_trial_duration = switching_data["myExp.trialDuration"].median() * 1000

        # creat completion time variable
        completion_time = switching_data['blank.stopped'].max() - switching_data['experimentalTrial.started'].min()

    else:
        medianRT_all = medianRT_switch = medianRT_repeat = medianRT_diff \
            = accuracy_all = accuracy_switch = accuracy_repeat = median_trial_duration = None

    # append values into the list
    data_list.append({'participant': switching_data.iloc[1]["participant"],
                      'task': switching_data.iloc[1]["expName"],
                      'medianRT_correct_all(ms)': medianRT_all,
                      'medianRT_correct_switch(ms)': medianRT_switch,
                      'medianRT_correct_repeat(ms)': medianRT_repeat,
                      'medianRT_diff(ms)': medianRT_diff,
                      'accuracy_all(%)': accuracy_all,
                      'accuracy_switch(%)': accuracy_switch,
                      'accuracy_repeat(%)': accuracy_repeat,
                      'median_trialDuration(ms)': median_trial_duration,
                      'completion_time(s)': completion_time})
switch_data_long = pd.DataFrame(data_list)

# save as csv
switch_data_long.to_csv('letterDigit_longFormat.csv', index=False)
