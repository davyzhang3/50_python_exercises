# # binary mode is used for reading PDF or JPEG files
# # you don't want to read the file per line because there is not \n in a binary file. 
# # Insetead you whould be using the read method to retrieve a fiexed number of bytes.
# # when read tetruns 0 bytes, you know that you're at teh end of the file

# with open(filename, 'rb') as f:
#     while True:
#         one_chunk = f.read(1000)
#         if not one_chunk:
#             break
#         print(f'This chunk contains {len(one_chunk)} bytes')




from io import StringIO

fakefile = StringIO('''
nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
''')

def get_final_line(filename):
    final_line = ''
    for current_line in fakefile:
        final_line = current_line
    return final_line

print(get_final_line('fakefile'))