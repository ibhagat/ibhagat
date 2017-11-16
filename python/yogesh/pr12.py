# pr12.py
# Dictionary Example

capitals =  { 'India' : 'New Delhi',
              'UK' : 'London',
              'Germany' : 'Berlin',
              'France' : 'Paris',
              'Bhutan' : 'Thimpu',
              'Russia' : 'Moscow' }

# Fetching a Value based on Key
print ('\n The Capital of Bhutan is : %s' %capitals['Bhutan']) 

# Adding {Key} : {Value} Pair

capitals['Japan'] = 'Tokyo'

print ('\n There are %d pairs in the dictionary' %len(capitals))

# Delete a Pair

del capitals['UK']

print ('\n Now, there are %d pairs in the dictionary \n' %len(capitals))

# List of Key:Value Pairs

for country, capital in capitals.items() :
    print ('Capital of %s is %s ' %(country, capital))


# Pickup value passing Key

if 'Germany' in capitals:
     print ('\n Capital of Germany is %s ' % capitals['Germany'])



   
