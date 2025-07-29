#Write a Python function that accepts a hyphen-separated sequence of colors as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically.

def sort_colors(color_sequence):
    color_list = color_sequence.split('-')
    sorted_colors = sorted(color_list)
    sorted_sequence = '-'.join(sorted_colors)
    return sorted_sequence

input1 = "green-red-yellow-black-white"
output1 = sort_colors(input1)
print("Sample output 1:", output1)

input2 = "PINK-BLUE-TAN-PURPLE"
output2 = sort_colors(input2)
print("Sample output 2:", output2)
