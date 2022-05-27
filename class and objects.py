class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score

    def change_name(self, new_name):
        self.name = new_name

    def change_age(self, new_age):
        if isinstance(new_age, int):
            self.age = new_age

    def add_track(self, new_track):
        self.track.append(new_track)

    def get_score(self):
        return self.score