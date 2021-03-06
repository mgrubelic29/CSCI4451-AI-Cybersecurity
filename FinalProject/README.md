# Final Project
## Detecting Anomalies in Network Traffic using Machine Learning 

**Authors:** Luke Turbert, Matthew Grubelic

The risk of crippling cyber attacks on computer systems is increasing rapidly each day. Current software and techniques used to defend against these malicious attacks are showing their limitations and are being completely overwhelmed in some cases. As a result, a more modern and forwardthinking solution is becoming increasingly necessary. The team is implementing one such software solution using a sequence to sequence neural network in Python3 with the Pytorch library to observe malicious events and predict when the next attack might happen. In this project, a deep learning sequence to sequence model, modeled after behavior of predictive typing technologies, was implemented on the DARPA 1999 dataset to detect malicious TCP traffic and determine the probability of another attack in the future. The model functions by observing sequences of network packets, using them to predict upcoming sequences of packets, and comparing the actual observed data to the prediction. Since the amount of notable research and experimentation done in this area so far is lacking, the results yielded by this network traffic anomaly detection approach further demonstrate that the use of a sequence to sequence model is a viable, though still emerging, solution for modern intrusion detection systems


## What is in this README.md? 

In this README.md, a quick instructional guide will be given to help in the setup and execution of the code associated with this projcet.

The project has **three main pieces of code:** The "DARPADatatsetParser.ipynb", the "Seq2SeqTraining.ipynb" and the "Seq2SeqTesting.ipynb"

