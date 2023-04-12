"""
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly 
one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, 
where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. 
A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.
"""
def longestStrChain(words):
    words_dict = {}
    final_chain = 1
    if len(words) == 1:
        return 1
    words.sort(key=len)
    for word in words:
        words_dict[word] = 1
        for i in range(len(word)):
            prev = word[:i] +word[i+1:]
            if prev in words_dict:
                words_dict[word] = max(words_dict[word], words_dict[prev] +1)
                final_chain = max(final_chain, words_dict[word])
    return final_chain

# words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# words2 = ["a","b","ba","bca","bda","bdca"]
# words3 = ["abcd","dbqca"]
words4 = ["c","cd","ab","bcd","abc","abcd","abcde"]
print(longestStrChain(words4))
                     