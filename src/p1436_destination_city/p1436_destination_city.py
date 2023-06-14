from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city_set = set()

        for path in paths:
            city_set.add(path[0])

        for path in paths:
            if path[1] not in city_set:
                return path[1]

        return ""


