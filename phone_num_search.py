import re
import os

def main():

    results = []
    text = ''
    pattern = r'\d{3}-\d{3}-\d{4}'
    directory = os.walk(os.getcwd() + '/extracted_content')

    for folder, subs, files in directory:

        for f in files:
            full_path = folder + '/' + f
            f = open(full_path, 'r')
            text = f.read()

            results.append(re.search(pattern, text))

    for r in results:
        if r != None:
            print(r.group())

if __name__ == '__main__':
    main()