
# helloagain
import sys
# sys.argv is a list. sys.argv[0] is always the module file name.
def main():
    print('this is sys.argv:', sys.argv)
    if len(sys.argv)!= 3:  #  check for the right number of arguments
        print('Please try again:')
    else:
        name = sys.argv[1] # get the name argument
        #  the first argument specified on the command line after the filename.
        try:
            number = int(sys.argv[2]) # get the number argument
        except ValueError:
            print('Please try again: helloagain.py name number')
        else: # print the name the specified number of times
            for i in range(number):
                print('Hello',name)
if __name__ == '__main__':
    main()
