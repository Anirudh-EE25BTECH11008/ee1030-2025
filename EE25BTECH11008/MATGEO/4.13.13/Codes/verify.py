import ctypes

# Load the shared object
lib = ctypes.CDLL('./verify.so')

# Define argument and return types
lib.verify_m.argtypes = [ctypes.c_double, ctypes.c_int]
lib.verify_m.restype = ctypes.c_double

def verify_value(m, sign):
    result = lib.verify_m(m, sign)
    print(f"m = {m}, v = [1, {sign}],  v^T A v = {result:.6f}")
    if abs(result) < 1e-9:
        print("The condition v^T A v = 0 is satisfied.\n")
    else:
        print("The condition v^T A v = 0 is NOT satisfied.\n")

# Test for m = 1 and m = -1
verify_value(1, 1)
verify_value(1, -1)
verify_value(-1, 1)
verify_value(-1, -1)
