class items():
    onehandsword1={"attack": 5, "defense": 5, "speed":1, "type": "one handed sword"}
    onehandsword2={"attack": 15, "defense": 10, "speed": 1, "type": "one handed s"}

class player():
    item: None

player.item = items.onehandsword1
print(player.item["attack"])