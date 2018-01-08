from comparator import Comparator

#Implementation of the Knuth-Morris-Pratt String Matching algorithm

def compute_prefix(p):
    '''
    Compute the prefix function for a given pattern.
    pi[i] is the length of the longest prefix of p[:i] that's also a suffix of p[:i]
    '''
    pi = [0]
    k = 0
    for i in range(1,len(p)):
        #The last iteration was a success, so keep looking through the pattern for a prefix = suffix
        while k > 0 and p[k] != p[i]:
            k = pi[k-1]
        # We found a pre/suf, so increment k (the length of the longest so far found pre/suf)
        if p[k] == p[i] or k > 0:
            k = k + 1
        pi.append(k)
    return pi

def kmp_match(t,p):
    '''
    Find all instances of p in t, runs a comparator class that keeps track of the number of comparisons made
    '''
    pi = compute_prefix(p)
    q = 0 #number of thus far matched characters in the pattern
    c = Comparator()
    results=[]
    for i in range(0, len(t)):
        # we've matched some characters, but not enough, so we shift forward by the prefix amount
        while q > 0 and not c.compare(p,q,t,i):
            q = pi[q]
        # we've matched another character 
        if c.compare(p,q,t,i):
            q += 1
        # we've matched as many chars are there in the pattern, we've found a match
        if q == len(p):
            results.append(i-len(p)+1)
            q = pi[q-1]
    return results, c

if __name__ == '__main__':
    t = 'abbabbbabbababbabbabababbabababbabababbabababbbababababbabababababbbabababa'
    p = 'abbab'
    print(compute_prefix(p))
    results, c = kmp_match(t,p)
    for result in results:
        print('Match found at shift ' + str(result))
        print(t)
        print(' ' * (result) + p)
        print()
    print('{} comparisons'.format(c.count))