class Solution:
    def accountsMerge(self, accounts):
        def mergeAccounts(accounts):
            parent = {}
            for email in accounts[0]:
                parent[email] = accounts[0][0]

            for account in accounts[1:]:
                for email in account:
                    tmp = email
                    if tmp in parent:
                        while parent[tmp] != tmp:
                            tmp = parent[tmp]

                        for i in account:
                            if i in parent:
                                while parent[i] != i:
                                    i = parent[i]
                            parent[i] = tmp
                        break
                    else:
                        parent[tmp] = account[0]

            root_dict = {}
            for email in parent:
                root = email
                while parent[root] != root:
                    root = parent[root]

                if root in root_dict:
                    root_dict[root].append(email)
                else:
                    root_dict[root] = [email]

            merged_emails = []
            for i in root_dict:
                merged_emails.append(root_dict[i])

            return merged_emails


        accout_list = {}
        for accout in accounts:
            user_name = accout[0]
            try:
                accout_list[user_name].append(accout[1:])
            except KeyError:
                accout_list[user_name] = [accout[1:]]

        merged_accouts = []
        for user in accout_list:
            emails = accout_list[user]
            if len(emails) > 1:
                merged_emails = mergeAccounts(emails)
            else:
                merged_emails = emails

            for i in merged_emails:
                x = list(set(i))
                x.sort()
                x.insert(0, user)
                merged_accouts.append(x)

        return merged_accouts


if __name__ == '__main__':
    a = Solution()
    print(a.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))