\# Executive Function Tasks



This repository contains \*\*five executive function tasks\*\*, each implemented in \*\*three different versions\*\*, as used in \*Jaiaue et al. (2026)\*.



> ⚠️ The Stop-Signal Task (Verbruggen et al., 2008) is publicly available at \\\[STOP-IT GitHub](https://github.com/fredvbrug/STOP-IT).



All tasks are compatible with \*\*PsychoPy version 2025.1.1\*\*.



---



\## 🔧 Task setup and modification (user-friendly guide)



Each task includes:



1\. Instructions

2\. A practice block

3\. An experimental block



Detailed task configurations can be found in the published paper and its supplementary materials.



---



\## 1. Both Practice and Experimental Blocks



* \### Stimulus Sequences Control



\#### Practice block

\- Controlled in the \*\*`stimuliCode`\*\* component

\- Location: \*\*End Routine\*\* of `practiceSequenceGeneration`



\#### Experimental block

\- Controlled in the \*\*`stimuliCode\\\_2`\*\* component

\- Location: \*\*End Routine\*\* of `taskSequenceGeneration`



Within these components, you can manipulate task parameters and predictability under the following sections:



\### a. Trial Numbers and Distributions

\- \*\*Total trial number:\*\* `trialAll\\\_num` ⚠️ Please note that higher number of trial may lead to longer time to generate trial sequence due to strick rules

\- \*\*Proportion of trial types\*\*



\### b. Trial Sequence Generation

Defines how trials are ordered and how predictable the sequence is.



\- \*\*b.1 Assign Stimuli Pool\*\*: define one or more stimulus pools and their distribution



\### c. Assign Response Keys

\- Set response keys for the task

\- Must also match the `allowedKeys` field of the `xxResp(\\\_x)` component in `practiceTrial` and `experimentalTrial`



---



* \### Data Identification and Recording

\- Controlled in the \*\*`addData(\\\_x)`\*\* component

\- Location: \*\*End Routine\*\* of `practiceTrial` or `experimentalTrial`



---



\## 2. Practice Block Settings



* \### Feedback for Each Trial

\- Text and colour controlled in \*\*`fbCode`\*\*

\- Location: \*\*Begin Routine\*\* of `practiceTrial\\\_feedback`



* \### Calculation of Individualized Trial Duration

\- Controlled in \*\*`fbCode\\\_2`\*\*

\- Location: \*\*Begin Routine\*\* of `practiceBlock\\\_feedback`



* \### Target Accuracy Threshold

\- Controlled in \*\*`fbCode\\\_2`\*\*

\- Location: \*\*End Routine\*\* of `practiceBlock\\\_feedback`



* \### Practice Repetition

\- Controlled in the `nReps` field of the `practiceRepetition` loop



---



\## 3. Experimental Block Settings



* \### Calling Initial Trial Duration from the Practice Block

\- Controlled in the \*\*`addData(\\\_x)`\*\* 

\- Location: #adaptive or trial duration in \*\*Begin Routine\*\* of `experimentalTrial`



* \### Adaptation Criteria (adaptive version only)

\- Controlled in the \*\*`addData(\\\_x)`\*\* component

\- Location: #adaption in \*\*End Routine\*\* of `experimentalTrial`

