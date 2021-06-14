def do_stuff(t: str) -> int:
    t = " ".join(t.split())
    return len(set(t.split(" ")))



