# lab1-boxpyramid.py - demonstrate the essentials of a while loop using a pyramid of boxes
# 3-clause BSD License

# Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.

# Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

# The figure illustrates the rule used by the builders:

#   *
#  * *
# * * *

# blocks = 6
# height = 3 

# sample_input = blocks: 3
# expected_output = height of the blocks: 2

#blocks = int(input("Enter the number of blocks: "))

blocks = 6
height = 0
layer = 1

height = blocks * layer * (layer + 1) // 2

""" while layer <= blocks:
    height += 1
    blocks -= layer
    layer += 1
    # each lower layer contains one block more than the layer above. """

print("The height of the pyramid:", height) # 3
    