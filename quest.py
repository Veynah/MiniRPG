class Quest:
    def __init__(self, quest_name, quest_description):
        self.quest_name = quest_name
        self.quest_description = quest_description
        self.is_completed = False

    def complete_quest(self):
        self.is_completed = True
        print(f"Quest '{self.quest_name}' completed!")

    def display_quest(self):
        print("Quest Details:")
        print(f"Name: {self.quest_name}")
        print(f"Description: {self.quest_description}")
        if self.is_completed:
            print("Status: Completed")
        else:
            print("Status: In Progress")


quest1 = Quest("Rescue the Princess", "Save the princess from the clutches of the vampire.")
quest1.display_quest()
# Output:
# Quest Details:
# Name: Rescue the Princess
# Description: Save the princess from the clutches of the vampire.
# Status: In Progress

quest1.complete_quest()
# Output: Quest 'Rescue the Princess' completed!

quest1.display_quest()
# Output:
# Quest Details:
# Name: Rescue the Princess
# Description: Save the princess from the clutches of the vampire.
# Status: Completed
