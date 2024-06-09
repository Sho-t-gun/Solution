import re

def extract_numbers(s):
    return list(map(int, re.findall(r'\d+', s)))


s = "В 2020 году было много событий, а в 2021 еще больше."
result = extract_numbers(s)
print(result)