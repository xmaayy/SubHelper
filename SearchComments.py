import re
import csv
import time
from collections import Counter

def AllTerms(comment_file, term_file):
    term_freq = Counter(TermFinder(comment_file, term_file))
    print(term_freq)

def TopN(comment_file, term_file,N):
    term_freq = Counter(TermFinder(comment_file, term_file)).most_common(N)
    print(term_freq)

def TermFinder(comment_file, term_file):
    comment_list, term_list = GetLists(comment_file, term_file)
    found_list = []
    term_finder = re.compile(r'\b(?:%s)\b' % '|'.join(term_list))

    for comment in comment_list:
            found = term_finder.match(comment);
            if found:
                found_list.append(found.group(0))
    return found_list

def GetLists(comment_file, term_file):
    comment_list = []
    term_list = []
    with open('./DATA/'+comment_file, 'r') as commentFile:
        reader = csv.reader(commentFile)
        for idx,row in enumerate(reader):
            comment_list.append(str(row[0]))

    with open('./DATA/'+term_file, 'r') as termFile:
        reader =  csv.reader(termFile)
        for idx,row in enumerate(reader):
            term_list.append(str(row[0]))

    return comment_list, term_list
