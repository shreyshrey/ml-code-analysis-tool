Run and tested on: Apple pro, M1 chip, RAM - 16gb


## Code analysis tool - Unit test generator (testgen)

`testgen` is  local-first command-line tool that uses AI to generate unit tests for your source files. It runs entirly on your machine, ensuring your code ramins private, and works offline without any API dependencies.


### How it works
This tool uses the open-source language model (`codellama:7b`) to locally run on your machine via Ollama. It is designed with following principles in mind:
- Standard hardware - by using quantized model, this tool is deigned to be responsive on develoepr laptops and desktops, without requiring a high-end GPU.
- Private and secure - code will never to sent to third-party API.
- Language aggnostic - caters to major languages, it detect the programming language from the file extension and uses the approatie testing frame.


### Prerequisties
- Before you beging, please make sure you have the following software installed on your system:
1. Python: version 3.8 or newer
2. Ollama: tool that allows you to run the LLM locally on your machine. Download from https://ollama.com

### Setup and installation

To get `testgen` up and running

1. Clone the repo

```sh
git clone git@github.com:shreyshrey/ml-code-analysis-tool.git
cd ml-code-analysis-tool
```

2. Set up the AI model with Ollama
- Ensure Ollama is running - launche the Ollama application. It will run as a background service
- Download the model - `codellama:7b` as its provides a good balance of performance and resources usage for standard hardware.
```sh
ollama pull codellama:7b
```

3. Install the `testgen` tool
Install the tool and its dependencies into an isolated Python virtual environment
- Create and activate the virtual environment
```sh
python3 -m venv code-analysis-env

# Activate it (macOS/Linux)
source code-analysis-env/bin/activate

# or activate on Windows
# .\venv\Scripts\activate
```
The terminal prompt should be prefixed with `code-analysis-env`.

- Install the project - Install `testgen` in editable model, this reads te `pyproject.toml` file and makes the `testgen` command available.
```sh
pip install -e .
```

You are now fully set up! yay!

### How to use

There are two ways to set this up: via command line or integrate in into code editor (tested on vs code).

#### On Command-line 

`testgen [OPTIONS] FILEPATH`

Example:
1. Create a sample Python file (or any choice of your language - see the languages it supports at the bottom) in `example_files` folder: `example_files/merge.py`.

```python
def merge_dicts(*dicts):
  super_dict = {}
  for dict in dicts:
      for k, v in dict.items():
          super_dict[k] = v

 return super_dict
```

2. Run `testgen` on the file:

```sh
testgen example_files/merge.py
```

3. The tool will create a new test file at `tests/test_merge.py`.

Options:

- `--model TEXT`: specifcy which Ollama model to use. Defaults to `codellama:7b`.
- `--force`, `-f`: ovoerwrites the test file if already exists.


#### Languages it supports
- Python
- JavaScript
- TypeScript
- Java
- Go
- Rust
- Ruby
- C#

