def average_score(student):
    if not student:
        raise ValueError("cannot average an empty list")
    return round(sum(s.score for s in student) / len(student), 2)


if __name__ == "__main__":

    print(average_score([{"name": "Asha", "score": 82}]))
    print(average_score([]))



class Student:
    def __init__(self,name,score):
        if score < 0 or score > 100:
            raise ValueError(f" score must be between 0 and 100 , score: {score}")
        self.name = name
        self.score = score

        
    def grade(self):
        if self.score >= 90:
            return "Distinction"
        elif self.score >= 60:
            return "Pass"
        return "Fail"
