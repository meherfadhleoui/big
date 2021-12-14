import re
from termcolor import colored, cprint
import sys
from pyspark import SparkContext
import os

if __name__ == "__main__":
    try:
        x = int(sys.argv[1])
    except:
        print('invalid args , arg must be an integer ')
        exit(0)

    # create Spark context with Spark configuration
    path = os.path.join("access.log")
    sc = SparkContext.getOrCreate()

    # read input text file to RDD
    lines = sc.textFile(path)

    # collect the RDD to a list
    python_lines = lines.map(lambda line: re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)).filter(
        lambda line: len(line) > 0).map(lambda line: line[0]).map(lambda line: line.replace("https", "http"))

    i = 0
    print('\n')
    for key, value in sorted(python_lines.countByValue().items(), key=lambda item: item[1], reverse=True):
        # print(style.MAGENTA + key , style.GREEN + " : " ,style.YELLOW + str(value) )

        cprint(key, 'magenta', attrs=['bold'], end=' ')
        cprint(" : ", 'green', attrs=['bold'], end=' ')
        cprint(value, 'yellow', attrs=['bold'], end=' ')
        print('\n ')

        i = i+1
        if (i == x):
            break
