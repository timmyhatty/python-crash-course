# 8-5: Cities

"""
TO DO:
    - Write a function called describe_city():
        * The function should accept two parameters: CITY and COUNTRY
            * COUNTRY should have a default DEFAULT PARAMETER
        * The function should print a simple sentence about the city and country
    - Call the function three (3) times:
        * At least one call should not use the default country parameter   
"""

# Function definition
def describe_city(city, country='Netherlands'):
    """This program prints information about cities and countries"""

    print(f'{city.title()} is in {country.title()}')

describe_city('amsterdam')
describe_city(city='detroit', country='united states')
describe_city(country='canada', city='montreal')