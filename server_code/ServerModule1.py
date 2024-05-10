import anvil.users
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def submit(name, weight, mobileNo, personaltraining):
 app_tables.gym.add_row(name=name, weight=weight, mobileNo = mobileNo, personaltraining = personaltraining)
 anvil.email.send(to="dpramod150@gmail.com", subject="Response from anvil app", 
                          text=f"feedback from {name}: weight is {weight} and Personal Training required: {personaltraining}")