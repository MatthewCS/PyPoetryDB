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
print("Found {} poems 9 lines long.".format(len(poemsList.searchAll("9"))))
