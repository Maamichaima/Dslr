

import matplotlib.pyplot as plt


class Histogram:

    def __init__(self, data):
        self.data = data

    def get_courses(self):
        """
        Return the list of courses.
        We exclude Index and Hogwarts House.
        """
        courses = []

        for column in self.data.columns:
            if column != "Index" and column != "Hogwarts House":
                courses.append(column)

        return courses

    # def get_scores_by_house(self, course):
    #     """
    #     Separate the scores of one course by Hogwarts House.
    #     """

    #     gryffindor = []
    #     hufflepuff = []
    #     ravenclaw = []
    #     slytherin = []

    #     for i in range(len(self.data)):

    #         house = self.data["Hogwarts House"][i]
    #         score = self.data[course][i]

    #         # Ignore missing values
    #         if score != score:
    #             continue

    #         if house == "Gryffindor":
    #             gryffindor.append(score)

    #         elif house == "Hufflepuff":
    #             hufflepuff.append(score)

    #         elif house == "Ravenclaw":
    #             ravenclaw.append(score)

    #         elif house == "Slytherin":
    #             slytherin.append(score)

    #     return (
    #         gryffindor,
    #         hufflepuff,
    #         ravenclaw,
    #         slytherin
    #     )
    
    def histogram_for_course(self, course, df):
        """
        Display the histogram of one course
        for the four Hogwarts houses.
        """

        # (
        #     gryffindor,
        #     hufflepuff,
        #     ravenclaw,
        #     slytherin
        # ) = self.get_scores_by_house(course)

        plt.figure(figsize=(10, 6))

        plt.hist(
            df["Gryffindor"],
            bins=30,
            alpha=0.5,
            label="Gryffindor"
        )

        plt.hist(
            df["Hufflepuff"],
            bins=30,
            alpha=0.5,
            label="Hufflepuff"
        )

        plt.hist(
            df["Ravenclaw"],
            bins=30,
            alpha=0.5,
            label="Ravenclaw"
        )

        plt.hist(
            df["Slytherin"],
            bins=30,
            alpha=0.5,
            label="Slytherin"
        )

        plt.title(course)
        plt.xlabel("Score")
        plt.ylabel("Number of students")

        plt.legend()
        plt.grid(True, alpha=0.2)

        plt.show()
    def show_all_histograms(self, df):
        """
        Display one histogram for every course.
        """

        courses = self.get_courses()

        for course in courses:
            self.plot_histogram(course)