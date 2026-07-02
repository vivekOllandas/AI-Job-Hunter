from typing import List
from scripts.common.job_model import Job


class IndeedSearcher:
    def __init__(self):
        self.source = "Indeed"

    def search(self, keyword: str, location: str) -> List[Job]:
        """
        Placeholder implementation.
        We'll replace this with the actual Indeed search logic.
        """
        return []