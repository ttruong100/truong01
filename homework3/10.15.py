#Thuyen Truong
#1780701

class Team:  #create class Team
    def __init__(self, team_name="none", team_wins=0, team_losses=0): #set defaults value
        self.team_name = team_name
        self.team_wins = team_wins
        self.team_losses = team_losses
    def get_win_percentage(self): #formula to get win percentage
        return self.team_wins / (self.team_wins + self.team_losses)


def myinput():
    myteam = Team()

    teamname = input()  #get inputs from user
    teamwins = int(input())
    teamlosses = int(input())

    myteam.team_name = teamname
    myteam.team_wins = teamwins
    myteam.team_losses = teamlosses

    if myteam.get_win_percentage() < 0.5:           #if the percentage is less than 50% or 0.5
        print("Team",teamname, "has a losing average.")         #then the team is losing
    else:
        print("Congratulations, Team", teamname, "has a winning average!")  #else if the percentage is 0.5 or more, than the team is winning



if __name__ == "__main__": myinput()
