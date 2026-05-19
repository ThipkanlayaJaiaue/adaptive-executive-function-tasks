import glob
import pandas as pd
import numpy as np

# list all data files from target folder
''' please add folders paths below '''
stopsig_folder = glob.glob(r"D:\PhD\study1\executive-function-tasks\Inhibition-StopSignal\Control\data\*.csv")
stopsig_filelist = [file for file in stopsig_folder]
print(stopsig_filelist)
# create an empty list to store data
data_list = []

# create the for loop to go through all data files
for file in range(0, len(stopsig_filelist)):
    stopsig = pd.read_csv(stopsig_filelist[file])

    # create if condition to work with the data
    if 'myExp.trial' in stopsig.columns:

        # create mean RT variables
        medianRT_go = stopsig["myExp.RT_correctTrials"].median() * 1000

        # create accuracy variables
        accuracy_go = (stopsig["myExp.Accuracy"].sum() / stopsig["myExp.trial"].max()) * 100

        # create trial duration variables
        median_trial_duration = stopsig["myExp.trialDuration"].median() * 1000

        # creat completion time variable
        completion_time = stopsig['blank.stopped'].max() - stopsig['experimentalTrial.started'].min()

        # append values into the list
        data_list.append({
            'participant': stopsig.iloc[0]["participant"],
            'task': stopsig.iloc[0]["expName"],
            'medianRT_go(ms)': medianRT_go,
            'accuracy_go(%)': accuracy_go,
            'median_trialDuration(ms)': median_trial_duration,
            'completion_time(s)': completion_time})
stopSignal_data_long = pd.DataFrame(data_list)

# save as csv
stopSignal_data_long.to_csv("stopSignal_longFormat.csv", index=False)