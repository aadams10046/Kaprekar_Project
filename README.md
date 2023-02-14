# Kaprekar_Project
This is a project that tests Kaprekar's Routine. Kaprekar's Constant, 6174, has a very interesting property. If you take any four digit number with at least 3 unique digits (i.e. not numbers like 1111, 1212, etc.), you can apply Kaprekar's Routine by arranging the digits in ascending and descending order (leading zeroes included) and subtracting the smaller of the numbers you've created from the larger. Applying this algorithm some number of times will result in Kaprekar's Constant. When applied to Kaprekar's Constant, Kaprekar's Routine results immediately in 6174.
A full description of the routine can be found [here](https://brilliant.org/wiki/kaprekars-constant/#:~:text=Kaprekar%20constant%2C%20or%206174%2C%20is,arrive%20at%20the%20number%206174.).

# Process
I started by building a function called "kap", which will test to see that a number meets the criteria of Kaprakar's Routine, then apply the routine to the number, returning the number of steps (i.e. the Kaprekar Score) needed to reach Kaprekar's Constant. Then, I used this function to find the Kaprekar Score of all numbers from 1000 through 9999, removing any that did not meet the criteria of the routine. Finally I graphed this result using seaborn. Results below.

<img src="https://github.com/aadams10046/Kaprekar_Project/blob/main/Kaprekar_Score_Chart.png?raw=true" alt="Graph for Kaprekar Score 1000-9999" title="Kaprekar Results">

# Skills Demonstrated
* Python: including seaborn, pandas series, building functions, and mathematical logic

# Full Python Code [Here](https://github.com/aadams10046/Kaprekar_Project/blob/main/kaprekar.py)
