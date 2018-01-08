from comparator import Comparator

def make_table(p):
    table = {'*': len(p)}
    i = 0
    for el in p:
        if i != len(p)-1:
            table[el] = len(p) - i - 1
        else:
            if el in table:
                pass
            else:
                table[el] = len(p)
        i+=1
    return table

def bmh_matcher(t,p):
    table = make_table(p)
    c = Comparator()
    results = []
    i = 0
    while i < len(t):
        try:
            first = t[i+len(p)]
        except IndexError:
            return results, c
        for j in range(len(p)-1,-1,-1):
            if not c.compare(p,j,t,i+j):
                i += table[first]
                break
            elif j == 0:
                results.append(i)
                i+=table[first]
    return results, c

if __name__ == '__main__':
    t = 'abbabbbabbababbabbabababbabababbabababbabababbbababababbabababababbbabababa'
    p = 'abbab'
    print(make_table(p))
    results, c = bmh_matcher(t,p)
    for result in results:
        print('Match found at shift ' + str(result))
        print(t)
        print(' ' * (result) + p)
        print()
    print('{} comparisons'.format(c.count))