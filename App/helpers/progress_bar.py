import sys


class ProgressBar:

    @staticmethod
    def print(progress, total, length=50, last:bool=False):
        bar = "█" * int(length * progress / total) + "-" * (length - int(length * progress / total))
        sys.stdout.write(f"\r|{bar}| {progress}/{total}")
        if progress==total:
            sys.stdout.write("\n")
        sys.stdout.flush()
