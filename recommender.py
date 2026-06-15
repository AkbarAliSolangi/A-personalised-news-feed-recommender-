news = {
    "Technology": ["AI Revolution"],
    "Sports": ["Cricket World Cup"],
    "Business": ["Stock Market Update"]
}

interest = input("Enter your interest: ")

if interest in news:
    print("Recommended News:")
    for article in news[interest]:
        print(article)
else:
    print("No recommendations found.")
