from main import People

our_people =People.select()
for people in our_people:
    print(people.name, people.phonenumber, people.email, people.county, people.gender,
          people.religion, people.password)