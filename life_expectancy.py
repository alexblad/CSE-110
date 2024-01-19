highest_exp = 0
lowest_exp = 99999
country_low = ""
country_high = ""
highest_year = ""
lowest_year = ""
count = 0
total = 0
country_max=''
country_min=''
year_max=0
year_min=99999
code_in=''
code_min=99999
code_max=0


year_in=input('Enter year: ')
code_in=input('Enter country: ')
with open('life-expectancy.csv') as the_file:
    first_line=the_file.readline()
    for line in the_file:
        line=line.split(',')
        country = line[0]
        code = line[1]
        year = line[2]
        exp=float(line[3])

        if exp < lowest_exp:
           lowest_exp = exp
           country_low = country
           lowest_year = year
        
           
        
        if exp > highest_exp:
            highest_exp = exp
            country_high = country
            highest_year = year

        if year_in == year:
            count += 1
            total = total + exp
            ave = (total / count)
        
            if exp>year_max:
                    year_max=exp
                    country_max=country
            if exp<year_min:
                    year_min=exp
                    country_min=country
        
        if code_in == line[1]:
            count += 1
            total = total + exp
            ave = (total / count)
        
            if exp>code_max:
                    code_max=exp
            if exp<code_min:
                    code_min=exp

    

    print(f'The country with the lowest life expectancy overall is {country_low} in {lowest_year} with a {lowest_exp:.2f} year life expectancy.')
    print(f'The country with the highest life expectancy overall is {country_high} in {highest_year} with a {highest_exp:.2f} year life expectancy.')
    

    
    print(f'For {year_in}, {ave:.2f} is the average life expectancy.')
    print(f'The max life expectancy for {year_in} was in {country_max} with {year_max:.2f} years.')
    print(f'The min life expectancy for {year_in} was in {country_min} with {year_min:.2f} years.')

    print(f'For {code_in}, {ave:.2f} is the average life expectancy')
    print(f'The max life expectancy for {code_in}  was {code_max:.2f} years.')
    print(f'The min life expectancy for {code_in} was {code_min:.2f} years.')