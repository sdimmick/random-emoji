#!/usr/bin/env python
import re

def main():
    with open('emojilist.php') as f:
        print '['

        for line in f:
            match = re.search('&#x.*?;', line)
            if match != None:
                print "    '%s'," % match.group(0)

        print ']'


if __name__ == '__main__':
    main()

