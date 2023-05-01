katz_deli = ['Geoffrey', 'John']

def line(katz_deli):
  if len(katz_deli) == 0:
      print("The line is currently empty.")
  else:
      message = "The line is currently:"
      for person in katz_deli:
        message += f" {katz_deli.index(person) + 1}. {person}"
      print(message)

def take_a_number(katz_deli, name):
  katz_deli.append(name)
#   print(katz_deli)
  print(f"Welcome, {name}. You are number {katz_deli.index(name) + 1} in line.")

def now_serving(katz_deli):
  if len(katz_deli) == 0:
    print("There is nobody waiting to be served!")
  else:
    print(f'Currently serving {katz_deli[0]}.')
    katz_deli.pop(0)
#   print(katz_deli)
