class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hash_set = set()
        for i, email in enumerate(emails):
            # find local and domain name
            local_name, domain_name = email.split('@')

            # clean the local_name
            # ignore everything after '+'
            local_name = local_name.split('+')[0]
            # replace "." with ""
            local_name = local_name.replace(".", "")

            hash_set.add((local_name, domain_name))
        
        return len(hash_set)


            

             
