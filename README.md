# Executive Function Tasks



This repository contains six folders for **6 executive function tasks**. Each task implemented in **3 different versions (control, standard, adaptive)** , while the stop-signal task is implemented only in a control version.

Each folder also includes a processing script 'processXXX.py' to process collected data into a dataframe


All tasks are compatible with *PsychoPy version 2025.1.1* and detailed task configurations can be found in *"Executive Function and Task Engagement in Workload and Mental Fatigue: A Multi-Domain Study Using a Novel Adaptive Paradigm" (Jaiaue et al., under review)* and its supplementary material.




> The standard and adaptive Stop-Signal Task implementations used in this study are based on Verbruggen et al. (2008) and are available at https://github.com/fredvbrug/STOP-IT.



---



## 🔧 Task setup and modification (user-friendly guide)


Each task includes:

1\. Instructions

2\. A practice block

3\. An experimental block





### 1. Both Practice and Experimental Blocks



**1.1 Stimulus Sequences Control**

Practice block

- Controlled in the *End Routine* of stimuliCode component
- Location: `practiceSequenceGeneration`

Experimental block

- Controlled in the *End Routine* of stimuliCode_2 component
- Location:  `taskSequenceGeneration`


> 🧩 Within these components, you can manipulate task parameters and predictability under the following sections:


**a. Trial Numbers and Distributions**

- Total trial number ⚠️ Please note that a higher number of trials may result in longer sequence generation times due to strict constraints.

- Proportion of trial types


**b. Trial Sequence Generation**: defines how trials are ordered and how predictable the sequence is

- **b.1 Assign Stimuli Pool**: define stimulus pool(s)


**c. Assign Response Keys**

- Set response keys for the task 
⚠️ Must also match the allowedKeys field of the xxResp(_x) component in `practiceTrial` and `experimentalTrial`



**1.2 Data Identification and Recording**
- Controlled in the *End Routine* of addData(_x) component
- Location:  `practiceTrial` or `experimentalTrial`(`practiceResponse` or `experimentalResponse` in Spatial-Figural Updating Task)





### 2. Practice Block Settings

**2.1 Feedback for Each Trial**
- Text and colour controlled in the *Begin Routine* of fbCode component
- Location:  `practiceTrial_feedback`

**2.2 Calculation of Individualized Trial Duration**
- Controlled in the *Begin Routine* of fbCode_2 component
- Location:  `practiceBlock_feedback`

**2.3 Target Accuracy Threshold**
- Controlled in the *End Routine* of fbCode_2 component
- Location:  `practiceBlock_feedback`

**2.4 Practice Repetition**
- Controlled in the `nReps` field of the `practiceRepetition` loop





### 3. Experimental Block Settings


**3.1 Calling Initial Trial Duration from the Practice Block**
- Controlled under *#adaptive or trial duration* in the *Begin Routine* of addData_x component 
- Location:  `experimentalTrial`

**3.2 Adaptation Criteria (adaptive version only)**
- Controlled under *#adaption* in *End Routine* of addData_x component (*Begin Routine* of endSetCode_2 component in Spatial-Figural Updating Task)
- Location:  `experimentalTrial` (`experimentalUpdateAccuracy_tot` in Spatial-Figural Updating Task)


---


### 🗃️ **Process the data**

Data collected from each task can be processed using *processXXX.py*, which can be found inside the respective task folder.
⚠️ Make sure the list of folder paths (line 7) is updated to match the location of your data folder(s).


---

***Please cite: Gallicchio, G., & Jaiaue, T. (2026). Adaptive-executive-function-tasks. Zenodo. https://doi.org/10.5281/zenodo.18416064***

**Questions or bug reports?**
📧 Please contact: thipkanlayajaiaue@gmail.com
