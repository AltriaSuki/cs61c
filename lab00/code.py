def get_airspeed_velocity_of(unladen_swallow):
  if unladen_swallow.type == "african":
    return # redacted
  elif unladen_swallow.type == "european":
    return # redacted

# pretend there's code here...

def fizzbuzz(num):
<<<<<<< HEAD
  if num%3==0 and num%5==0:
    print(f"{num}: fizzbuzz")
  if num %3==0: # edit this line
    print(f"{num}: fizz")
  if num %5 == 0: # edit this line
=======
  if str(num) in ["15"]:
    print(f"{num}: fizzbuzz")
  elif str(num) in ["3", "6", "9", "12", "15", "18"]:
    print(f"{num}: fizz")
  elif str(num) in ["5", "10", "15"]:
>>>>>>> 0bdba63993cd46d120b74cf550d3d551c99b32f3
    print(f"{num}: buzz")

for i in range(1, 20):
  fizzbuzz(i)

# pretend there's code here...
