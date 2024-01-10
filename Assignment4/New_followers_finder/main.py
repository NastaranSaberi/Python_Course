import instaloader
import getpass


# Read old followers
file = open("followers.txt","r")
old_followers = []

for line in file :
    old_followers.append(line)

file.close()


# Login in instagram 
L = instaloader.Instaloader()

username = input("username: ")
password = getpass.getpass("pass: ")

L.login(username,password)
print("Successful login ✅")


# go to profile 
profile = instaloader.Profile.from_username(L.context,"nstrn_saberi")


# List new followers
new_followers = []

for follower in profile.get_followers() :
    new_followers.append(follower.username)


# instagram new followers finder
file = open("instagramNewFollowersFinder.txt" , "w")

for new_follower in new_followers:
    file.writelines(new_follower)

if new_followers == [] :
    file.write("You dont have new follower .")

file.close()


# Comparison
for old_follower in old_followers :
    if old_follower not in new_followers :
        print(old_follower)


# update list new followers
file = open("followers.txt","w")

for follower in new_followers :
    file.writelines(follower)

file.close()

