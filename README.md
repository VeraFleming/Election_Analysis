# Election_Analysis

## Project Overview

Work with exsisting statrer code to analyse election_results.csv file using for loops and conditional statements with membership and logical operators find the requested results. Then, print the results to the command line and save them to election_results.txt file.

A Colorado Board of Elections employee has given us the following tasks to complete the election audit of a recent local congressional election:

1. Calculate the total number of votes cast.
2. Get a complete list list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

After that write additional script to the existing code, so that the election commission could see the following:
- The voter turnout for each county;
- The percentage of votes from each county out of the total count;
- The county with the highest turnout.
After that we had to print the results to the command line and save them to election_results.txt file.

# Resources
- Data source: election_results.csv

- Software: Python 3.7.6, Visual Studio Code 1.67.2

- Tools: Jupyter Notebook

## Election-Audit Results:

When we run our code we can see the next outcomes:
- The total number of votes in this congressional election was 369,711 votes.
- There were 3 county in the election and their results were the following:
    
    - Jefferson received 10.5% of the votes and 38,855 number of votes.
    - Denver received 82.8% of the votes and 306,055 number of votes.
    - Arapahoe received 6.7% of the votes and 24,801 number of votes.
    
- The largest number of votes received Denver county.

- There were 3 candidates in the election and their results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
    
The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
    
The text file was created for the Colorado Board of Elections and look like the following picture:

<img src= "analysis/election results.png" width = "400">    

## Election-Audit Summary:

Our code can be applied to any election at any time; all we need to do is verify that the file we intend to use contains the same rows as our original 
file, and then modify the source code by altering the value of the "file_to_load" variable.
Additionally, in the future we can create a code that would check for new file with election results daily and run our existing code to reveal the winner's name every day, then you can see the trend of the elections.

    
