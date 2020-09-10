from rasa_core_sdk import Tracker
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher


class BookingConfirm(Action):
	def name(self):
		return "action_confirmation"
		
	def run(self, dispatcher, tracker, domain):
		no_of_people=tracker.slots['number_of_people']
		time=tracker.slots['time']
		date=tracker.slots['date']
		if date==None or no_of_people==None or time==None:
			response="Couldn't make reservations due to incomplete information received"
		else:
			response="""The table is booked for {} , {} at {} .""".format(no_of_people,date,time)				
		dispatcher.utter_message(response)
		return ''