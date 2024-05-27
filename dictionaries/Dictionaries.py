#changeable unordered collection of unique key: value pairs
# They are fast because they use hashing, they allow quick access a value quickly

captials = {'Ireland': 'Dublin',
            'USA': 'Washington',
            'India': 'Dehli',
            'Germany': 'Berlin',
            'Russia': 'Moscow'}
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