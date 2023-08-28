import os
import subprocess
from time import sleep

class AssignmentMarker:
    def __init__(self, assignment_path, rubric) -> None:
        self.assignment_path = assignment_path
        self.assignment_exe_path =  "built_assignment_to_mark.exe"
        self.rubric = rubric

    def process(self):
        if self.build():
            self.mark()

        os.remove(self.assignment_exe_path)
        

    def build(self) -> bool:
        print(f"  Building assignment {self.assignment_path}...")

        # Build the assignment.
        build_result = subprocess.run(["g++", self.assignment_path, "-o", self.assignment_exe_path], )

        if build_result.returncode != 0:
            print(f"  Failed to build assignment {self.assignment_path}.")
            return False
        else:
            print(f"  Completed building assignment {self.assignment_path} it is found at {self.assignment_exe_path}")
            return True
        
    def mark(self):
        print(f"  Marking assignment {self.assignment_path}...")

        for test in self.rubric.get("tests"):
            process = subprocess.Popen(
                [self.assignment_exe_path],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

            process.stdin.write(test.get("input"))
            process.stdin.flush() 

            output, error = process.communicate()

            print(f"    Input: {input} produced output: {output}")

            if error:
                print(f"    Error: {error}")

        print(f"  Completed marking assignment {self.assignment_path}.")