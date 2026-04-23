from email.base64mime import body_decode


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        body = self.scores[index]
        if 90 <= body <= 100:
            return "A"
        elif 80 <= body <= 89:
            return "B"
        elif 70 <= body <= 79:
            return "C"
        elif 60 <= body <= 69:
            return "D"
        elif 50 <= body <= 59:
            return "E"
        elif 0 <= body <= 49:
            return "F"

    def find(self, body):
        for i in range(len(self.scores)):
            if self.scores[i] == body:
                kolikaty = i
        return kolikaty

    def get_sorted(self):
        nums = self.scores.copy()
        n = len(nums)
        for i in range(n - 1):
            for j in range(n - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    pocet = results.count()
    vypsat_indexy= []
    for index, i in enumerate(results.scores):
        znamka = results.get_grade(index)
        print(f"Student {index}: {i} points - {znamka}")
        if i == 100:
            vypsat_indexy.append(index)
    print(vypsat_indexy)
    serazeny = results.get_sorted()
    print(serazeny)

if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())          # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    print(results.get_grade(2))
    print(results.find(42))
    print(results.get_sorted())
    print(main())