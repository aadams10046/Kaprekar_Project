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