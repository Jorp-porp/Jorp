#itertools allows easy utilization of cartesian products to create a list of all T/F combinations.
import itertools

#pandas is used to store statement variables/statement forms in dataframes and to access that data
import pandas as pd

#Statement form to be evaluated
'''
    I intend to extract this from any input logical statement ie:
        'Josh is dumb and not smart' would be parsed into 'a and not b'
        But for now, I just convert the statement into statement its statement
        form manually. This should be scaleable to more complex logical
        statements abiding to the order of operations.
    '''
form = '(a or b) and not (a and b)'

#Set the number of statement variables in statement form
'''
    This will be expanded to automatically pull numVars from the input statement.
    '''
numVars = 2

#Generate the number of columns and assign alphabetical variable names
columns = []
for n in range(numVars):
    columns.append('abcdefghijklmnopqrstuvwxyz'[n])

#create a truth table for the desired number of variables
cartesianProduct = list(itertools.product((True, False), repeat=numVars))

#initialize a dataframe with numVars columns and include all possible T/F values via the cartesianProduct
df = pd.DataFrame(cartesianProduct, columns=columns)

#Evaluate statements using all possible combinations of truth values.
for row in df:
    df[form] = df.eval(form)

print(df)