class Solution:
    def subdomainVisits(self, cpdomains):
        
        # Create Hash
        # loop through domains
        # split domain into all domains
        # count domain occurences
        
        allVisits = {}
        for domain in cpdomains:
            domain = domain.split(" ")
            visits = int(domain[0])
            domain = domain[1]
            subdomains = []
            subdomains.append(domain)
            while('.' in domain):
                domain = domain.split(".", 1)[1]
                subdomains.append(domain)

            for domain in subdomains:                
                if(domain in allVisits):
                    allVisits[domain] += visits
                else:
                    allVisits[domain] = visits

        
        output = []
        for key in allVisits:
            output.append(f"{allVisits[key]} {key}")
            
        return output

cpdomains = ["9001 discuss.leetcode.com"]
S = Solution().subdomainVisits(cpdomains)
print(S)