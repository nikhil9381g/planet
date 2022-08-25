class Planet:
    def __init__(self,name,surface_gasesno,moons,planet_rings):
        self.name = name
        self.surface_gasesno_of_moons = surface_gasesno
        self.moons = moons
        self.palnet_rings = planet_rings
    def count_moon(moons,planet_rings):
        if planet_rings > "Yes":
            return moons
    def max_no_gas(surface_gasesno):
        list_a = [surface_gasesno]
        counting={}
        for i in list:
            counting[i] = list_a.count[i]
        return counting


values = [["Mercury", 0, "No"],
["Venus" ,"Carbon Dioxide", "Nitrogen",0, "No"],
["Earth", "Nitrogen", "Oxygen", 1, "No"],
["Jupitor", "Hydrogen", "Helium", 79, "Yes"],
["Saturn", "Hydrogen", "Helium", 83 ,"Yes"],
["Uranus" "Hydrogen", "Helium", "Methane", 27, "Yes"]]


def mapping_data(i):
    Planet1 = Planet(i)

for i in values:
    mapping_data(i)

print(mapping_data)
