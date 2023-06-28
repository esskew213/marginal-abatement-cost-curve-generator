import matplotlib.pyplot as plt
from itertools import accumulate
from create_colour_floats import create_colour_floats
from pydantic_classes import AbatementMeasure
from decimal import Decimal
from choose_colour_map import choose_colour_map


def get_macc_plot(macc_input_data: list[AbatementMeasure]):
    fig = plt.figure()
    bar_width = [row.abatement for row in macc_input_data]
    y_coord = [row.marginal_cost for row in macc_input_data]
    category_labels = [row.category for row in macc_input_data]
    x_coord = [Decimal(0)] + list(accumulate(bar_width))[:-1]
    colour_floats = create_colour_floats(macc_input_data)
    colour_map = choose_colour_map()
    my_cmap = plt.get_cmap(colour_map)
    plt.bar(
        x=x_coord,
        height=y_coord,
        width=bar_width,
        align='edge',
        linewidth=1,
        edgecolor='black',
        color=my_cmap(colour_floats),
        label=category_labels,

    )
    plt.title("Marginal Abatement Cost Curve")
    plt.legend(list(dict.fromkeys(category_labels)))
    plt.xlabel('Abatement')
    plt.ylabel('Marginal Cost')
    print('MAC curve generated. Please close the image preview to proceed.')
    plt.show()
    return fig