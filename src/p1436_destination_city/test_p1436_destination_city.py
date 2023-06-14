from p1436_destination_city import Solution

def test_01():
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    result = Solution().destCity(paths)
    assert result == "Sao Paulo"

def test_02():
    paths = [["B","C"],["D","B"],["C","A"]]
    result = Solution().destCity(paths)
    assert result == "A"    
