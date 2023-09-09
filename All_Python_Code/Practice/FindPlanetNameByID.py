def planet(id):
    planets = {1:'Mercury',2:'Venus',3:'Earth',4:'Mars',
               5:'Jupiter',6:'Saturn',7:'Uranus',8:'Neptune',
               9:'Pluto'}
    if id in planets:
        return f"Planet Name is {planets[id]}"
    else:
        return "Invalid Id."

if __name__ == "__main__":
    id = int(input("Enter Id : "))
    print(planet(id))