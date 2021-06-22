def reverse_lines(infilename, outfilename):
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
        for one_line in infile: 
            # s[::-1] means that we want all of the elements of s, from the start to the end, but I use a step size of –1, which returns a reversed ver- sion of the string.
            outfile.write(f'{one_line.rstrip()[::-1]}\n')