from subprocess import check_output

def get_my_ip():
    output = check_output(['ip -6 addr'], shell=True).decode().split("\n")
    count = 0

    for str in output:
        count += 1
        if "teredo" in str:
            break

    address = output[count]
    unw_words = [" ", "inet6", "scope", "global"]

    for word in range(len(unw_words)):
        address = address.replace(unw_words[word], "")

    return address[:-3]
