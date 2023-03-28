"""_summary_
    Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].
"""

def spell_checker(wordlist, queries):
    vowels = 'aeiou'
    
    passing_queries = []
    
    def match_consonants(query, word):
        query_consonants = ''
        word_consonants = ''
        for char in query:
            if char.lower() not in vowels:
                query_consonants += char
            else:
                query_consonants += '1'
        for char in word:
            if char.lower() not in vowels:
                word_consonants += char
            else:
                word_consonants += '1'
        return query_consonants.lower() == word_consonants.lower()
    
    for query in queries:
        "Simplest case if the query matches something exactly"
        
        print(query)
        if(query in wordlist):
            passing_queries.append(query)
            continue
            
        "Next we need to correct vowels"
        match_found = False
        for word in wordlist:
            if(len(word) == len(query) and match_consonants(word, query)):
                passing_queries.append(word)
                match_found = True
                break    
        if (match_found == True):
            continue
        
        "Next we need to correct capitalization"
        
        if query.lower() in wordlist:
            passing_queries.append(query)
            continue

        passing_queries.append("")
        
    return passing_queries
    
wordlist = [["zeo","Zuo"]]
queries = ["zeo"]
print(spell_checker(wordlist, queries))

