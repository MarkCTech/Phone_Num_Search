import re
import os

def search(file, pattern):
    f = open(file, 'r')
    text = f.read()
    match = re.search(pattern, text)

    if match:
        return match
    else:
        pass


def main():

    results = []
    pattern = r'\d{3}-\d{3}-\d{4}'

    for folder, subs, files in os.walk(os.getcwd() + '/extracted_content'):
        for f in files:
            full_path = folder + '/' + f
            results.append(search(full_path, pattern))
    for r in results:
        if r != None:
            print(r.group())

if __name__ == '__main__':
    main()
