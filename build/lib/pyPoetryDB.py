"""

    A simple module for accessing data from PoetryDB.
    Made by MatthewCS in the Winter of early 2018.
    http://poetrydb.org/index.html

"""


""" This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>. """

import urllib.request
import urllib.parse
import urllib.error
import json
from random import choice



class Poem:
    """
        A simple class for storing poetry data, either in json or txt format.
    """
    filetype = ""
    author = ""
    title = ""
    lines = []
    rawdata = ""
    linecount = 0

    def __init__(self, author, title, lines, rawdata, line_count=len(lines), file_type="json"):
        """
            Create a new Poem object.

            Parameters:
                author:     author of the poem
                title:      title of the poem
                lines:      array containing the poem's lines
                rawdata:    the data contained by the poem's file on poetrydb
                line_count: the number of lines in the poem (equal to len(lines) by default)
                file_type:  the type of file this poem is ("json" (default) or "txt"(/"text"))
        """
        if file_type != "json" and file_type != "txt":
            if file_type == "text":
                file_type = "txt"
            else:
                raise ValueError("file_type ({}) must be either json or txt(/text)".format(file_type))
                pass

        self.filetype = file_type
        self.author = author
        self.title = title
        self.lines = lines
        self.rawdata = rawdata
        self.linecount = len(lines)

    def __str__(self):
        return "author:\t{0}\ntitle:\t{1}\nlines:\n{2}\nlinecount:\t{3}\nfiletype:\t{4}".format(self.author, self.title, self.lines, self.linecount, self.filetype)

class Poems:
    """
        A simple class for storing Poem objects.
    """
    poemlist = []
    sortedby = ""
    
    def __init__(self, poetry=[], sortby="title"):
        """
            Creates a new Poems object from the given list of Poem objects, and sorts it.

            Parameters:
                poetry:     a list of poems to be passed. Empty by default
                sortby:     a string value ("title" by default) acting as Poems.sort's sortby parameter.
        """
        for p in poetry:
            if not isinstance(p, Poem):
                raise ValueError("poetry must be a list of Poem objects, and only of Poem objects.")
            else:
                poemlist.append(p)
        self.sort(sortby)
        self.sortedby = sortby

    def addPoem(self, poem, sortby="title"):
        """
            Add a given Poem to the Poems object, and sort the Poems afterward.

            Parameters:
                poem:       a poem to add
                sortby:     a string valie ("title" by default) acting as Poems.sort's sortby parameter.
        """
        if not isinstance(poem, Poem):
            raise ValueError("poetry must be a Poem object, and only a Poem object.")
            pass
        else:
            self.poemlist.append(poem)
            self.sort(sortby)
            self.sortedby = sortby
            pass

    def sort(self, sortby="title"):
        """
            Sorts the list of Poem objects in ascending order by the given argument.

            Parameters:
                sortby:     what to sort the poetry list by. Can be "title" (default), "author", or "linecount"
        """
        if len(self.poemlist) == 0:
            pass    #poemlist is empty, cannot be sorted

        if sortby != "title" and sortby != "author" and sortby != "linecount":
            raise ValueError("sortby ({}) must be either \"title\", \"author\", or \"linecount\"".format(sortby))
            pass

        if sortby == "title":
            self.poemlist = sorted(self.poemlist, key=lambda p: Poem.title)
            self.sortedby = sortby
            pass
        elif sortby == "author":
            self.poemlist = sorted(self.poemlist, key=lambda p: Poem.author)
            self.sortedby = sortby
            pass
        else:
            self.poemlist = sorted(self.poemlist, key=lambda p: Poem.linecount)
            self.sortedby = sortby
            pass

    def search(self, searchfor):
        """
            Searches the list of Poem objects based on the given parameter to find a single matching poem
            This is accomplished through an implementation of the binary search algorithm
            
            Parameters:
                searchfor:      a string to search for (title, author, linecount), checking based on how the array was
                                last sorted. If the array was last sorted by linecount, it will automatically convert
                                the given string to an int.

            Returns:
                A Poem object based on what was searched for, or None if nothing was found
        """
        first = 0
        last = len(self.poemlist) - 1
        while first <= last:
            mid = (first + last) // 2
            if self.sortedby == "title":
                if self.poemlist[mid].title == searchfor:
                    return self.poemlist[mid]
                elif self.poemlist[mid].title < searchfor:
                    first = mid
                else:
                    last = mid
            elif self.sortedby == "author":
                if self.poemlist[mid].author == searchfor:
                    return self.poemlist[mid]
                elif self.poemlist[mid].author < searchfor:
                    first = mid
                else:
                    last = mid
            else:   #linecount
                if self.poemlist[mid].linecount == int(searchfor):
                    return self.poemlist[mid]
                elif self.poemlist[mid].linecount < int(searchfor):
                    first = mid
                else:
                    last = mid

        return None

    def searchAll(self, searchfor):
        """
            Searches the list of Poem objects based on the given parameter to find a list of matching poem
            This is accomplished through an implementation of the linear search algorithm
            
            Parameters:
                searchfor:      a string to search for (title, author, linecount), checking based on how the array was
                                last sorted. If the array was last sorted by linecount, it will automatically convert
                                the given string to an int.

            Returns:
                A list of Poem objects based on the given parameter, or an empty list if nothing was found
        """

        matches = []
        found = False
        for p in self.poemlist:
            if self.sortedby == "title":
                if p.title == searchfor:
                    matches.append(p)
                    found = True
            elif self.sortedby == "author":
                if p.author == searchfor:
                    matches.append(p)
                    found = True
            elif self.sortedby == "linecount":
                if p.linecount == int(searchfor):
                    matches.append(p)
                    found = True
            elif found: #Last matching poem found
                return matches

        return matches
    
    def getRandom(self, **kwargs):
        """
            Gets a random Poem object from the PoemList. kwargs may be added to search by given values, and if none
            are passed, returns a random Poem regardless of that Poem attributes.

            Parameters:
                kwargs:
                    author:     poem author to search for (Will also search for poetry by authors with the same name)
                    title:      string which must be contained by a poem's title if it is to be returned
                    min_lines:  minimum number of lines per poem
                    max_lines:  maximum number of lines per poem

            Returns:
                A random Poem chosen by the kwargs
        """
        author = ""
        title = ""
        min_lines = -1
        max_lines = -1
        randPoemCandidates = []

        if len(kwargs.items()) == 0:    #No kwargs passed
            return choice(self.poemlist)

        for key, value in kwargs.items():
            if key == "author":
                author = value  
            elif key == "title":
                title = value
            elif key == "min_lines":
                min_lines = value
            elif key == "max_lines":
                max_lines = value
            else:
                raise TypeError("{} is not a valid kwarg.".format(key))
        
        if min_lines != -1 and max_lines != -1 and min_lines > max_lines:
            raise ValueError("min_lines ({0})  may not be greater than max_lines ({1})".format(min_lines, max_lines))
            pass
        
        for p in self.poemlist:
            if author in p.author and title in p.title:
                if p.linecount >= min_lines:
                    if max_lines == -1 or p.linecount <= max_lines:
                        randPoemCandidates.append(p)

        if len(randPoemCandidates) == 0:
            return None

        return choice(randPoemCandidates)

    def __len__(self):
        """
            Gets the total number of Poem objects stored by this Poems object
        """
        return len(self.poemlist)
    
