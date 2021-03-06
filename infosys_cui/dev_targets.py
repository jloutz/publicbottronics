import json
import sys
import os

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter, RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_nlu.model import Interpreter
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer


def train_nlu():
    training_data = load_data('data/nlu.md')
    conf = RasaNLUConfig("nlu_config.json")
    trainer = Trainer(RasaNLUConfig("nlu_config.json"))
    trainer.train(training_data)
    model_directory = trainer.persist(conf["path"], project_name=conf["project"],
                                      fixed_model_name=conf["fixed_model_name"])
    print("persisted model to ", model_directory)


def do_nlu_eval(txt):
    # where `model_directory points to the folder the model is persisted in
    interpreter = Interpreter.load("models/infosys_cui/current", RasaNLUConfig("nlu_config.json"))
    return interpreter.parse(txt)


def train_dialog(online=False,nlu=False,policies = [KerasPolicy()]):
    agent = Agent("domain.yml", policies=policies)
    stories = "data\stories.md"
    output_path = "models\dialog"
    if online:
        if nlu:
            agent.interpreter = RasaNLUInterpreter("models/infosys_cui/current")
        else:
            agent.interpreter = RegexInterpreter()
        agent.train_online(
                stories,
                input_channel=ConsoleInputChannel(),
                epochs=10,
                model_path=output_path)
    else:
        kwargs = {"epochs": 300}
        agent.train(
                stories,
                validation_split=0.1,
                **kwargs
        )

    agent.persist(output_path)


def run():
    from rasa_core.run import main
    main("models\dialog",nlu_model="models/infosys_cui/current",channel="cmdline")

if __name__ == "__main__":
    # cd to project src dir
    src_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    os.chdir(src_dir)
    if len(sys.argv) >= 2:
        command = sys.argv[1]
        if command in ("-h", "-help"):
            print("so, you want help, huh?")
        elif command == "nlu_eval":
            if len(sys.argv) < 3:
                print("please provide a string to evaluate")
            else:
                txt = sys.argv[2]
                eval_result = do_nlu_eval(txt)
                print(json.dumps(eval_result, indent=4))
        elif command == "nlu_train":
            train_nlu()
        elif command == "dialog_train":
            train_dialog()
        elif command == "interactive_train":
            train_dialog(online=True)
        elif command == "run":
            run()
