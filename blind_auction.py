from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
print("Welcome to the secret auction program")
new_dict = {}
#bidding_amount
def find_bidder():
  all_values = new_dict.values()
  bidding_amount = max(all_values)
  # list out keys and values separately
  key_list = list(new_dict.keys())
  val_list = list(new_dict.values())
  position = val_list.index(bidding_amount)
  x = key_list[position]
  print(f"The winner is {x} with a bid of {bidding_amount}")


program_running = True
while program_running:
  clear()
  key = input("What is your name?: ")
  value = int(input("What is your highest bid?: $"))
  new_dict[key] = value
  add_user = input("Any other bidders, 'yes' or 'no': ")
  if add_user == "yes":
    program_running = True
  elif add_user == "no":
    program_running = False
    find_bidder()

