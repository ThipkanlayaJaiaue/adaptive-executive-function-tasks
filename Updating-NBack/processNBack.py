import glob
import pandas as pd
import numpy as np

# list all data files from target folders
''' please add folders paths below '''
nBack_folders = [r'D:/PhD/study1/executive-function-tasks/Updating-NBack/Adaptive/data',
                 r'D:/PhD/study1/executive-function-tasks/Updating-NBack/Standard/data',
                 r'D:/PhD/study1/executive-function-tasks/Updating-NBack/Control/data']
nBack_filelist = [file for path in nBack_folders for file in glob.glob(path + '/*.csv')]

# create an empty list for storing data
data_list = []

# create the for loop to go through all data files
for files in range(0, len(nBack_filelist)):
    nBack = pd.read_csv(nBack_filelist[files])
    # create if condition to work with the data
    if 'myExp.trial' in nBack.columns:
        # create variables for numbers of match/non-match/total trials for future calculation
        match_num = len(nBack[nBack['myExp.nback_match'] == 1])
        nonmatch_num = len(nBack[nBack['myExp.nback_match'] == 0])
        total_trials = nBack["myExp.trial"].max()
        correctTrial_all = nBack["myExp.RT_correctTrials"]
        correctTrial_match = nBack.loc[nBack['myExp.nback_match'] == 1, "myExp.RT_correctTrials"]
        correctTrial_nonmatch = nBack.loc[nBack['myExp.nback_match'] == 0, "myExp.RT_correctTrials"]

        # create medianRT variables
        medianRT_correct_all = correctTrial_all.median() * 1000
        medianRT_correct_match = correctTrial_match.median() * 1000
        medianRT_correct_nonmatch = correctTrial_nonmatch.median() * 1000
        medianRT_diff = medianRT_correct_match - medianRT_correct_nonmatch

        # create accuracy variables
        accuracy_all = (nBack["myExp.Accuracy"].sum() / total_trials) * 100
        accuracy_match = (nBack.loc[nBack['myExp.nback_match'] == 1, "myExp.Accuracy"].sum() / match_num) * 100
        accuracy_nonmatch = (nBack.loc[nBack['myExp.nback_match'] == 0, "myExp.Accuracy"].sum() / nonmatch_num) * 100

        # create trial duration variables
        median_trial_duration = nBack["myExp.trialDuration"].median() * 1000

        # creat completion time variable
        completion_time = nBack['blank.stopped'].max() - nBack['experimentalTrial.started'].min()

    else:
        medianRT_correct_all = medianRT_correct_match = medianRT_correct_nonmatch = medianRT_diff \
            = accuracy_all = accuracy_match = accuracy_nonmatch = median_trial_duration = None

    # append values into the list
    data_list.append({'participant': nBack.iloc[1]["participant"],
                      'task': nBack.iloc[1]["expName"],
                      'medianRT_correct_all(ms)': medianRT_correct_all,
                      'medianRT_correct_match(ms)': medianRT_correct_match,
                      'medianRT_correct_nonmatch(ms)': medianRT_correct_nonmatch,
                      'medianRT_diff(ms)': medianRT_diff,
                      'accuracy_all(%)': accuracy_all,
                      'accuracy_match(%)': accuracy_match,
                      'accuracy_nonmatch(%)': accuracy_nonmatch,
                      'median_trialDuration(ms)': median_trial_duration,
                      'completion_time(s)': completion_time})
nBack_data_long = pd.DataFrame(data_list)

# save as csv
nBack_data_long.to_csv("nBack_longFormat.csv", index=False)
