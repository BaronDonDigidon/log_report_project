from log_parser.reporter import sorted_average_stats

def test_sorted_average_stats():
    data = [["/a", 10, 0.5], ["/b", 20, 0.3]]
    sorted_data = sorted_average_stats(data)
    assert sorted_data[0][0] == "/b"