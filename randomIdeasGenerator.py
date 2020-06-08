import random

companies = [
    "Google",
    "Wordpress",
    "Stack Overflow",
    "Github",
    "YouTube",
    "WIX",
    "Windows",
    "Mac OS",
    "Linux"
]

categories = [
    "website",
    "web app",
    "desktop app",
    "mobile app"
]

subject = [
    "CEO's",
    "developers",
    "designers",
    "average people",
    "builders"
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
