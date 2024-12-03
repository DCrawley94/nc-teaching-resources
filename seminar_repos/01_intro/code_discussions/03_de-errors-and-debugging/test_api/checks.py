import functools

# ANSI colour codes
BOLD_RED = "\033[1;31m"
NORMAL_RED = "\033[0;31m"
BOLD_GREEN = "\033[1;32m"
NORMAL_GREEN = "\033[0;32m"
BOLD_YELLOW = "\033[1;33m"
NORMAL_YELLOW = "\033[0;33m"
DEFAULT = "\033[0;37m"


def run_test(testing_func):
    @functools.wraps(testing_func)
    def wrapper():
        try:
            testing_func()
            feedback_msg = (f"{BOLD_GREEN}{testing_func.__name__}()"
                            f"{NORMAL_GREEN}: Test passed ✅{DEFAULT}")
            print(feedback_msg)
        except Exception:
            feedback_msg = (f"{BOLD_RED}{testing_func.__name__}(){NORMAL_RED}:"
                            " Test failed ❌, see error message below:"
                            f"{DEFAULT}\n")
            print(feedback_msg)
            raise
    return wrapper


def skip_test(testing_func):
    @functools.wraps(testing_func)
    def wrapper():
        feedback_msg = (f"{BOLD_YELLOW}{testing_func.__name__}()"
                        f"{NORMAL_YELLOW}: Test skipped 🔇{DEFAULT}")
        print(feedback_msg)
    return wrapper


def format_err_msg(expected, received):
    err_msg = (f"{NORMAL_RED}expected {expected}, instead received "
               f"{received}{DEFAULT}")
    return err_msg
