# Executive Function Tasks



This repository contains **5 executive function tasks**, each implemented in **3 different versions (control, standard, adaptive)**



> ⚠️ The Stop-Signal Task (Verbruggen et al., 2008) is publicly available at https://github.com/fredvbrug/STOP-IT.



All tasks are compatible with *PsychoPy version 2025.1.1*



---



## 🔧 Task setup and modification (user-friendly guide)


Each task includes:

1\. Instructions

2\. A practice block

3\. An experimental block


Detailed task configurations can be found in the published paper and its supplementary material



---



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


---


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


---


### 3. Experimental Block Settings


**3.1 Calling Initial Trial Duration from the Practice Block**
- Controlled under *#adaptive or trial duration* in the *Begin Routine* of addData(_x) component 
- Location:  `experimentalTrial`

**3.2 Adaptation Criteria (adaptive version only)**
- Controlled under *#adaption* in *End Routine* of addData(_x) component (*Begin Routine* of endSetCode_2 component in Spatial-Figural Updating Task)
- Location:  `experimentalTrial` (`experimentalUpdateAccuracy_tot` in Spatial-Figural Updating Task)

---


**Questions or bug reports?**
📧 Please contact: thipkanlayajaiaue@gmail.com