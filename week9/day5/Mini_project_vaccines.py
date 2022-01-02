class Human:
    def __init__(self, id_number: str, name: str, age: int, priority: bool, blood_type: str):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type

    def add_family_member(self, person):
        self.family.append(person)

    def __str__(self):
        return f"name: {self.name} age: {self.age} priority: {self.priority}"


class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person: Human):
        if person.age > 60 or person.priority:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)

    def find_in_queue(self, person: Human):
        for index in range(len(self.humans)):
            if self.humans[index].id_number == person.id_number:
                return index
            return -1

    def swap(self, person1, person2):
        person1_index = self.find_in_queue(person1)
        person2_index = self.find_in_queue(person2)
        self.humans[person1_index] = person2
        self.humans[person2_index] = person1

    def get_next(self):
        return self.humans[0]

    def get_next_blood_type(self, blood_type):
        for human in self.humans:
            if blood_type == human.blood_type:
                return human

        return None

    @staticmethod
    def get_age(human):
        return human.age

    @staticmethod
    def get_priority(human):
        return 1 if human.priority else 0

    def sort_by_age(self):
        self.humans.sort(key=Queue.get_age, reverse=True)
        self.humans.sort(key=Queue.get_priority, reverse=True)

    def __str__(self):
        humans = []
        for index in range(len(self.humans)):
            humans.append(str(self.humans[index]))

        return "\n".join(humans)

    def rearrange_queue(self):
        for i in range(len(self.humans)):
            if self.waiting_humans[i] and self.humans[i + 1] in Human.family:
                self.swap(i + 1, i + 2)


evelyn = Human("0123", "Evelyn", 28, False, "O")
adriel = Human("4567", "Adriel", 18, False, "B")
maria = Human("8910", "Maria", 48, True, "O")
claudio = Human("1112", "Claudio", 49, False, "B")
susana = Human("1314", "Susana", 69, True, "AB" )
angelica = Human("1516", "Angelica", 69, True, "O")

queue = Queue()

queue.add_person(evelyn)
queue.add_person(adriel)
queue.add_person(maria)
queue.add_person(claudio)
queue.add_person(susana)
queue.add_person(angelica)

print(queue.find_in_queue(evelyn))
print(queue.find_in_queue(adriel))
print(queue.find_in_queue(maria))
print(queue.find_in_queue(claudio))
print(queue.find_in_queue(susana))
print(queue.find_in_queue(angelica))

queue.sort_by_age()
print(queue)
queue.swap(person1=evelyn, person2=susana)
print(queue.find_in_queue(evelyn))
print(queue.find_in_queue(maria))
print(queue.find_in_queue(susana))
