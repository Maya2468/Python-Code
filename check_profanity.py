def read_text():
    quotes = open("/Users/ma/Documents/Maya_Python/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close

read_text()
