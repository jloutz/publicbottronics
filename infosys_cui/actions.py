from rasa_core.actions import Action
from rasa_core.events import SlotSet
from rasa_core.trackers import DialogueStateTracker


class ActionEvalEingabekanal(Action):
    def name(self):
        return "action_eval_eingabekanal"

    def run(self, dispatcher, tracker:DialogueStateTracker, domain):
        anz_kurs = tracker.get_slot("anz_kuerse")
        change_freq = tracker.get_slot("change_freq")
        eingabe_kanal = "online"
        if int(anz_kurs) > 50:
            if change_freq in ["täglich","wöchentlich"]:
                eingabe_kanal = "xml"

        return [SlotSet(key="empfohlenes_kanal",value=eingabe_kanal)]


class ActionEvalEingabeverfahren(Action):
    def name(self):
        return "action_eval_eingabeverfahren"

    def run(self, dispatcher, tracker:DialogueStateTracker, domain):
        kanal = tracker.get_slot("empfohlenes_kanal")
        auf_ok = tracker.get_slot("aufwand_ok")
        verfahren = "redaktion"
        if auf_ok == "ja":
            verfahren = "selbst_"+kanal
        elif auf_ok == "nein":
            if kanal == "xml":
                verfahren = "extern_xml"

        return [SlotSet(key="empfohlenes_verfahren",value=verfahren)]