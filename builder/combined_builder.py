# The base class representing a person with address and job information
class Person:
    def __init__(self):
        # Address information
        self.street_address = None
        self.postal_code = None
        self.city = None

        # Job information
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return (f'Address: {self.street_address}, {self.postal_code}, {self.city}\n' +
                f'Employed at: {self.company_name} as a {self.position} earning {self.annual_income}')


# The base builder class
class PersonBuilder:
    def __init__(self, person=None):
        # Avoid shared mutable default by using None
        self.person = person or Person()

    def build(self):
        # Finalizes the building process and returns the Person object
        return self.person

    @property
    def works(self):
        # Switches to the job-building interface
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        # Switches to the address-building interface
        return PersonAddressBuilder(self.person)


# Sub-builder for building job-related properties
class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self  # Enables method chaining

    def as_a(self, position):
        self.person.position = position
        return self  # Enables method chaining

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self  # Enables method chaining


# Sub-builder for building address-related properties
class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self  # Enables method chaining

    def with_postcode(self, postal_code):
        self.person.postal_code = postal_code
        return self  # Enables method chaining

    def in_city(self, city):
        self.person.city = city
        return self  # Enables method chaining


# Usage of the combined builder pattern
p_b = PersonBuilder()
person = p_b\
    .lives\
        .at('1111 4st Ave SW')\
        .in_city('Calgary')\
        .with_postcode('T2S3H9')\
    .works\
        .at('AMAZON')\
        .as_a('Web Developer')\
        .earning(200_000)\
    .build()

print(person)


