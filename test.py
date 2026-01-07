
import os
import subprocess
import sys
import time

if __name__ == "__main__":
    solutions = 0
    t_start_all = time.perf_counter()
    for name in sorted(os.listdir()):
        if name.startswith("p"):
            solutions += 1
            print(f"\nProblem {int(name[1:5])}:")
            t_start_solution = time.perf_counter()
            subprocess.run([sys.executable or "python", name])
            print(f"(in {time.perf_counter()-t_start_solution:.1f}s)")
    print(f"Ran {solutions} solutions in {time.perf_counter()-t_start_all:.1f}s.")
