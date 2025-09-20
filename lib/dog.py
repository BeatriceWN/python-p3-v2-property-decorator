APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        """Return the dog's name"""
        return self._name

    @name.setter
    def name(self, value):
        """Validate and set the dog's name"""
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            raise ValueError("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        """Return the dog's breed"""
        return self._breed

    @breed.setter
    def breed(self, value):
        """Validate and set the dog's breed"""
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            raise ValueError("Breed must be in list of approved breeds.")