import random
from models import Person


first_names = ["Linda", "Michael", "Carol", "John", "Diana", "Tim", "Mary", "David", "Maggie", "Jeremy", "Anna",
               "Jason"]
last_names = ["Butter", "Scotch", "Mellon", "Castle", "Smith", "Hill", "Under", "Grad", "Nob", "Whale", "Nip", "Son"]
email_providers = ["ninjamail.org", "hotsumo.com", "dojobox.net", "ninyahoo.co"]
cities = ["London", "Newcastle", "Leicester", "London", "Oxford", "Cambridge"]
genders = ["male", "female"]


def create_fake_persons(person_number=1):
    try:
        for x in xrange(person_number):
            fname = str(random.choice(first_names))
            lname = str(random.choice(last_names)) + str(random.choice(last_names).lower())
            email = "%s.%s@%s" % (fname.lower(), lname.lower(), str(random.choice(email_providers)))
            gender = str(random.choice(genders))
            city = str(random.choice(cities))
            age = random.randint(18, 105)

            Person.create(first_name=fname, last_name=lname, email=email, city=city, age=age, gender=gender)
        return True
    except:
        return False
