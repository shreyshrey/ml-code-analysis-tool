Ran and tested on: Apple MacBook Pro, M1 chip, RAM - 16gb


## Code analysis tool - Unit test generator (testgen)

`testgen` is  local-first command-line tool that uses AI to generate unit tests for your source files. It runs entirly on your machine, ensuring your code ramins private, and works offline without any API dependencies.


### How it works
This tool uses the open-source language model (`qwen2.5-coder:7b`) to locally run on your machine via Ollama. It is designed with following principles in mind:
- Standard hardware - by using quantized model, this tool is deigned to be responsive on developer laptops and desktops, without requiring a high-end GPU.
- Private and secure - code will never to sent to third-party API.
- Language agnostic - caters to major languages, it detect the programming language from the file extension and uses the appropriate testing frame.


### Prerequisties
- Before you begin, please make sure you have the following software installed on your system:
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
- Ensure Ollama is running - launch the Ollama application. It will run as a background service
- Download the model - `qwen2.5-coder:7b` as its provides a good balance of performance and resources usage for standard hardware.
```sh
ollama run qwen2.5-coder:7b
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

- `--model TEXT`: specify which Ollama model to use. Defaults to `qwen2.5-coder:7b`.
- `--force`, `-f`: overwrites the test file if already exists.


#### Languages the tool supports
- Python
- JavaScript
- TypeScript
- Java
- Go
- Rust
- Ruby
- C#


#### Common troubleshotting
- `ModuleNotFoundError: No module named test_generator`: this means that your virtual environment is not active in th terminal where you are running the command. 
- `Error: could not connect to Ollama`: this means that the Ollama server is not running on your machine.

### Design decision and trad-off

This section detail the technical decision, assumptions and trad-offs made during the development of this tool.

**Local tool:** Ollama <br>
**Alternatives that were considered:** LM studio, GPT4ALL <br>
**Why Ollama:** its flexible, controlled anc customised. For more advanced users such as developers, while other are more user-friendly. It is full open-source and available for all major OS. It is secure when working with sensitive codebase. It also avoid network latency and cannot be dependent on issues such as deprecation or outage.

**Model:** `qwen2.5-coder:7b` <br>
**Alternatives that were considered:** `codellama:7b`. Larger model of Qwen2.5-coder were also consider as they are leading models for coding, see the leaderboard [here](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard) <br>
**Why `qwen2.5-coder:7b`:** this model has demonstrated state-of-the-art performance for its size. The critical code generation benchmark for HumanEvl, thi model shows significant improvement over the alternative choice. Resulting in more accurate and logically sound unit test. Both models were tested out of with `qwen2.5-coder:7b` not only created better unit test but also faster.

**Interface choice:**: A simple command-line tool <br>
**Why**: it is lightweight, native and can be easily integrated into larger automated workflow and IDEs. <br>
**Trade-off**: prioritised developer workflow integration and performance over the visual discoverability and potential ease of use that GUI might offer.

### Future improvements

With more time, the tool can evolved into intelligent-assistant.
1. Multiple files instead of running each file one ny one to generate the tests.
2. Full integration to IDE, currently the user have to highlight and run the code. It would be ideal to have it run from the menu or command palette.
3. Performance - currently the tol waits for the entire test file to be generated before displaying it. For complex test, this can be slow (encountered during testing). Perhaps having stream can generate test code token-by-token, for immediate feedback and potential increase in the performance.