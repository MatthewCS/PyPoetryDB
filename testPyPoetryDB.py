import pyPoetryDB

poem = pyPoetryDB.getPoem("text", author="Charles Swinburne")
titles = pyPoetryDB.getAllTitles()
titledPoem = pyPoetryDB.getPoem(title=titles[50])

print(titles[50])
print("\n\t" + "\n\t".join(titledPoem.lines))

print("#######################################################################")

poemsList = pyPoetryDB.Poems()
for t in titles:
    poemsList.addPoem(pyPoetryDB.getPoem(title=t))
    if len(poemsList) >= 25:
        break

foundPoem = poemsList.search(titles[15])
print(foundPoem.title)
print("\n\t" + "\n\t".join(foundPoem.lines))

print("#######################################################################")

print("str() representation of foundPoem:")
print("+=+=+=+=+=+=+=+=+=+")
print(str(foundPoem))

print("#######################################################################")

poemsList.sort(sortby="linecount")
print("Sorted by linecount!")
print("Found {} poems 24 lines long.".format(len(poemsList.searchAll("24"))))

print("#######################################################################")
fourty_line_poem = pyPoetryDB.getPoem(linecount="40")
print("Here is a 40-line-long poem:\n{0.title}".format(fourty_line_poem))
print("\n\t" + "\n\t".join(fourty_line_poem.lines))

