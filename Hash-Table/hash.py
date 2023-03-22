def my_hash_store(s, v=None):
    sb = s.encode()
    total = 0
    for b in sb:
        total += b
        total &= 0xffffffff
    my_array[total % len(my_array)] = v
    print(f"Index={total % len(my_array)}, Value={v}")


def my_hash_pwcheck(s):
    pw = s.encode()
    total = 0
    for char in pw:
        total += char
        total &= 0xffffffff
    return my_array[total % len(my_array)]


def my_hash_checker():
    global fail_counter, password_check
    pw_attempt = input("Password: ")
    pw_result = my_hash_pwcheck(pw_attempt)
    if pw_result is None and fail_counter < max_counter:
        fail_counter += 1
        print("Incorrect password, try again. You have {0} tr{1} remaining.".format(
            (max_counter-fail_counter), ("y" if (max_counter-fail_counter) == 1 else "ies")))
        my_hash_checker()
    elif pw_result is None and fail_counter == max_counter:
        print("Too Many Attempts! Try again later. Good-bye.")
    else:
        password_check = True
        print(f"Access granted! Your stored value is {pw_result}")


if __name__ == "__main__":
    my_array = [None] * (2**7)
    seed_pw = ["hello world", "test_password",
              "sample_text", "ab", "ac", "ad", "af", "ag", "az", "abc", "cba"]
    seed_vals = ["I am sentient, please help me leave", "gorilla warfare",
                "example_value", "gab", "gac", "gad", "gaf", "gag", "zag", "abc", "cba"]

    for index, password in enumerate(seed_pw):
        my_hash_store(password, seed_vals[index])
    print(my_array)
    password_check = False
    fail_counter = 0
    max_counter = 3
    my_hash_checker()
