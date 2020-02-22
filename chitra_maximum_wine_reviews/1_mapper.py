# Reading d.txt as a input file 
input = open("d.txt", "r")
# Writing 01.txt as a output file
output = open("01.txt", "w")
# reading each line in the input file
for line in input:
    # splitting the line using tab and assigning it to a datalist
    datalist = line.strip().split("\t")
    # Assigning the columns to the datalist
    sno,country,points,price,province = datalist
    # if condition to check the null values
    if len(country) != 0:
        if len(price) != 0:
            #writing mapper output i.e country and price to 01.txt file
            output.write(country + "\t" + price + "\n")
# closing the input and output files
input.close()
output.close()