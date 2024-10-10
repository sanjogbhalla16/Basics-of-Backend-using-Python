file = open('youtube.txt','w')

try:
    file.write("Hello World") # This is a valid statement
finally:
    file.close()
    
with open('youtube.txt','w') as file:
    file.write('chai aur python\n')