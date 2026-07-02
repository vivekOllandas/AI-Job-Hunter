from search import IndeedSearcher

searcher = IndeedSearcher()

jobs = searcher.search(
    keyword="Data Analyst",
    location="India"
)

print(jobs)