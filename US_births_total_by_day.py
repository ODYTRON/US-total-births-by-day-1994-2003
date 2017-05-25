# the dictionary 
the_dict = dict() 
# open the dataset
f = open("births.csv", 'r')
# read the dataset
text = f.read()
# split the dataset aka put it in list
data = text.split('\n')
# cut the heading year /year,month,date_of_month,day_of_week,births
data_no_head = (data[1:-1])
# with this iteration we access the data so far
for row in data_no_head:
# then we split every element with comma to make list of lists
    split_row = row.split(',')
# store the day of week 
    day_of_week = split_row[3] 
# store births
    births = int(split_row[4])
# if the day of the week key is in the_dict
    if day_of_week in the_dict:
# set the specific key in the dict and add the number of births
        the_dict[day_of_week] = the_dict[day_of_week] + births 
# else else just set the key with the births / this is the initial trigger to fill the_dict 
    else:
        the_dict[day_of_week] = births
# print the dict out of the loop 
print (the_dict)
