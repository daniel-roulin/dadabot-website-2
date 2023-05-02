import sys


def progress(done, todo):
    completion = done/todo
    sys.stdout.write(f"\r[{round(50*completion) * '='}>{round(50*(1-completion)) * '.'}] {round(completion * 100)}% ({done}/{todo})")
    sys.stdout.flush()