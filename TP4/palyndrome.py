def palyndrome(chain):
    reverse = chain[::-1]
    if chain == reverse:
        return True
    else:
        return False

print(palyndrome("aya"))
print(palyndrome("Boussoufi"))