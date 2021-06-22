def myxml(tagname, content='', **kwargs):
    """When we define a function with **kwargs, 
    we’re telling Python that we might pass any name-value pair in the style name=value. 
    These arguments aren’t passed in the normal way but are treated separately, 
    as keyword arguments. They’re used to create a dict, traditionally called kwargs, 
    whose keys are the keyword names and whose values are the keyword values."""
    attrs = ''.join([f' {key}="{value}"' for key, value in kwargs.items()])
    return f'<{tagname}{attrs}>{content}</{tagname}>'


print(myxml('tagname'))