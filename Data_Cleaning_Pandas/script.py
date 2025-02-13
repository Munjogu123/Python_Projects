import pandas as pd

df = pd.read_excel(r"E:\Data Analysis\Learning\Python\Pandas\Customer Call List.xlsx")

# Removes all duplicates from the DataFrame
df = df.drop_duplicates()

# Removes whitespaces and the characters listed in the quotes from the column 'Last_Name'
df['Last_Name'] = df['Last_Name'].str.strip('123._/')

# Deletes the Column 'Not_Useful_Column'
df.drop(columns = 'Not_Useful_Column', inplace=True)

# Removes any characters other than numbers in the column
df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]', '', regex=True)

# Converts phone numbers to a string
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))

# Formats the phone numbers in this format(123-456-7890)
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' +x[6:10])

# Replaces the 'nan--' and 'Na--' strings to empty strings
df['Phone_Number'] = df['Phone_Number'].str.replace('nan--', '')
df['Phone_Number'] = df['Phone_Number'].str.replace('Na--', '')

# Splits the 'Address' column into three columns based on commas and creates new columns for the split elements
df[['Street_Name', 'State', 'Zip_Code']] = df['Address'].str.split(pat=',', n=2, expand=True)

# Coverts the 'Yes' and 'No' elements to 'Y' and 'N' respectively for the 'Paying Customer' and 'Do_Not_Contact' columns
df['Paying Customer'] = df['Paying Customer'].str.replace('No', 'N')
df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No', 'N')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes', 'Y')

# Fills N/A and NaN values with an empty string 
df.fillna('', inplace=True)

"""
Loops over the 'Do_Not_Contact' column using the DataFrame Index and checks if the value is 'Y'.
If the Value is 'Y', it deletes the row with that value
"""
for x in df.index:
    if df.loc[x, 'Do_Not_Contact'] == 'Y':
        df.drop(x, inplace=True)

"""
Loops over the 'Phone_Number' column using the DataFrame Index and checks if the value is an empty string.
If the Value is an empty string, it deletes the row with that value
"""
for x in df.index:
    if df.loc[x, 'Phone_Number'] == '':
        df.drop(x, inplace=True)

# Deletes the column 'Address'
df.drop(columns = 'Address', inplace=True)

# Resets the index of the DataFrame
df.reset_index(drop=True)
