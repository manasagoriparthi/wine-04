#Reading 01.txt as a input file 
unsorted = open("01.txt", "r")
#Writing 02.txt as a output file
sorted = open("02.txt", "w")
# redaing the input data lines into the datalist
dataList = unsorted.readlines()
# sorting the data 
dataList.sort()
#for loop for reading each line and writing it to the output
for line in dataList:
    print (line)
    sorted.write(line)
#closing the input and output files
unsorted.close()
sorted.close()