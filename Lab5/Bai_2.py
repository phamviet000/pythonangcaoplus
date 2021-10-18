import Bai_1
canada = Bai_1.Country('Canada',34482779,9984670)
usa = Bai_1.Country('United States of America', 313914040,9826675)
mexico = Bai_1.Country('Mexico', 112336538, 1943950)
countries = [canada,usa,mexico]
class Continent(Bai_1.Country):
    def __init__(self,name,countries):
        self.name=name
        self.countries = countries
    def total_population(self):
        total=0
        for value in self.countries:
            total += value.population
        return total
    def __str__(self):
        string = self.name + '\n'
        for country in self.countries:
            string += '{} has a population of {} and is {} square km.'.format(country.name, country.population, country.area) + '\n'
        return string
north_america = Continent('North America', countries)
print(north_america.name)
for country in north_america.countries:
    print(country)
print(north_america.total_population())
print(north_america)
