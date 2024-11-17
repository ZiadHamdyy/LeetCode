class Solution:
    def defangIPaddr(self, address: str) -> str:
        arr = list(address)
        arr = ["[.]" if i == "." else i for i in arr]
        return "".join(arr)