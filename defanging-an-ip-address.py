#Given a valid (IPv4) IP address, 
# return a defanged version of that IP address.
# LEETCODE EASY QUESTION
def defangIPaddr(self, address: str) -> str:
    ans = ''
    for char in address:
        if char == '.':
            ans += '[.]'
        else:
            ans += char
    return ans