def announce(f):
    def wrapper():
        print("About to start")
        f()
        print("Done with the announcement")
    return wrapper


@announce
def Hello():
    print("Hello!")


Hello()
