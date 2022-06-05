from typing import List

def find_maximum_distance(number_of_cities: int, cities_with_train_station: List[int]) -> int:
    distance = 0
    maximum_distance = min(cities_with_train_station)

    hasStation = [False] * number_of_cities
    for i in cities_with_train_station:
        hasStation[i] = True

    for i in range(number_of_cities):
        if hasStation[i] == True:
            maximum_distance = max((distance + 1) // 2, maximum_distance)
            distance = 0
        else:
            distance = distance + 1
    return max(maximum_distance, distance)

if __name__ == "__main__":
    # These are some of test cases. When evaluating the task, more will be added:
    assert find_maximum_distance(number_of_cities=3, cities_with_train_station=[1]) == 1
    assert find_maximum_distance(number_of_cities=4, cities_with_train_station=[3]) == 3
    assert (find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 4]) == 2)
    print("ALL TESTS PASSED")