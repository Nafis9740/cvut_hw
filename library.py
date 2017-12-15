def load_library(book):
    bookdic = {}
    with open(book, 'r') as f:  # open the file
        content = f.read().splitlines()   # put the lines to a variable.
        for i in content:
            s = i.split('|')
            bookdic[s[0]] = s[1]
        return bookdic

def index_by_author(d):
     newdict = {}
     for k, v in d.items():
        newdict.setdefault(v, []).append(k)
     return newdict

def report_author_counts(books, report):
    f = open(report, "w+")
    all = load_library(books)
    indexedAll = index_by_author(all)

    total = 0
    for k, v in indexedAll.items():
        f.write(k + ": " + str(len(v)) + "\n")
        total += len(v)
    f.write("TOTAL BOOKS: " + str(total))
    f.close()

