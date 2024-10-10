pwd = "12e324324"

if len(pwd) < 6:
    strength = "Weak"
elif len(pwd) < 10:
    strength = "Medium"
else:
    strength = "Strong"

print(strength)
