#Menghilangkan huruf vokal

tu = "aiueoAIUEO"
hi = input("")
for letter in hi:
    if letter in tu:
        hi = hi.replace(letter,"")
print(hi)
