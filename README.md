# Kaprekar_Project
This is a project that tests Kaprekar's Routine. Kaprekar's Constant, 6174, has a very interesting property. If you take any four digit number with at least 3 unique digits (i.e. not numbers like 1111, 1212, etc.), you can apply Kaprekar's Routine by arranging the digits in ascending and descending order (leading zeroes included) and subtracting the smaller of the numbers you've created from the larger. Applying this algorithm some number of times will result in Kaprekar's Constant. When applied to Kaprekar's Constant, Kaprekar's Routine results immediately in 6174.
A full description of the routine can be found [here](https://brilliant.org/wiki/kaprekars-constant/#:~:text=Kaprekar%20constant%2C%20or%206174%2C%20is,arrive%20at%20the%20number%206174.).

# Process
I started by building a function called "kap", which will test to see that a number meets the criteria of Kaprakar's Routine, then apply the routine to the number, returning the number of steps (i.e. the Kaprekar Score) needed to reach Kaprekar's Constant. Then, I used this function to find the Kaprekar Score of all numbers from 1000 through 9999, removing any that did not meet the criteria of the routine. Finally I graphed this result using seaborn. Results below.

<img src="https://github.com/aadams10046/Kaprekar_Project/blob/main/Kaprekar_Score_Chart.png?raw=true" alt="Graph for Kaprekar Score 1000-9999" title="Kaprekar Results">

One might expect either a normal distribution or a uniform distribution of the Kaprekar scores, but we can see that is not precisely the case. However, it can be said that the results are *roughly* uniform.
# Skills Demonstrated
* Python: including seaborn, pandas series, building functions, and mathematical logic

# Full Python Code Below

```python
#Importing the appropriate Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Function for determining if a number meets the criteria and returning the number of steps to reach Kaprekar's constant.
def kap(n):
    string, counstr, count, new = str(n), '', 0, 0
    for _ in string:
        if _ not in counstr:
            counstr += _
    #Numbers with at least two unique digits are required for this algorithm.
    #By returning 0 in the case of a number not meeting the criteria, I can easily filter these out later.
    if len(counstr) < 3 or len(string) != 4:
        return 0
    else:
        while new != 6174:
            little = ''.join(sorted(list(string)))
            big = ''.join(sorted(list(string),reverse = True))
            new = int(big) - int(little)
            string = str(new)
            count +=1 
        return count

#Establishing a DataFrame and removing all entries where the number doesn't meet the criteria.
data = {'Number': [x for x in range(1000, 9999)], 'Count': [kap(x) for x in range(1000,9999)]}
ddf = pd.DataFrame(data)
df = ddf[ddf['Count'] >= 1]

#Graphing the counts for all numbers that meet the criteria for Kaprekar algorithm.
sns.barplot(data = df, x = 'Number', y = 'Count', orient = 'h', ci = None, capsize = 0.4, linewidth = 3, edgecolor = '0.5', facecolor = (0,0,0,0))
plt.xlabel('Count')
plt.ylabel('Kaprekar Score')
plt.show()
```
