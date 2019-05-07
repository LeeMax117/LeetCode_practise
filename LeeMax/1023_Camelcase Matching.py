class Solution:
    def compare(self,pattern,query):
        position = 0
            
        for index,i in enumerate(query):
            if i.isupper() and i != pattern[position]:
                break
            else:
                if i == pattern[position]:
                    position += 1
                if position == len(pattern):
                    if index == len(query)-1 or query[index+1:].islower():
                        return True
                    else:
                        return False
        return False
    
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        output = []
        for query in queries:
            output.append(self.compare(pattern,query))
        return output
