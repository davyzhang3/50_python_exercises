import operator


PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_records(list_of_tuple):
    output = []
    # We can do that in str.format by adding a colon (:) character after 
    # the index we wish to display. Thus, {1:10} tells Python to display 
    # the item with index 1, inserting spaces if the data contains fewer 
    # than 10 characters. Strings are left aligned by default, such that 
    # the names will be displayed flush left within their columns.
    template = "{1:10} {0:10} {2:5.2f}"
    for person in sorted(list_of_tuple, key=operator.itemgetter(1,0)):
        output.append(template.format(*person)) # *person make it not a tuple, but the elements of that tuple. This means that we're passing three separate arguments to str.format, which we can access via {0}, {1}, {2}
    return output

print('\n'.join(format_sort_records(PEOPLE)))