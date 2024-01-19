highest_exp = 0
lowest_exp = 99999
country_low = ""
country_high = ""
highest_year = ""
lowest_year = ""
count = 0
total = 0

input_year = input("Enter year: ")
with open("life-expectancy.csv") as the_file:
    # next(the_file) #this tells it to go to the 2nd/next line
    first_line = the_file.readline() #reads the line then ignores it
    for line in the_file:
        line = line.split(",")
        country = line[0]
        code = line[1]
        year = line[2]
        exp = float(line[3])


        if exp < lowest_exp:
           lowest_exp = exp
           country_low = country
           lowest_year = year
        
        if exp > highest_exp:
            highest_exp = exp
            country_high = country
            highest_year = year

        if input_year == year:
            count += 1
            total = total + exp
            ave = total / count
         
    
    print(f"{ave} is the average life expectancy for that year.")
            

    print(f"The year and country with the lowest life expectancy is {lowest_year} in {country_low} with {lowest_exp} life expectancy.")
    print(f"The year and country with the highest life expectancy is {highest_year} in {country_high} with {highest_exp} life expectancy.")


    #Allow the user to type in a year, then, find the average life expectancy for that year. 
    #Then find the country with the minimum and the one with the maximum life expectancies for that year.

    

                