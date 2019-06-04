def pytest_configure(config):
    config.addinivalue_line("markers", "points(arg): used to assign points to test cases for grading.")
    config.addinivalue_line("markers", "mandatory: used to declare a test case as mandatory for the assignment.")
