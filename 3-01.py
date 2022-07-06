from Levenshtein import distance

pairs = [
    ('home', 'work'),
    ('home', 'house'),
    ('computer', 'computers'),
    ('house', 'townhouse'),
]

if __name__ == '__main__':
    for sourse, dest in pairs:
        dist = distance(sourse, dest)
        print('sourse:', sourse, ', dest:', dest, '; distance =', dist)