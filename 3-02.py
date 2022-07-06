import difflib

str = """Жэка
Женя
Женечка
Евгения
Евгеха
""".split('\n')
dest = 'Евгений'

def similarity(s1, s2):
  normalized1 = s1.lower()
  normalized2 = s2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()

if __name__ == '__main__':
    for i in str:
        print(i, dest, similarity(i, dest))
