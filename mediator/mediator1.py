class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room = None  # mediator reference

    def receive(self, sender, message):
        s = f"{sender}: {message}"
        print(f"[{self.name}'s chat session] {s}")
        self.chat_log.append(s)

    def say(self, message):
        # delegate broadcast to mediator
        self.room.broadcast(self.name, message)

    def private_message(self, who, message):
        if self.room:
            self.room.message(self.name, who, message)


class ChatRoom:
    def __init__(self, room_name):
        self.people = []
        self.room_name = room_name  # identifies mediator

    def join(self, person):
        person.room = self
        self.broadcast("system", f"{person.name} joined the chat.")
        self.people.append(person)

    def broadcast(self, source, message):
        # notify all participants except sender
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def message(self, source, destination_name, message):
        # targeted communication between participants
        for p in self.people:
            if p.name == destination_name:
                p.receive(source, message)
                break

    def leave(self, person):
        if person in self.people:
            self.people.remove(person)
            person.room = None  # detach from mediator

    def __repr__(self):
        return f"ChatRoom('{self.room_name}', members={len(self.people)})"


if __name__ == "__main__":
    # concrete mediator orchestrating chat participants
    room = ChatRoom("Job Discussions")

    john = Person("John")
    jane = Person("Jane")

    room.join(john)
    room.join(jane)

    john.say("hi room!")
    jane.say("oh, hey jhon!")

    simon = Person("Simon")
    room.join(simon)
    simon.say("hi everyone!")

    jane.private_message("Simon", "glad you joined us!")

    print(room)
    room.leave(simon)
    print(room)
    
    jane.say("Simon left, finally!")