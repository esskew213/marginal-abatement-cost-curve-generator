def create_colour_floats(macc_input_data):
    unique_categories = list({row.category for row in macc_input_data})
    unique_categories.sort()
    print(unique_categories)
    unique_colour_floats = [i * 1 / (len(unique_categories)) for i, _ in enumerate(unique_categories)]
    colour_legend = {key: value for key, value in zip(unique_categories, unique_colour_floats)}
    colour_floats = [colour_legend[row.category] for row in macc_input_data]
    print(colour_floats)
    return colour_floats