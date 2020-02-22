# Reading 02.txt as a input file 
s = open("02.txt","r")
# Reading 03.txt as a input file 
r = open("03.txt", "w")

thisKey = ""
thisValue = 0.0
max = 0.0
#reading each line and splitting the data using tab
for line in s:
  data = line.strip().split('\t')
  # storing the country and price into the data
  country, price = data
  # writing if condition to check whether the country is same as thiskey
  if country != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = country 
    thisValue = 0.0
    max=0
  # Applying the aggregation function(maximum) which provides the maximum price of wine in each country.
  # thisValue += float(amount)
  if float(price)>max:
    thisValue=float(price)
    max=thisValue
# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

# closing the input and output files.
s.close()
r.close()