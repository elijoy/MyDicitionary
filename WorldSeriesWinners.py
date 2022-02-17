def main():
#variables
    teams_dict = {}
    years_dict = {}

    file_object = open("WorldSeriesWinners.txt", "r")
    line = file_object.readline().strip("\n")

    #User Input
    year = int(input('Input Year in the range of 1903-2008: '))

    for years in range(1903,2008):
        #They dont play in these years
        if year == 1904 or year == 1994:
            print("World Series were not played.")
            break
        elif year < 1904 or year >=2008:
            print("World Series were not/have not been played.")
            break
        else:
            winner = teams_dict[year]
            wins = years_dict[winner]
            print(wins)

            # teams_dict[year] = line
            # line = file_object.readline().strip("\n")
            # print(teams_dict)
            





    # if year == 1903 or == 2008:
    #     winner = years_dict[year]
    #     wins = teams_dict[winner]
    #     print(winner)
    #     print(wins)


    # count = 0




    # for year in range(1903,2008):
    #     teams_dict[year] = line
    #     line = file_object.readline().strip('\n')
    #     count += 1
    #     #print(line, count)

    # if line != teams_dict:
    #     count += 1
    #     teams_dict[line] = count
    # else:
    #     count = 0
    # print(teams_dict)





main()
