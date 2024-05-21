# Press the green button in the gutter to run the script.
import test_login_correct_creds
import test_login_wrong_creds
import test_register_email_only
import test_register_new

if __name__ == '__main__':
    try:
        test_register_email_only.run_test()
        print("Test test_register_email_only passed")
    except AssertionError as e:
        print(f"Assertion Error in test_register_email_only: {e}")

    try:
        test_register_new.run_test()
        print("Test test_register_new passed")
    except AssertionError as e:
        print(f"Assertion Error in test_register_new: {e}")

    try:
        test_login_wrong_creds.run_test()
        print("Test test_login_wrong_creds passed")
    except AssertionError as e:
        print(f"Assertion Error in test_login_wrong_creds: {e}")

    try:
        test_login_correct_creds.run_test()
        print("Test test_login_correct_creds passed")
    except AssertionError as e:
        print(f"Assertion Error in test_login_correct_creds: {e}")

