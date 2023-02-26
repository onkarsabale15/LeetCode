class Solution:
    def generatetreeHelper(self,left,right):
        if left > right: return [None]
        ans = []
        for x in range(left,right+1):
            leftsubtree = self.generatetreeHelper(left,x-1)
            rightsubtree = self.generatetreeHelper(x+1,right)
            for node1 in leftsubtree:
                for node2 in rightsubtree:
                    root = TreeNode(x)
                    root.left = node1
                    root.right = node2
                    ans.append(root)
        return ans        
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generatetreeHelper(1,n)

