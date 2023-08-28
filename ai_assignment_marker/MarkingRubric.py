import yaml

class MarkingRubric:
    def __init__(self, rubric_path) -> None:
        self.rubric = self.read_rubric(rubric_path)

    def read_rubric(path):
        with open(path) as rubric_file:
            return yaml.safe_load(rubric_file)
        
    def get_tests(self):
        return self.rubric
