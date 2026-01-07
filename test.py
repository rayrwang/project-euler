
import os
import subprocess
import sys
import time

if __name__ == "__main__":
    for name in sorted(os.listdir()):
        if name.startswith("p"):
            print(f"\nProblem {int(name[1:5])}:")
            start = time.perf_counter()
            subprocess.run([sys.executable or "python", name])
            print(f"(in {time.perf_counter()-start:.1f}s)")

