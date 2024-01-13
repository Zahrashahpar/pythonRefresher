print("Hello world!")

a = 10
b = "salam"
c = [a, b]
print(c[1])

c = c * 10
for i in c:
    print(i)

print(c[0:5])
print(c[5::2])

d = {
    "name": "Zahra",
    "job": "student",
    "favorites": {
        "food": "pizza",
        "color": "blue",
        "language": "Python"
    }
}

if d["favorites"]["language"].lower() == "python":
    print("Python is awesome!")


def my_function(inp):
    return f"I am a function and I got {inp} as input!"


if __name__ == '__main__':
    print(my_function(input("Enter your input: ")))
