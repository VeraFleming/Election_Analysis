counties = ['Arapahoe', 'Denver', 'Jefferson']
if "El Paso" in counties:
    print('El Paso is in the list of counties')
else:
    print('El Paso is not in the list of counties')

if 'Arapahoe' in counties or 'El Paso' in counties:
    print('Apahoe and El Paso is in the list of counties')
else:
    print('Apahoe or El Paso is not in the list of counties')

counties_dict = dict()

counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print (county, voters)

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")




voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


for county_dict in voting_data:
    print(county_dict['county'])

   

candidate_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))


message_to_candidate = (
        f"You recieved {candidate_votes:,} number of votes."
        f"The total number of votes in the election was {total_votes:,}."
        f"you recieved {candidate_votes / total_votes *100:.2f}% of the total votes.")
    def new_func(message_to_candidate):
    print(message_to_candidate)

new_func(message_to_candidate)