#using huggingface api
from transformers import pipeline
import torch
import json
from dict_creator import create_dict

#reading inputs
with open("input.txt") as f:
    inputs = f.readlines()

#creating the pipeline for text generation
pipe = pipeline("text-generation")

#returns a list of responses from gpt-2
outputs = pipe(
    inputs,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    top_p=0.95
)

#writing the outputs to the outputs.json file
json_object = json.dumps(create_dict(outputs), indent=4)
with open("output.json", "w") as outfile:
    outfile.write(json_object)
