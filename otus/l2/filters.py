""" filters
takes two args - filtering function and list of vlues to be filtered

  """


my_nums = range(-10, 20, 3)
print(my_nums[:])

filter(lambda x: -7 < x < 10, my_nums)

print(type(filter(lambda x: -7 < x < 10, my_nums)))

print(list(filter(lambda x: -7 < x < 10, my_nums)))
