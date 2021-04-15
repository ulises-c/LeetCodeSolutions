# https://leetcode.com/problems/defanging-an-ip-address/


def defangIPaddr(address: str) -> str:
    address = address.replace(".", "[.]")
    return address

print(defangIPaddr("1.1.1.1"))