def convert(number):
    word = {3: "Pling", 5: "Plang", 7: "Plong"}
    result = "".join(word[num] for num in word if number % num == 0)
    return result or str(number)
