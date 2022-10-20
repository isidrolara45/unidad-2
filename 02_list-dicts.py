#create 
country = ['Brasil','Rusia','India','China','South Africa']
"""Create a dictionary of BRICS capitals.
Note that South Africa has 3 capitals. Therefore, we embed a list inside
the dictionary.
"""
capitals = {'Brasil': 'Brasilia', 'Rusia':'Moscu', 'India':'New Dheli','China':'Beijing','South Africa':['Pretoria','Cope Town','Bloemfontein']}

print('Country')
for pai in country: 
    print(pai)
print('--------------------------------------------')
print('Capitals')
for cap in capitals: 
    print(cap)
    print(capitals[cap])

print(capitals["South Africa"][1])
"""
What response did you get?
Why did the list and dictionary contents not print?
Fix the code and run the script again.
"""


"""
Why did you get an error for the 2nd capital of South Africa?
Hint: Check the syntax for the index value.
"""