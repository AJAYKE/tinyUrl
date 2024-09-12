basechars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def url_shortener(longurl):
    id = 12309846113
    shortUrl = generate_base62(id)
    return shortUrl

def generate_base62(id):
    base = ""
    global basechars
    while id > 62:
        rem = id % 62
        id = id // 62
        base = base+basechars[rem]
    base = base + basechars[id]
    return base[::-1]

if __name__ == '__main__':
    print(url_shortener("asdff"))
