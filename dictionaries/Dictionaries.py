#changeable unordered collection of unique key: value pairs
# They are fast because they use hashing, they allow quick access a value quickly

captials = {'Ireland': 'Dublin',
            'USA': 'Washington',
            'India': 'Dehli',
            'Germany': 'Berlin',
            'Russia': 'Moscow'}

#adding a new item to the dictionary
captials.update({'Brazil': 'Rio'})

#can update certain values in the dictonary is well
captials.update({'USA': 'Florida'})

#Can use the pop method within the dictonaries. Removes item where the key value is 
captials.pop('Russia')

#the clear method empties the entire dictonary
captials.clear()

#Use the get method for a safer choice when using dictionaries
#print(captials['Russia'])

#Using the get method
#print(captials.get('Brazil'))

#printing just the keys
#print(captials.keys())

#printing just the values
#print(captials.values())

#printing the keys and the values
#print(captials.items())

#my attempt at print all the values using the for loop
#for x in captials:
 #   print(x)
    
#the tutorials version
for key, value in captials.items():
    print(key, value)