import re
import sys
import os
from pyspark import SparkContext
from termcolor import colored, cprint

if __name__ == "__main__":
    try:
        x = int(sys.argv[1])
    except:
        print('invalid args , arg must be an integer ')
        exit(0)

    path = os.path.join("access.log")
    sc = SparkContext.getOrCreate()

    lines = sc.textFile(path)

    list_websites = lines.map(lambda line: re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)).filter(
        lambda line: len(line) > 0).map(lambda line: line[0]).map(lambda line: line.replace("https", "http"))

    i = 0
    for key, value in sorted(list_websites.countByValue().items(), key=lambda item: item[1], reverse=True):
        cprint(key, 'green', attrs=['bold'], end=' ')
        cprint(" : ", 'blue', attrs=['bold'], end=' ')
        cprint(value, 'yellow', attrs=['bold'], end=' ')
        print('\n ')
        i = i+1
        if (i == x):
            break
