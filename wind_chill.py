def degree_fahr(cel):
    fahrenheit = (cel * 9 / 5) + 32
    return fahrenheit 

def compute_windchill(fahr, V):
    wind_chill = 35.74 + (0.6215 * fahr) - (35.75 * (V ** 0.16)) + ((0.4275 * fahr) * (V ** 0.16))
    return wind_chill

temparature = float(input("What is the temparature? "))
temp_kind = input("Fahrenheit or Celcius (F/C)? ")
temp_kind = temp_kind.upper()

if temp_kind == "C":
    fahr = degree_fahr(temparature)
    # print(fahr)
    for wind_speed in range(5,65,5):
        wind_chill = compute_windchill(fahr,wind_speed)
        print(f"At temparature {temparature}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}")

else:
    for wind_speed in range(5,65,5):
        wind_chill = compute_windchill(temparature,wind_speed)
        print(f"At temparature {temparature}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}")