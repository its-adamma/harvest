
############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""
# object impl., similar to self

    def __init__(self, name, code, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""

        self.pairings = []
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller


        # Fill in the rest

    def add_pairing(self, pairing):
        
        """Add a food pairing to the instance's pairings list."""
    
        self.pairings.append(pairing)

        #REMOVE ME, TEST ONLY
        #print(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        #self.code = new_code
        #print(f'Here is the new code {new_code}')

        # Fill in the rest

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('Muskmelon', 'musk', 1998, 'green', True, True)
    musk.add_pairing("Mint")
    musk.add_pairing("Chicken")
    all_melon_types.append(musk)

    cas = MelonType('Casaba', 'cas', 1995, 'red', False, True)
    cas.add_pairing("Mint")
    cas.add_pairing("Chicken")
    all_melon_types.append(cas)

    cren = MelonType('Crenshaw', 'cren', 1996, 'green', False, True)
    cren.add_pairing("proscuitto")
    cren.add_pairing("Chicken")
    all_melon_types.append(cren)

    yw = MelonType('Yellow Watermelon', 'yw', 2013, 'yellow', True, True)
    yw.add_pairing("proscuitto")
    yw.add_pairing("Chicken")
    all_melon_types.append(yw)


  #  all_melon_types.append(MelonType('musk', 1998, 'green', True, True).add_pairing("Mint"))
  #  all_melon_types.append(MelonType('musk', 1998, 'green', True, True).add)
 #   all_melon_types.append(MelonType('musk', 1998, 'green', True, True))


    # Fill in the rest

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    #If statement to loop through list
    # Fill in the rest
    #for melon in melon_types:
   #     for pair in melon.pairings:
  #          print(f'{melon.name}' + ' pairs with ' + f'{pair}')



    for melon in melon_types:
        print(f'{melon.name}' + ' pairs with ' + f'{melon.pairings}')



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melons_dict = {}
    for melon in melon_types:
        if melon.id not in melons_dict:
            melons_dict[melon.id] = melon      
    return melons_dict

    print_pairing_info(make_melon_types())

    make_melon_type_lookup(melon_types())
    # no output 
############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 


