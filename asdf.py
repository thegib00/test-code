jobs = {
    "Oil change": "$35",
    "Tire rotation": "$19",
    "Car wash": "$7",
    "Car wax": "$12"
}

display = """Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12 """

print(display)

input1 = input()
input2 = input()

def whatService():
    for item in jobs:
        if item == input1:
            new = item
            del item[
            return new
        elif item == input2:
            new = item
            return new
        elif item == '-':
            return 'No service'
        else:
            continue

test = 'test'

print(f"""Davy's auto shop invoice
Service 1: {whatService()}
Service 2: {whatService()}

Total: {test}""")
