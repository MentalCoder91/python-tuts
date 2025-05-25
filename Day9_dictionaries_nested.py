capitals = {
    'France': "Paris",
    'Germany': "Berlin"
}
#
# travel_log = {
#
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }
#
# # Print lille
# print(travel_log["France"][1])

# Print D
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "num_times_visited": 3,
        "cities_visited": ["Stuttgart", "Berlin"]
    }
}

print(travel_log['Germany']['cities_visited'][0])
