from p933_number_of_recent_calls import RecentCounter

def test_case_01():
    rc = RecentCounter()
    pings = [1, 100, 3001, 3002]
    result = []
    for p in pings:
        result.append(rc.ping(p))
    output = [1, 2, 3, 3]
    assert output == result

def test_case_02():
    rc = RecentCounter()
    pings = [1, 100, 3001, 4000]
    result = []
    for p in pings:
        result.append(rc.ping(p))
    output = [1, 2, 3, 2]
    assert output == result