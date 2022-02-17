file_subject = open("WorldSeriesWinners.txt",'r')

#variables
winner = []
wincount={}
year_list = []
win_years= {}

for record in file_subject:
    record = record.rstrip('\n')
    winner.append(record)

#finding count
for record in winner:
    counter = winner.count(record)
    wincount[record]= counter

for key in list(wincount.keys()):
    print(key, ": ",wincount[key], sep = '')

for record in range (1903,2009):
    if record == 1904:
        continue
    elif record == 1994:
        continue
    else:
        year_list.append(record)

for key in year_list:
    for value in winner:
        win_years[key] = value
        winner.remove(value)
        break  


#user input
year = int(input('Enter year from 1903-2008: '))
if year == 1904 or year == 1994:
    print("The world series did not play in the ", year)
elif year < 1903 or year > 2008:
    print("The World Series did not happen at this time.")
elif year in win_years:
    print(win_years[year])

file_subject.close()