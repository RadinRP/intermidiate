players = [
    {
        "id" : "ali",
        "score" : 100,
        "level" : 3 ,
        "coin" : 100
    },
    {
        "id" : "reza",
        "score" : 20,
        "level" : 2 ,
        "coin" : 10
    },
    {
        "id" : "mohammad",
        "score" : 50,
        "level" : 8 ,
        "coin" : 1000
    },
    {
        "id" : "radin",
        "score" : 1000,
        "level" : 17 ,
        "coin" : 250
    }
]
for player in players:
    if player["id"] == "radin":
        player["coin"] += 50
    print(player["id"],player["coin"])