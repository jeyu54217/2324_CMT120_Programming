##############################
# BACK END
##############################

import sys
from pathlib import Path
import importlib
import os

from multiprocessing import Process, Manager
import time

'''
    An automated testing script for CMT120
     2022/23 using multiprocessing and not SIGALRM,
      ....so, this should work on Windows machines....
'''


class TimeoutException(Exception):
    pass


def a_test(running_complete_dict, out, fun, *param):
    '''
        Function to be used in mutliprocessing Process.
        This updates the dictionary values if
        The test completes within the Process time limit
    '''
    out = fun(*param)
    running_complete_dict["running_complete"] = True
    running_complete_dict["response"] = out
    return out  # dont really need this


def main():
    # Importing functions
    def importModule(module_name):
        # get a handle on the module
        mdl = importlib.import_module(module_name)

        # is there an __all__?  if so respect it
        if "__all__" in mdl.__dict__:
            names = mdl.__dict__["__all__"]
        else:
            # otherwise we import all names that don't begin with _
            names = [x for x in mdl.__dict__ if not x.startswith("_")]

        # now drag them in
        globals().update({k: getattr(mdl, k) for k in names})

    try:
        mod = sys.argv[1].split('.')[0]
        importModule(mod)
    except IndexError as ie:
        sys.exit('Please, provide the name of the file to test.')


    # Testing function
    def runTest(call, output ,isSoft = False):
        if type(call) != type(output):
            return False

        if isinstance(call,list):
            if len(call) != len(output):
                return False
            for ind in range(len(call)):
                if isSoft:
                    res = call[ind] in output
                else:
                    res = runTest(call[ind],output[ind])
                if not res:
                    return False
        elif call != output:
            return False

        return True

    ##############################
    # TESTCASES
    ##############################

    # Lists of tests for each function
    # Each element of the list is a (input,solution) tuple
    # - 'input' is a tuple containing the input parameters.
    # - 'solution' must be provided in format expected.
    exercise1_list = [((12, 15), (4, 5)),
					  ((3, 7), (3, 7))]

    exercise2_list = [((6, 10, 1960), True),
					  ((7, 1, 2021), False)]

    exercise3_list = [((["a", 2, (0, "zero")],),[
						[],
						["a"],
						[2],
						[(0, "zero")],
						["a", 2],
						[2, (0, "zero")],
						["a", 2, (0, "zero")]
						]),
					  ((["a", 1],),[[], ["a"], [1], ["a", 1]])]

    exercise4_list = [(("computer",),"omputercay"),
					  (("think",),"inkthay")]

    exercise5_list = [(("Hello, World!",),".... . .-.. .-.. --- .-- --- .-. .-.. -.."),
    				  (("Testing, 1, 2, 3, Testing!",),"- . ... - .. -. --. .---- ..--- ...-- - . ... - .. -. --.")]

    exercise6_list = [((21,),"twenty-one"),
    				  ((191,),"a hundred and ninety-one")]
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file1 = Path(script_dir, "test_data", "code1.py")
    input_file2 = Path(script_dir, "test_data", "code2.py")
    exercise7_list = [((input_file1,),["__init__", "overdrawn"]),
    				  ((input_file2,),[])]
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    text_file = Path(script_dir, "test_data", "text1.txt")
    text_50 = [
        "Alice was beginning to get very tired of sitting",
        "by her sister on the bank, and of having nothing",
        "to do: once or twice she had peeped into the book",
        "her sister was reading, but it had no pictures or",
        'conversations in it,"and what is the use of a',
        'book," thought Alice, "without pictures or',
        'conversations?"',
    ]
    text_20 = [
        "Alice was beginning",
        "to get very tired of",
        "sitting by her",
        "sister on the bank,",
        "and of having",
        "nothing to do: once",
        "or twice she had",
        "peeped into the book",
        "her sister was",
        "reading, but it had",
        "no pictures or",
        "conversations in",
        'it,"and what is the',
        'use of a book,"',
        "thought Alice,",
        '"without pictures or',
        'conversations?"',
    ]

    exercise8_list = [((text_file, 50),text_50),
                      ((text_file, 20),text_20)]

    exercise9_list = [(("a1", "c5", 2),True),
                      (("c6", "h1", 1),False)]

    exercise10_list = [((["XX......", "XX....O.", ".....OOO"],), [
                            "XXX.....",
                            "XXX..OOO",
                            "XX....O."]),
    				  ((["XX....", "XX....", "OOOOOO"],),[
                            "XXX...",
                            "XXOOOO",
                            "......"])]

    ##############################
    # FRONT END
    ##############################

    # Dictionary of functions to test
    test_dict = {exercise1: exercise1_list,
    			 exercise2: exercise2_list,
    			 exercise3: exercise3_list,
    			 exercise4: exercise4_list,
    			 exercise5: exercise5_list,
    			 exercise6: exercise6_list,
    			 exercise7: exercise7_list,
    			 exercise8: exercise8_list,
    			 exercise9: exercise9_list,
    			 exercise10: exercise10_list
                }
    
    soft_equal = (exercise3,) # Used for checking if two lists have the same elements instead of being fully identical

    res_list = []
    # Loop on every function to test
    manager = Manager()

    for fun,test_list in test_dict.items():
        # show the name of the exercise to be tested
        sys.stdout.write(f'\n#### FUNCTION {fun.__name__}:\n\n')
        res = 0
        # Loop on every test to run
        for index, t in enumerate(test_list, start=1):
            test_time_limit = 3 # per test time limit (seconds)
            param = t[0]
            sol = t[1]
            out = None

            try:
                # establish a dict to be passed to multiprocess Process.
                running_complete_dict = manager.dict()
                running_complete_dict["running_complete"] = False
                running_complete_dict["response"] = None
                new_test_process = Process(target=a_test, args=(running_complete_dict, out, fun ,*param,))
                # show test underway....else the 2-second pause can be frustrating
                sys.stdout.write(f'Test: {index}\n')
                sys.stdout.flush()

                new_test_process.start()
                # Process starts and we wait for the length of time indicated
                # 2-seconds per test is more generous than in the first testing
                #  framework.
                time.sleep(test_time_limit)
                new_test_process.terminate()

                out = running_complete_dict["response"]

                if not running_complete_dict["running_complete"] == False:
                    # the test has completed within the timelimit set,
                    #  test for correctness
                    isSoft = fun in soft_equal
                    if not runTest(out,sol,isSoft):
                        # the submission, does not return the correct value
                        err_str = f'ERROR IN {fun.__name__}{param}: *** EXPECTED: {sol} *** OBTAINED: {out}\n\n'
                        sys.stdout.write(err_str)
                        sys.stdout.flush()
                    else:
                        # the submission returns the correct value
                        res += 1
                        sys.stdout.write(f'{fun.__name__}{param}: PASSED\n\n')
                        sys.stdout.flush()
                else:
                    # the test did not complete within the time limit set...
                    raise TimeoutException
            except Exception as e:
                if type(e) == TimeoutException:
                    e = f"TimeoutException > {test_time_limit} seconds"
                err_str = f'ERROR IN {fun.__name__}{param}: {str(e)} \n\n'
                sys.stdout.write(err_str)
                sys.stdout.flush()
            # END for t in test_list:

        res_list.append(res)
        err_str = f'#### FUNCTION {fun.__name__} SCORE: {res} / {len(test_list)}\n\n'
        sys.stdout.write(err_str)
        sys.stdout.flush()
        # END for fun_name,test_list in test_dict.items():

    # print res_list as a CSV
    out_str = f'{sys.argv[1]}, {", ".join(str(x) for x in res_list)}\n'

    sys.stderr.write(out_str)
    sys.stderr.flush()


if __name__ == '__main__':
    main()
