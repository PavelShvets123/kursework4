class Vacancy:

    def __init__(self, title, url, salary_min, salary_max, experience):
        self.title = title
        self.url = url
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.experience = experience

    def __str__(self):
        return f"""{self.title}
{self.url}
От {self.salary_min} до {self.salary_max}
{self.experience}"""

    def to_dict(self):
        return {
            "title": self.title,
            "url": self.url,
            "salary_min": self.salary_min,
            "salary_max": self.salary_max,
            "experience": self.experience
        }
