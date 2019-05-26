class Solution:
    email_graph = {}
    def union(self, email1, email2):
        root1 = self.getroot(email1)
        root2 = self.getroot(email2)
        if root1 == root2:
            return True
        else:
            self.graph_dict[root2] = root1
            return False

    def getroot(self, val):
        if val not in self.graph_dict:
            self.graph_dict[val] = val
            return val
        root = val
        while(root != self.graph_dict[root]):
            root = self.graph_dict[root]
        return root
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_user = {}
        self.graph_dict = {}
        for account in accounts:
            user_name = account[0]
            main_email = account[1]
            for email in account[1:]:
                email_user[email] = user_name
                self.union(main_email, email)
        mains = {}
        for email in email_user:
            main_email = self.getroot(email)
            if main_email not in mains:
                mains[main_email] = [email]
            else:
                mains[main_email].append(email)
        return [[email_user[key]] + sorted(val) for key, val in mains.items()]
