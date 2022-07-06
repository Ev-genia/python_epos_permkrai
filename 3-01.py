from Levenshtein import distance

if __name__ == '__main__':
    pairs = [
        ('home', 'work'),
        ('home', 'house'),
        ('computer', 'computers'),
        ('house', 'townhouse'),
    ]
    for sourse, dest in pairs:
        dist = distance(sourse, dest)
        print('sourse:', sourse, ', dest:', dest, '; distance =', dist)