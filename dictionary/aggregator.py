# -----------------------------------------------------------------------------
# Name:        aggregator.py
# Purpose:     CS 21A - implement a simple general purpose aggregator
#
# Author: Luyan Deng
# Date: 03/08/2018
# -----------------------------------------------------------------------------
"""
Implement a simple general purpose aggregator

Usage: aggregator.py filename topic
filename: input file that contains a list of the online sources (urls).
topic:  topic to be researched and reported on
"""

import urllib.request
import urllib.error
import re
import sys


def reference(text,topic):
    """
    picks up all references to the given topic outside html tags.
    :param text:
    :param topic(string): the word we are searching for
    :return:
    all_references(string) - all references to the topic outside html tags
                            separated by new line characters.
                            an empty string if there are no such references
    """
    all_references = ''
    # extract text outside html tags containing the topic word
    pattern = r'\>([^\<]*\b{}\b.*?)\<'.format(topic)
    matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
    if matches:
        all_references = '\n'.join(matches)

    return all_references


def new_file(all_references, url, topic):
    """

    :param all_references(str): all references to the topic outside html tags
    :param url (str): each line in the specific file
    :param topic(str): the word we are searching for
    :return: None
    """
    if all_references != '':
        with open(topic + 'summary.txt', 'a',
                  encoding='utf-8') as output_file:
            output_file.write('Source url: ' + url + all_references
                              + '-' * 32)
    else:
        # created an empty file since no urls include any reference
        with open(topic + 'summary.txt', 'a',
                  encoding='utf-8') as output_file:
            output_file.write('')


def main():
    #  check for the right number of arguments
    if len(sys.argv) != 3:
        print('Error:  invalid number of arguments \nUsage: aggregator.py '
              'filename topic')
    else:
        filename = sys.argv[1]  # get the filename argument
        try:
            topic = sys.argv[2]  # get the reference argument
        except ValueError:
            print('Error:  invalid number of arguments \nUsage: '
                  'aggregator.py filename topic')
        else:
            with open(filename, 'r', encoding='utf-8') as my_file:
                # read the file one line at a time
                for line in my_file:
                    url = line

                    try:
                        with urllib.request.urlopen(url) as url_file:
                            # read the web page and decode it
                            text = url_file.read().decode('UTF-8')
                            # call the reference function
                            all_references = reference(text, topic)
                            print(all_references)
                            # put the outputs in a new text file
                            new_file(all_references, url, topic)
                    except urllib.error.URLError as url_err:
                        print('Error opening url:', url, url_err)
                    except UnicodeDecodeError as decode_err:
                        print('Error decoding url: ', url, decode_err)


if __name__ == '__main__':
    main()
