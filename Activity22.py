anime_type = ["Gojo", "Satoru",  "Jujutsu Kisen"]
anime_title = []

while True:
    ans = input("Do you know any anime --> (yes / no)? ")

    if ans.lower() == "yes":
        print("What is its type -- select from the list")

        for x in anime_type:
            print(x)

        a_type = input("type --> ")
        title = input("What is the title of the anime --> ")

        anime_title.append(title)
        continue

    else:
        print("Thank you")
        break