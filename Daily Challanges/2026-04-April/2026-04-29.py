def parse_url_query(url):
    query_string = url.split("?")[1]
    pairs = query_string.split("&")
    dictionary = {}
    for pair in pairs:
        key, value = pair.split("=")
        dictionary[key] = value
    return dictionary


print(parse_url_query("https://example.com/search?name=Alice&age=30"))
print(
    parse_url_query("https://freecodecamp.org/learn?skill=programming&language=python")
)
print(parse_url_query("https://freecodecamp.org/items?category=books&sort=asc&page=2"))
