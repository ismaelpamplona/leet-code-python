from p739_daily_temperatures import Solution

def test_case_01():
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    output = [1, 1, 4, 2, 1, 1, 0, 0]
    result1 = Solution().daily_temperatures(temperatures)
    assert result1 == output

def test_case_02():
    temperatures = [30, 40, 50, 60]
    output = [1, 1, 1, 0]
    result1 = Solution().daily_temperatures(temperatures)
    assert result1 == output

def test_case_03():
    temperatures = [30, 60, 90]
    output = [1, 1, 0]
    result1 = Solution().daily_temperatures(temperatures)
    assert result1 == output

def test_case_04():
    temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    output = [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]
    result1 = Solution().daily_temperatures(temperatures)
    assert result1 == output

def test_case_05():
    temperatures = [34, 33, 32, 31, 30, 50]
    output = [5, 4, 3, 2, 1, 0]
    result1 = Solution().daily_temperatures(temperatures)
    assert result1 == output

def test_case_06():
    temperatures = [40, 35, 32, 37, 50]
    output = [4, 2, 1, 1, 0]
    result1 = Solution().daily_temperatures(temperatures)
    assert result1 == output