def convert(number):
    words = {3: "Pling", 5: "Plang", 7: "Plong"}
    result = "".join(words[num] for num in words if number % num == 0)
    return result or str(number)
