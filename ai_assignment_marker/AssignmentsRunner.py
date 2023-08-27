import os

class AssignmentsRunner:
    def __init__(self, assignments_path):
        self.assignments_path = assignments_path

    def run(self):
        for assignment in self.get_assignments():
            print(f"Running assignment {assignment}...")

            # Call assginment marker and pass the path to the file.

            print(f"Completed assignment {assignment}.")

    def get_assignments(self):
        
        return os.listdir(self.assignments_path)