import json
import sys
import os
from rasa_nlu.model import Interpreter
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

def train():
    training_data = load_data('data/nlu.md')
    conf = RasaNLUConfig("nlu_config.json")
    trainer = Trainer(RasaNLUConfig("nlu_config.json"))
    trainer.train(training_data)
    model_directory = trainer.persist(conf["path"],project_name=conf["project"],fixed_model_name=conf["fixed_model_name"])
    print("persisted model to ",model_directory)


def do_nlu_eval(txt):
    # where `model_directory points to the folder the model is persisted in
    interpreter = Interpreter.load("models/infosys_cui/current", RasaNLUConfig("nlu_config.json"))
    return interpreter.parse(txt)



if __name__=="__main__":
    # cd to project src dir
    src_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    os.chdir(src_dir)
    if len(sys.argv) >= 2:
        command = sys.argv[1]
        if command in ("-h","-help"):
            print("so, you want help, huh?")
        elif command == "nlu_eval":
            if len(sys.argv) < 3:
                print("please provide a string to evaluate")
            else:
                txt = sys.argv[2]
                eval_result = do_nlu_eval(txt)
                print(json.dumps(eval_result,indent=4))
        elif command == "nlu_train":
            train()


