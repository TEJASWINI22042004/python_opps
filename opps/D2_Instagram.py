# Class Definition
class Instagram:
    
    # Class Attribute (shared by all objects)
    platform_name = "Instagram"
    
    # Constructor Method
    def __init__(self, title, description, creator_name, location):
        # Instance Variables (unique for each object)
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.likes = 0
        self.comments = []   # List to store comments

    # Method to display title
    def display_title(self):
        print("Title of the reel:", self.title)

    # Method to display description
    def display_description(self):
        print("Description of the reel:", self.description)

    # Method to display creator name
    def display_creator(self):
        print("Creator of the reel:", self.creator_name)

    # Method to display location
    def display_location(self):
        print("Location of the reel:", self.location)

    # Method to display likes
    def display_likes(self):
        print("Likes:", self.likes)

    # Method to like the reel
    def liked(self):
        self.likes += 1

    # Method to dislike the reel
    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

    # Method to add comment
    def add_comment(self, comment):
        self.comments.append(comment)

    # Method to display all comments
    def display_comments(self):
        print("Comments:")
        for comment in self.comments:
            print("-", comment)


# Object Instantiation
reel1 = Instagram("Dancing", "Dancing with friends", "Teja", "Hyderabad")
reel2 = Instagram("Finance Conference", "Finance Minister Conference", "Rahul", "Delhi")

# Performing operations
reel1.liked()
reel1.liked()
reel1.add_comment("Nice video!")
reel1.add_comment("Awesome dance!")

reel2.liked()
reel2.add_comment("Very informative!")

# Display details
reel1.display_title()
reel1.display_creator()
reel1.display_location()
reel1.display_likes()
reel1.display_comments()

print("--------------------")

reel2.display_title()
reel2.display_creator()
reel2.display_location()
reel2.display_likes()
reel2.display_comments()

# Memory Allocation
print("Memory address of reel1:", id(reel1))
print("Memory address of reel2:", id(reel2))