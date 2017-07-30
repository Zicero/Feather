load_test(TestCase1(test_params1))
load_test(TestCase2(test_params2))
...
load_test(TestCaseN(test_params3))

...

for test in loaded_tests:
    test.run()

        