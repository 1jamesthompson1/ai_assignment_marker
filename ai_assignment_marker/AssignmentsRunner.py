import os
from ai_assignment_marker.AssignmentMarker import AssignmentMarker
from ai_assignment_marker.MarkingRubric import MarkingRubric

class AssignmentsRunner:
    def __init__(self, assignments_path, rubric_path):
        self.assignments_path = assignments_path
        self.rubric = MarkingRubric(rubric_path).get_rubric()

    def run(self):
        for assignment in self.get_assignments():
            print(f"Running assignment {assignment}...")

            AssignmentMarker(assignment, self.rubric).process()

            print(f"Completed assignment {assignment}.")

    def get_assignments(self):
        
        return [os.path.join(self.assignments_path, file) for file in os.listdir(self.assignments_path)]