#!/usr/bin/env python3

# One string is an anagram of another if the second is simply a rearrangement
# of the first. For example, 'heart' and 'earth' are anagrams. The strings
# 'python' and 'typhon' are anagrams as well. For the sake of simplicity, we
# will assume that the two strings in question are of equal length and that
# they are made up of symbols from the set of 26 lowercase alphabetic
# characters. Our goal is to write a boolean function that will take two
# strings and return whether they are anagrams.

def anagramSolution1(s1, s2):
    """
    Solution 1: Checking Off

    Our first solution to the anagram problem will check the lengths of the
    strings and then to see that each character in the first string actually
    occurs in the second. If it is possible to “checkoff” each character, then
    the two strings must be anagrams. Checking off a character will be
    accomplished by replacing it with the special Python value None. However,
    since strings in Python are immutable, the first step in the process will
    be to convert the second string to a list. Each character from the first
    string can be checked against the characters in the list and if found,
    checked off by replacement.

    """

    stillOK = True
    if len(s1) != len(s2):
        stillOK = False

    alist = list(s2)
    pos1 = 0

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 += 1

    return stillOK

def anagramSolution2(s1, s2):
    """
    Solution 2: Sort and Compare

    Another solution to the anagram problem will make use of the fact that
    even though s1 and s2 are different, they are anagrams only if they
    consist of exactly the same characters. So, if we begin by sorting each
    string alphabetically, from a to z, we will end up with the same string if
    the original two strings are anagrams.

    """

    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True
    if len(s1) != len(s2):
        matches = False

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False

    return matches

def anagramSolution3(s1, s2):
    """
    Solution 4: Count and Compare

    Our final solution to the anagram problem takes advantage of the fact that
    any two anagrams will have the same number of a’s, the same number of b’s,
    the same number of c’s, and so on. In order to decide whether two strings
    are anagrams, we will first count the number of times each character
    occurs. Since there are 26 possible characters, we can use a list of 26
    counters, one for each possible character. Each time we see a particular
    character, we will increment the counter at that position. In the end, if
    the two lists of counters are identical, the strings must be anagrams.

    """

    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    i = 0
    stillOK = True
    while i < 26 and stillOK:
        if c1[i] == c2[i]:
            i += 1
        else:
            stillOK = False

    return stillOK

def main():
    print(anagramSolution1('abcd', 'dcba'))
    print(anagramSolution2('abcde', 'edcba'))
    print(anagramSolution3('apple', 'pleap'))

main()
