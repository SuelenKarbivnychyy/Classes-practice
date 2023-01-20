############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []   

    def __repr__(self):

        return f"< [Suelen, I'm pringing, yay!] melon name: {self.name}, color: {self.color}, is_seedless: {self.is_seedless}>"                 

        
    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    all_melon_types.append(musk)
    musk.add_pairing("mint")

    cas = MelonType("cas", 2003, "orange", False, False, "Casaba")
    all_melon_types.append(cas)
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")

    cren = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    all_melon_types.append(cren)
    cren.add_pairing("prosciutto")

    yw = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon" )
    all_melon_types.append(yw)
    yw.add_pairing("ice cream") 

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pair well with")
        for pairing in melon.pairings:
            print(f"- {pairing} \n")
    return None 

melon_types = make_melon_types()                        #saving the result of make_melon_types to melon_types variable
# print_pairing_info(melon_types)                         #Caling print_pairing_info with the result of make_melon_types that is saved ti melon_types variable

# print_pairing_info(make_melon_types())                calling print_pairing_info with the result of make_melon_types function



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melons_dict = {}
    for melon in melon_types:
        melons_dict[melon.code] = melon

    return melons_dict

# melon_types = make_melon_types()      
# print(make_melon_type_lookup(melon_types))        



############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def __init__(self, melon_type, shape_rating, color_rating, field, harvested_by):
        """Initialize a melon harvest."""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by
        

    def __repr__(self): 

        return f"< - Melon type: ***{self.melon_type}*** \n - Shape rating: {self.shape_rating} \n - Color rating: {self.color_rating} \n - Havested from: {self.field} \n - Havested by: {self.harvested_by}"   


    def is_sellable(self):
        """Return True if a melon is good enougth to be sold."""

        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False

#testing if is_sellable method is working
# melons_by_id = make_melon_type_lookup(melon_types)
# melon1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")  
# print(melon1.is_sellable())            


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons = []
    melons_by_id = make_melon_type_lookup(melon_types)

    melon1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
    melon2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")
    melon3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    melon4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    melon5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    melon6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    melon7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    melon8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    melon9 = Melon(melons_by_id["yw"], 7, 10, 3, "Sheila")

    melons.append(melon1)
    melons.append(melon2)
    melons.append(melon3)
    melons.append(melon4)
    melons.append(melon5)
    melons.append(melon6)
    melons.append(melon7)
    melons.append(melon8)
    melons.append(melon9)

    return melons  

# melon_types = make_melon_types()  
# print(make_melons(melon_types))



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable() == True:            
            print(f"Havested by {melon.harvested_by} from field {melon.field} (CAN BE SOLD)")
        else:
            print(f"Havested by {melon.harvested_by} from field {melon.field} (NOT SELLABLE)")    
    

# melons = make_melons(melon_types)
# print(get_sellability_report(melons))




def create_objects(file):
    """Creating a melon object for each melon in the file"""

    melons = []

    melon_types = make_melon_types()      
    melon_types_dict = make_melon_type_lookup(melon_types)  
    
    with open("harvest_log.txt") as file:        
        file_content = file.readlines()        

        for line in file_content:
            melon = line.rstrip().split(" ")

            melon_type_code = melon[5] 
            melon_type_instance = melon_types_dict[melon_type_code]

            shape_rating = melon[1] 
            color_rating = melon[3] 
            field = melon[-1] 
            harvested_by = melon[8]            

            melon_obj = Melon(melon_type_instance, shape_rating, color_rating, field, harvested_by)
            melons.append(melon_obj)

    return melons 

result = create_objects("harvest_log.txt")
print(result)
