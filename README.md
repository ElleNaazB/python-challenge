## Introduction

This repository contains two distinct Python scripts, each designed to extract and analyze specific data from two unique datasets. The primary focus of this project is to demonstrate data processing and analysis capabilities using Python.

# 1. Financial Data Analysis Script
<img src="https://github.com/ElleNaazB/python-challenge/blob/main/revenue-per-lead.png">

## Objective
The objective of this project is to develop a Python script capable of performing an in-depth analysis of a <a href="https://github.com/ElleNaazB/python-challenge/blob/main/PyBank/Resources/budget_data.csv" target="_blank">financial dataset</a>.  <a href="https://github.com/ElleNaazB/python-challenge/blob/main/PyBank/Main%20Script/PyBankScript.py" target="_blank"> The script </a> is able to to compute a range of critical financial metrics, offering valuable insights into the dataset's underlying trends and patterns.

## Calculated values 

1. **Total Duration**: Compute the total number of months covered in the dataset.
2. **Net Total**: Accurately determine the net total amount of "Profit/Losses" over the entire period covered by the dataset.
3. **Monthly Changes and Average**: Analyze the month-to-month changes in "Profit/Losses", and calculate the average of these changes across the entire period.
4. **Peak Profit Increase**: Identify the month with the greatest increase in profits, including both the date and the amount of the increase.
5. **Largest Profit Decline**: Determine the month with the greatest decrease in profits, specifying the date and the amount of the decrease.

## Output Requirements
The script is capable of both displaying these analyses directly in the terminal and exporting the results to an   <a href="https://github.com/ElleNaazB/python-challenge/blob/main/PyBank/Analysis/financial_analysis.txt" target="_blank"> external file </a> for further use or record-keeping.


# 2. Election Data Analysis Project
<img src="https://github.com/ElleNaazB/python-challenge/blob/main/Vote_counting.png">

## Overview
This project revolves around a comprehensive analysis of a dataset named <a href="https://github.com/ElleNaazB/python-challenge/blob/main/PyPoll/Resources/election_data.csv" target="_blank"> `election_data.csv` </a>. The dataset comprises three columns: "Voter ID", "County", and "Candidate". The primary task here is to develop a <a href="https://github.com/ElleNaazB/python-challenge/blob/main/PyPoll/PythonScript/PyPollScript.py" target="_blank"> Python script </a> tailored to dissect the voting data and extract important insights.

## Calculated values:

1. **Total Votes Cast**: Calculate the aggregate number of votes cast in the election.
2. **Candidates List**: Compile a complete list of candidates who received votes.
3. **Vote Percentage by Candidate**: Determine the percentage of the total vote each candidate won.
4. **Total Votes per Candidate**: Count the total number of votes each candidate secured.
5. **Election Winner**: Ascertain the winner of the election based on the popular vote.

## Output Specifications
The script is capable of performing two essential functions:
- **Display Results in Terminal**: Directly present the analysis in the terminal.
- **Export Results**: Generate a <a href="https://github.com/ElleNaazB/python-challenge/blob/main/PyPoll/PythonScript/election_results.txt" target="_blank">text file </a>that encapsulates the complete analysis.
