from covid import Covid
covid = Covid()
print("Total Active Cases  in the World :", covid.get_total_active_cases())
print("Total Recovered cases in world :", covid .get_total_recovered())
print("Total deaths in world :",covid.get_total_deaths())
cases = covid.get_status_by_country_name("CHINA")
for x in cases :
    print(x, ":", cases[x])