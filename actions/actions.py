# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher 
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict

from readdatadb import fetch_about_program, fetch_deadline, fetch_how_to_apply, fetch_link, fetch_who_can_apply,fetch_details_program
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class ProgramNameForm(Action):
    def name(self) -> Text:
        return "program_name_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["program_name"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not yet filled, request user to fill this slot next
                print("result00",slot_name)
                return [SlotSet("requested_slot", slot_name)]

        # All slots filled 
        return [SlotSet("requested_slot", None)]

class AboutProgram(Action):
    def name(self) -> Text:
        return "action_about_program"

    def run(
        self,
        dispatcher,
        tracker:Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text,Any]]:
        buttons = []
        result = fetch_about_program(tracker.get_slot("program_name"))
        # result = str(result)
        for index, program_name in enumerate(result):
            if index == 5:
                break
            rst = program_name.program_name
            # dispatcher.utter_message(rst)
            buttons.append({"title": rst, "payload": "/program_details{'button_slot':"+rst+"}"})
        # dispatcher.utter_message(result)
        # dispatcher.utter_message(response="utter_know_more_education_part")
        dispatcher.utter_message(text="Programs:", buttons=buttons)        
        return []

class anotherProgram(Action):
    def name(self) -> Text:
        return "action_anotherProgram"

    def run(
        self,
        dispatcher,
        tracker:Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text,Any]]:
        
        dispatcher.utter_message(template="utter_happy")
        # dispatcher.utter_message(result)
        #dispatcher.utter_message(response="utter_know_more_education_part")
        return [SlotSet("program_name", None)]

class WhoCanApply(Action):
    def name(self) -> Text:
        return "action_who_can_apply"

    def run(
        self,
        dispatcher,
        tracker:Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text,Any]]:
        
        result = fetch_who_can_apply (tracker.get_slot("program_name"))
        result = str(result)
        dispatcher.utter_message(result)
        dispatcher.utter_message(template="utter_know_more_education_part")
        return []

class Deadline(Action):
    def name(self) -> Text:
        return "action_deadline"

    def run(
        self,
        dispatcher,
        tracker:Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text,Any]]:
        
        result = fetch_deadline(tracker.get_slot("selected_program_name"))
        result = str(result)
       
        dispatcher.utter_message(result)
        dispatcher.utter_message(template="utter_know_more_education_part")
        return []

class HowToApply(Action):
    def name(self) -> Text:
        return "action_how_to_apply"

    def run(
        self,
        dispatcher,
        tracker:Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text,Any]]:
        
        result = fetch_how_to_apply(tracker.get_slot("selected_program_name"))
        result = str(result)
       
        dispatcher.utter_message(result)
        dispatcher.utter_message(template="utter_know_more_education_part")
        return []
class Link(Action):
    def name(self) -> Text:
        return "action_link"

    def run(
        self,
        dispatcher,
        tracker:Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text,Any]]:
        
        result = fetch_link(tracker.get_slot("selected_program_name"))
        result = str(result)
       
        dispatcher.utter_message(result)
        dispatcher.utter_message(response="utter_know_more_education_part")
        return [SlotSet("program_name", None)]
        # return []

class anotherProgram(Action):
    def name(self) -> Text:
        return "action_anotherProgram"

    def run(
        self,
        dispatcher,
        tracker:Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text,Any]]:
        
        dispatcher.utter_message(template="utter_happy")
        # dispatcher.utter_message(result)
        #dispatcher.utter_message(response="utter_know_more_education_part")
        return [SlotSet("program_name", None)]
class getUserId(Action):
    def name(self) -> Text:
        return "getUserId"

    def run(
        self,
        dispatcher,
        tracker:Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text,Any]]:
        
        userId = tracker.get_slot("userId")
        print("userId",userId)
        # dispatcher.utter_message(result)
        #dispatcher.utter_message(response="utter_know_more_education_part")
        return [SlotSet("userId",userId)]

class bussinessSupport(Action):
    def name(self) -> Text:
        return "action_bussinessSupport"

    def run(
        self,
        dispatcher,
        tracker:Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text,Any]]:
        
        result = fetch_bussinessSupport(tracker.get_slot("selected_program_name"))
        result = str(result)
        dispatcher.utter_message(result)  
        dispatcher.utter_message(template="utter_bussiness_support")
        return []
        
class WhoCanApply(Action):
    def name(self) -> Text:
        return "action_who_can_apply"

    def run(
        self,
        dispatcher,
        tracker:Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text,Any]]:
        
        result = fetch_who_can_apply (tracker.get_slot("selected_program_name"))
        result = str(result)
        dispatcher.utter_message(result)
        dispatcher.utter_message(template="utter_know_more_education_part")
        return []

class programDetails(Action):
    def name(self) -> Text:
        return "action_programDetails"

    def run(
        self,
        dispatcher,
        tracker:Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text,Any]]:
        print("program_name",str(tracker.latest_message['text']).split(":",1)[1].replace("}",""))
        prog_name = str(tracker.latest_message['text']).split(":",1)[1].replace("}","")
        result = fetch_details_program(prog_name)
        result = str(result)
        dispatcher.utter_message(result)
        dispatcher.utter_message(text="Call 1-800-567-9604 for more details")
        dispatcher.utter_message(template="utter_know_more_education_part")
        return[SlotSet("selected_program_name", prog_name)]