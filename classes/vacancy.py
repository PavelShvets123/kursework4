class Vacancy:

    def __init__(self, title, url, salary_min, salary_max, experience):
        self.title = title
        self.url = url
        self.salary_min = salary_min
        self.salary = salary_max
        self.experience = experience

    def to_dict(self):
        return {
            "title": self.title,
            "url": self.url,
            "salary": self.salary,
            "experience": self.experience
        }
