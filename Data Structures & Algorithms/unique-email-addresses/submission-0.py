class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hash_set = set()
        for i, email in enumerate(emails):
            # find local and domain name
            local_and_domain = email.split('@')
            local_name = local_and_domain[0]
            domain_name = local_and_domain[1]

            # clean the local_name
            clean_local_name = ""
            for char in local_name:
                if char == ".":
                    continue
                elif char == "+":
                    break
                
                else:
                    clean_local_name += char
            
            unique_email = clean_local_name + domain_name
            hash_set.add(unique_email)
        
        return len(hash_set)


            

             
