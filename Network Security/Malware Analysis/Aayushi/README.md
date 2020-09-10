# Malware-Analysis
Malware Analysis using Machine Learning

## Introduction

The objective of this project is to perform malware analysis on a given dataset to implement various basic classification-based machine learning algorithms. We make use of two datasets, one which is self-generated and another obtained from the internet. The classification algorithms used are Gaussian Naive Bayes, RandomForestClassifier, DecisionTreeClassifier & Linear SVC.

## Summary

The self-generated dataset was created by:
- running windows PE files through the cuckoo sandbox to obtain benign file data
- obtaining malign hashes from virusshare.com and running them through an online malware analyzer (virustotal.com) to obtain malignant file data

The online dataset used was: https://www.kaggle.com/amauricio/pe-files-malwares

The accuracy obtained using various algorithms on the self-generated dataset:
- using Gaussian Naive Bayes: 50.5%
- using RandomForestClassifier: 96.96%
- using DecisionTreeClassifier: 100%
- using Linear SVC: 100%

The accuracy obtained using various algorithms on the online dataset:
- using Gaussian Naive Bayes: 32.24%
- using RandomForestClassifier: 98.44%
- using DecisionTreeClassifier: 41.01%
- using Linear SVC: 96.06%

