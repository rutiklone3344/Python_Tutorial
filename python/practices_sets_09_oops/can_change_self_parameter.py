# can you change the self parameter inside a class to something else(say 'Rutik')
# Try changing self to "Slf" or "Rutik" and see the effects

class sample:
    def __init__(hytj, name):  #yes we change the self parameter with anything
        hytj.name = name

obj = sample("Rutik")
print(obj.name)
