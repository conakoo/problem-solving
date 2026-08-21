"""Split & Replace
Level: Easy

Let N be the number of the emails and M be the average length of an email.
Time Complexity: O(N⋅M)
Space Complexity: O(N)
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        n = len(emails)
        for i in range(n):
            local, domain = emails[i].split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            emails[i] = local+"@"+domain
        return len(set(emails))
