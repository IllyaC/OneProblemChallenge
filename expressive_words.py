def expressiveWords(s, words):
    
    def get_groups(string):
        groups = [[string[0], 1]]
        for character in string[1:]:
            if character == groups[-1][0]:
                groups[-1][1] += 1
            else:
                groups.append([character, 1])
        return groups
    
    s_groups = get_groups(s)
    stretchy_words = 0
    print(s_groups)
    
    for word in words:
        word_groups = get_groups(word)
        
        if(len(s_groups) != len(word_groups)):
            continue
        
        isStretchy = True
        for i in range(len(word_groups)):
            if(word_groups[i][0] !=s_groups[i][0]):
                isStretchy = False
                break
            if(word_groups[i][1] > s_groups[i][1]):
                isStretchy = False
                break
            if(s_groups[i][1] != word_groups[i][1] and s_groups[i][1] <3):
                isStretchy = False
                break
        if isStretchy:
            stretchy_words+=1
    
    return stretchy_words
            
                
            
    
    

s = "heeellooo"
words = ["hello", "hi", "helo"]
print(expressiveWords(s, words))