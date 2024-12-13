import pytest
from producerConsumer import *

def test_OneOperations():

    listUrl = []

    listUrl.append("https://en.wikipedia.org/wiki/Rubber_duck")
    
    operations(listUrl)

def test_Eight_Operations():

    listUrl = []

    listUrl.append("https://en.wikipedia.org/wiki/Rubber_duck")
    listUrl.append("https://en.wikipedia.org/wiki/London")
    listUrl.append("https://en.wikipedia.org/wiki/New_York_City")
    listUrl.append("https://en.wikipedia.org/wiki/Berlin")
    listUrl.append("https://en.wikipedia.org/wiki/Paris")
    listUrl.append("https://en.wikipedia.org/wiki/Mumbai")
    listUrl.append("https://en.wikipedia.org/wiki/Tokyo")
    listUrl.append("https://en.wikipedia.org/wiki/Shenzhen")
    listUrl.append("https://en.wikipedia.org/wiki/San_Francisco")

    output = operations(listUrl)

