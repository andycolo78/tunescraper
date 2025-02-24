import sys

class ProgressBar:

    @staticmethod
    def print(progress, total, length=50):
        bar = "█" * int(length * progress / total) + "-" * (length - int(length * progress / total))
        sys.stdout.write(f"\r|{bar}| {progress}/{total}")
        sys.stdout.flush()