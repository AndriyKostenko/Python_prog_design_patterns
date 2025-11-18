class Event(list):
    def __call__(self, *args, **kwargs):
        # iterate through registered handlers and invoke them with provided arguments
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        self.events = Event()  # mediator event list

    def fire(self, args):
        self.events(args)  # propagate event arguments to all subscribers


class GoalScoredInfo:
    def __init__(self, who_scored, goals_scored):
        self.who_scored = who_scored  # player name
        self.goals_scored = goals_scored  # number of goals scored


class Player:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.goals_scored = 0

    def score(self):
        self.goals_scored += 1
        args = GoalScoredInfo(self.name, self.goals_scored)
        # notify mediator that a goal has been scored
        self.game.fire(args)


class Coach:
    def __init__(self, game):
        game.events.append(self.celebrate_goal)  # subscribe to goal events

    def celebrate_goal(self, args):
        if isinstance(args, GoalScoredInfo) and args.goals_scored < 3:
            # respond to early goals only
            print(f"Caoch said: well donw, {args.who_scored}")


if __name__ == "__main__":
    game = Game()
    player = Player('Sam', game)
    coach = Coach(game)

    player.score()
    player.score()
    player.score()