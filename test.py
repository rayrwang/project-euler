
import os
import subprocess
import sys
import time
import re

if __name__ == "__main__":
    if len(sys.argv) > 1:
        problems = [f"p{n.rjust(4, "0")}.py" for n in sys.argv[1:]]
    else:
        problems = sorted(os.listdir())

    correct = 0
    incorrect = 0
    unverified = 0
    solutions = 0
    timed_out = 0
    timeout_s = 120
    t_start_all = time.perf_counter()
    for name in problems:
        if name.startswith("p"):
            solutions += 1
            print(f"\nProblem {int(name[1:5])}:")
            t_start_solution = time.perf_counter()
            try:
                proc = subprocess.run([sys.executable or "python", name],
                                    capture_output=True,
                                    timeout=timeout_s)
            except subprocess.TimeoutExpired:
                timed_out += 1
                print(f"Timeout after {timeout_s}s.")
                continue
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
                    correct += 1
                    print(f"{answer} ✔️")
                else:
                    incorrect += 1
                    print(f"{answer} ❌ (solution: {solution})")
            else:
                unverified += 1
                print(f"{answer} ? (no solution found)")

            print(f"(in {time.perf_counter()-t_start_solution:.1f}s)")
            
    print(f"Ran {solutions} solutions in {time.perf_counter()-t_start_all:.1f}s.")
    print(f"({correct} correct, {incorrect} incorrect, {unverified} unverified, {timed_out} timed out)")
    assert correct == solutions, "Not all solutions have been verified as correct."
