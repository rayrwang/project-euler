
import os
import subprocess
import sys
import time
import re

if __name__ == "__main__":
    solutions = 0
    t_start_all = time.perf_counter()
    for name in sorted(os.listdir()):
        if name.startswith("p"):
            solutions += 1
            print(f"\nProblem {int(name[1:5])}:")
            t_start_solution = time.perf_counter()
            proc = subprocess.run([sys.executable or "python", name], capture_output=True)
            answer = proc.stdout.decode().strip()

            # Check answer:
            # The solution is written as a comment on the line with a print statement
            solution = None
            solution_pattern = r"print\(.+#"
            with open(name, "r") as f:
                for line in f:
                    if re.search(solution_pattern, line):
                        split = re.split(solution_pattern, line)
                        if split:
                            solution = split[-1].strip()
                            break
            if solution:
                if answer == solution:
                    print(f"{answer} ✔️")
                else:
                    print(f"{answer} ❌ (solution: {solution})")
            else:
                print(f"{answer} ? (no solution found)")

            print(f"(in {time.perf_counter()-t_start_solution:.1f}s)")
            
    print(f"Ran {solutions} solutions in {time.perf_counter()-t_start_all:.1f}s.")
