import random

companies = [
    "Google",
    "Wordpress",
    "Stack Overflow",
    "Github",
    "YouTube",
    "WIX",
    "Windows 7",
    "Windows 10",
    "Mac OS",
    "Linux",
    "PowerPoint",
    "Blender",
    "VirtualBox",
    "Audacity",
    "Unix",
    "MS-DOS"
]

categories = [
    "website",
    "web app",
    "desktop app",
    "mobile app",
    "development environment",
    "game",
    "game engine",
    "programming language",
    "shell",
    "operating system"
]

subject = [
    "CEO's",
    "developers",
    "designers",
    "average people",
    "business owners"
]

while True:
    currentIdea = "A " + random.choice(categories) + " like " + random.choice(companies) + " for " + random.choice(subject)
    print(currentIdea)
    goodOrBad = input("Do you like the sound of that idea? (y/n): ")
    if goodOrBad == "y" or goodOrBad == "Y":
        f = open("goodIdeas.txt", "a+")
        f.write(currentIdea + "\n")
        f.close()

    print()
