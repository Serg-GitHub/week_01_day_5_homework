# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash_amount):
    pet_shop["admin"]["total_cash"]= (pet_shop["admin"]["total_cash"]+cash_amount)


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pet_sales):
     pet_shop["admin"]["pets_sold"] = (pet_shop["admin"]["pets_sold"]+pet_sales)

def get_stock_count(pet_shop):
   return len(pet_shop ["pets"])

def get_pets_by_breed(var_input, breed):
    breed_count = []

    for pet in var_input["pets"]:
        if pet ["breed"] == breed:
            breed_count.append(breed)
    return breed_count

def find_pet_by_name(var_input, name_input): 
    for pet in var_input["pets"]: 
        if pet["name"] == None: 
          return None 

        elif pet ["name"] == name_input: 
             return pet

def remove_pet_by_name(var_input, pet_name_string):
    pet_name_string == ("Arthur"):
    for pet in var_input["pets"]:
        if pet_name_string == ("Arthur"):
           return pet.pop("Arthur")
