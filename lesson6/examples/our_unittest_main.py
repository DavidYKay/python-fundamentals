from test_caesar import TestCaesar

def find_all_test_cases():
    return [TestCaesar]

def our_unittest_main():
    successes = 0
    failures = 0
    for test_class in find_all_test_cases():
        instance_of_test = test_class()
        for method in instance_of_test.methods():
            if method.name.contains("test"):
                try:
                    method()
                    successes = successes + 1
                except:
                    print("Oh snap, we got a failure!")
                    failures = failures + 1
    print("We had %d successes and %d failures." % (successes, failures))

