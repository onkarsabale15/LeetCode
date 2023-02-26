class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort()
        lower = []
        for x, y in trees:
            if len(lower) < 2:
                lower.append((x, y))
                continue

            while len(lower) >= 2:
                ax, ay = lower [-2]
                bx, by = lower[-1]
                cx, cy = x, y
                area = ax * by + bx * cy + cx * ay - bx * ay - cx * by - ax * cy
                if area < 0:
                    lower.pop()
                else:
                    break
            lower.append((cx, cy))
        upper = []
        for x, y in trees:
            if len(upper) < 2:
                upper.append((x, y))
                continue
            while len(upper) >= 2:
                ax, ay = upper[-2]
                bx, by = upper[-1]
                cx, cy = x,y
                area = ax * by + bx * cy + cx * ay - bx * ay - cx * by - ax * cy
                if area > 0:
                    upper.pop()
                else:
                    break
            upper.append((cx, cy))
        return set(lower) | set(upper)