def getPoem(file_type="json", **kwargs):
    """
        Parameters:
            file_type:  type of poetry file type to return. Can be "json" (default) or "txt"/"text".

            kwargs:
                author:     poem author to search for
                title:      poem title to tearch for
                line_count: number of lines to search for
        Returns:
            A new Poem from the given parameters.

        Raises:
            TypeErrors for non-valid constructors
            ValueErrors for a bad value for line_count
    """

    # initialize the variables

    if file_type != "json" and file_type != "txt" and file_type != "text":
        raise ValueError("file_type ({}) must be either json or txt(/text)".format(file_type))
        pass
    
    author = ""
    title = ""
    line_count = None
    url_string = "http://poetrydb.org/"
    url_parameters_left = []
    url_parameters_right = []
    poem = None

    
    for key, value in kwargs.items():
        if key == "author":
            author = value
        elif key == "title":
            title = value
        elif key == "line_count":
            line_count = value
        else:
            raise TypeError("{} is not a valid kwarg.".format(key))

    if file_type == "txt":
        file_type = "text"

    # fetch the poem from poetrydb

    if author != "":
        url_parameters_left.append("author")
        url_parameters_right.append(author)
    if title != "":
        url_parameters_left.append("title")
        url_parameters_right.append(title)
    if line_count != None:
        if line_count < 0:
            raise ValueError("line_count ({}) cannot be less than 0.".format(max_lines))
            pass
        url_parameters_left.append("linecount")
        url_parameters_right.append(str(linecount))

    url_string += ",".join(url_parameters_left) + "/"
    url_string += urllib.parse.quote(";".join(url_parameters_right)) + "/"
    url_string += "all." + file_type

    try:
        poem = urllib.request.urlopen(url_string).read()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        else:
            raise e

    # return time!

    if file_type == "json":
        try:
            jsonPoem = json.loads(poem.decode())[0]
        except: #404 not found, usually
            jsonPoem = json.loads(poem.decode())
            return jsonPoem
        return Poem(jsonPoem["author"], jsonPoem["title"], jsonPoem["lines"], str(jsonPoem), line_count=jsonPoem["linecount"])
    else:
        lines = poem.decode().split("\n")
        return Poem(lines[lines.index("author")+1], lines[lines.index("title")+1], lines[lines.index("lines")+1:lines.index("linecount")],
                    lines, line_count=lines[lines.index("linecount")+1], file_type = file_type)

def getAllTitles():
    """ Returns all titles currently in http://poetrydb.org/title """
    titlesString = urllib.request.urlopen("http://poetrydb.org/title").read()
    jsonTitles = json.loads(titlesString.decode())["titles"]
    return jsonTitles

def getAllAuthors():
    """ Returns all authors currently in http://poetrydb.org/author """
    authorsString = urllib.request.urlopen("http://poetrydb.org/author").read()
    jsonAuthors = json.loads(authorsString.decode())["authors"]
    return jsonAuthors
