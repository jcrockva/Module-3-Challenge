# Module-3-Challenge
PyPoll and PyBank Analysis


PyBank: In this excersie I used python to analyze financial data from a CSV file. I used the csv and os modules to create the file path and read the data. I then looped through the data to find the total number of months, the net profit and monthly changes.
I then found the greatest increase and decrease by subtracting the current months value from the previous months. These values were stored in a list then using the min() and Max() function I found the desired results. Lastly the data was printed to a txt file to display my findings.

PyPoll: For this excersise I used similar methods. Again using the csv and os functions to create a file path and read the data in the file. I again lopped through the data this time looking for total votes, votes per canidate and vote percentage per canidate. 
Using the Winning_count variable I was able to keep track of the current highest vote getter with each iteration checking to see if the next vote getter was higher. If a new higher percentage or count was found then the the winning canidate would be updated. The results once again were printed in a text file using print to txt.

