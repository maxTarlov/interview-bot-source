from tkinter import Tk, filedialog
import json
import os

Tk().withdraw()  # prevents extra window

with filedialog.askopenfile(initialdir='~') as input_file:
    base_name = os.path.basename(input_file.name)
    if base_name.split('.')[-1] != 'ipynb':
        raise ValueError("Expected file extension '.ipynb'")
    input_obj = json.load(input_file)

output_obj = {key: val for key, val in input_obj.items() if key != 'cells'}
output_obj['cells'] = []

for cell in input_obj['cells']:
    if cell['cell_type'] == 'code':
        output_obj['cells'].append({key: val for key, val in cell.items() if key != 'outputs'})

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'notebooks')
with open(os.path.join(OUTPUT_DIR, base_name), 'w') as output_file:
    json.dump(output_obj, output_file )
