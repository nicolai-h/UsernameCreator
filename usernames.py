import sys, getopt
from itertools import permutations


combining_chars = ["",".", "-", "_", "@", " "]

def first(name):
    usernames = []
    for i in combining_chars:
        usernames.append(name[0]+i)
    
    return usernames


def firstl(name):
    usernames = []
    for i in combining_chars:
        usernames.append(name[0] + i + name[-1][0])
    
    return usernames


def flast(name):
    usernames = []
    for i in combining_chars:
        usernames.append(name[0][0] + i + name[-1])
    
    return usernames


def firstlast(name):
    usernames = []
    for i in combining_chars:
        usernames.append(name[0] + i + name[len(name)-1])
    
    return usernames


def fl(name):
    usernames = []
    for i in combining_chars:
        usernames.append(name[0][0] + i + name[-1][0])
    
    return usernames


def main(argv):
    inputfile = []
    try:
        opts, args = getopt.getopt(argv,"i:")

    except getopt.GetoptError:
        print('usernames.py -i <infile> > <outfile>')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-i':
            inputfile = arg
        else:
            print('usernames.py -i <infile> > <outfile>')
            sys.exit()

    with open(inputfile, "r") as f:
        data = f.readlines()
        for name in data:
            name = name.strip().split()
            if len(name) < 2:
                name += name

            name = list(permutations(name, 2))
            for n in name: # john doe
                print(*first(n), sep="\n") # john, john., john-, john_, john@, john 
                print(*firstl(n), sep="\n") # johnd,john.d, john-d, john-d, john@d, john d
                print(*flast(n), sep="\n") # jdoe, j.doe, j-doe, j_doe, j@doe, j doe
                print(*firstlast(n), sep="\n") # johndoe, john.doe, john-doe, john_doe, john@doe, john doe
                print(*fl(n), sep="\n") # jd, j.d, j-d, j_d, j@d, j d


if __name__ == '__main__':
    main(sys.argv[1:])
