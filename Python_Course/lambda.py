people = [{"name": "Ahmad", "city": "Faisalabad"},
          {"name": "Ammar", "city": "Lahore"},
          {"name": "Sharique", "city": "Karachi"}]

# two ways to sort such nested data structure.

# 1.

# def sorting(f):
#    return f["city"]

# people.sort(key=sorting)

# OR simply

# 2.
people.sort(key=lambda f: f["city"])


print(people)
