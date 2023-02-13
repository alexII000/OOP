import insectCLASS as i

#this is creating an instance of the insect class
mosquito = i.Insect('mosquito',2,4)
housefly = i.Insect('housefly',2,4)

mosquito.flight_length()
housefly.flight_length()


def main():

    my_insect = i.Insect()

    print(f'The {mosquito.get_name()} flies for:', {mosquito.get_miles()})
    print(f'The {housefly.get_name()} can fly up to {housefly.getmiles()})


main()
