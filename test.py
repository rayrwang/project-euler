import os
import subprocess
import sys
import time

if __name__ == "__main__":
    if len(sys.argv) > 1:
        problems = [f"p{n.rjust(4, "0")}.py" for n in sys.argv[1:]]
    else:
        problems = sorted(os.path.join(d, f) for d in ["0-99"] for f in os.listdir(d))

    correct = 0
    incorrect = 0
    unverified = 0
    solutions = 0
    timed_out = 0
    timeout_s = 600
    t_start_all = time.perf_counter()
    for name in problems:
        file_name = os.path.basename(name)
        if file_name.startswith("p") and file_name.endswith(".py"):
            solutions += 1
            print(f"Problem {int(file_name[1:5])}:", end=" ")
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
            error = proc.stderr.decode().strip()

            # Check answer:
            # The expected answer is written as a comment on the executable
            # print line, e.g.  print(s)  # 233168
            solution = None
            with open(name, "r") as f:
                for line in f:
                    if line.lstrip().startswith("#"):
                        continue  # skip commented-out code
                    if "print(" in line and "#" in line:
                        solution = line.split("#", 1)[1].strip()
                        break
            if solution:
                if answer == solution:
                    correct += 1
                    print(f"{answer} ✔️ ", end=" ")
                else:
                    incorrect += 1
                    print(f"{answer} ❌ (solution: {solution})", end=" ")
            else:
                unverified += 1
                print(f"{answer} ? (no solution found)", end=" ")

            # Surface crashes that would otherwise hide behind an empty answer.
            if proc.returncode != 0 and error:
                last = error.splitlines()[-1]
                print(f"[exit {proc.returncode}: {last}]", end=" ")

            print(f"(in {time.perf_counter()-t_start_solution:.1f}s)")
            
    print(f"\nRan {solutions} solutions in {time.perf_counter()-t_start_all:.1f}s.")
    print(f"({correct} correct, {incorrect} incorrect, {unverified} unverified, {timed_out} timed out)")
    assert correct == solutions, "Not all solutions have been verified as correct."
