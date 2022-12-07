def safe_squares_rooks(n, rooks):
    r = set()
    c = set()
    for i in range(len(rooks)):
        r.add(rooks[i][0])
        c.add(rooks[i][1])
    return (n - len(c)) * (n - len(r))