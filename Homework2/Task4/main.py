import random


def random_array(number_of_pupils):
    return sorted([random.randint(60, 190) for el in range(number_of_pupils)], reverse=True)


def place_identifier(school_class, user_height):
    if user_height in school_class:
        start_index = school_class.index(user_height)
        height = user_height
        while height == user_height:
            start_index += 1
            height = school_class[start_index]
        return start_index
    else:
        half_school_class = school_class[:]
        count_iterations = 0
        while True:
            count_iterations += 1
            pupil_middle_index = int(len(half_school_class) / 2)
            neighbor_height = half_school_class[pupil_middle_index]
            if user_height < neighbor_height and len(half_school_class) != 1:
                half_school_class = half_school_class[pupil_middle_index:]
                print(half_school_class)
                continue
            if user_height > neighbor_height and len(half_school_class) != 1:
                half_school_class = half_school_class[:pupil_middle_index]
                print(half_school_class)
                continue
            print(count_iterations)
            return school_class.index(half_school_class[0]) + 1


my_school_class = random_array(50)
print(my_school_class)
print(place_identifier(my_school_class, 120))
