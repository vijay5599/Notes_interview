# ─── How a Decorator Works ─────────────────────────────────────────────────────
#
#  @deco_func          is just syntactic sugar for:
#  def main_func(): …      →    main_func = deco_func(main_func)
#
#  So deco_func receives the FUNCTION OBJECT, not its arguments.
#  Arguments only exist when the returned wrapper is actually called.

def deco_func(func):                    # step 1 — receives the function
    def wrapper(*args, **kwargs):       # step 2 — captures call-time args
        print("before main func")
        result = func(*args, **kwargs)  # step 3 — calls the original function
        print("after main func")
        return result
    return wrapper                      # step 4 — returns the wrapper

@deco_func                  # ← equivalent to: main_func = deco_func(main_func)
def main_func(name):
    print("main func", name)


main_func("vijaya")
# Output:
#   before main func
#   main func vijaya
#   after main func

