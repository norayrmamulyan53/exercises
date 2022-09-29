from packages.exception_handling import NotFoundError


def check():
    raise NotFoundError
    return 0


check()
