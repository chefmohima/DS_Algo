# Word Ladder Problem
# You are given 2 words A and B, both of the same length. Your task is to transform one word to another changing only one letter each time. Each intermediate word should be a valid word in the dictionary. Print out the length of the path. (Alternate version: print out the intermediate words)
# A = CAB, B = DOG 
# Result: 4 (CAB -> COB -> COG -> DOG)


# Queue structure 
class Queue:
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return len(self.elements) == 0
        
    def enqueue(self,element):
        self.elements.append(element)
        
    def dequeue(self):
        if self.is_empty() == False:
            element = self.elements.pop(0)
            return element
        
# helper function
# return True if worda and wordb differ by just 1 character
def diff_by_one(worda,wordb):
    diff = 0
    for i in range(len(worda)):
        if worda[i] != wordb[i]:
            diff += 1
            if diff > 1:
                return False
    return True
        
    

# word ladder function        
def word_ladder(start,tgt,dict):
    q = Queue()
    l = 0
    q.enqueue(start)
    
    while q.is_empty() == False:
        w = q.dequeue()
        print(w)
        l += 1
        if w  == tgt:
            return l
        
        for word in dict:
            if diff_by_one(word,w) == True:
                q.enqueue(word)
                dict.remove(word)
                break

        
# Test code
d = ['POON', 'PLEE', 'SAME', 'POIE', 'PLEA', 'PLIE', 'POIN']
print(word_ladder('TOON','POIN',d))



        
        
        
        
            


        
        