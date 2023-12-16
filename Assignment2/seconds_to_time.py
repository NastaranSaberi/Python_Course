time = int(input("Please enter seconds:"))

hours = int(time // 3600)
minutes = int((time % 3600) // 60)
seconds = time % 60

print ("Time: ", hours , ":" , minutes , ":" ,seconds)