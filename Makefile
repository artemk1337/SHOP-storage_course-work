BASE_PTH = $(shell pwd)

### NAME ###
PROJECT_NAME = store

### PATHS ###
SRC_DIR		= store
BUILD_DIR	= build
OBJ_DIR		= $(BUILD_DIR)/obj
BIN_DIR		= $(BUILD_DIR)/dist
PORTABLE	= portable
VENV_DIR	= venv
PYTHON_PATH	= $(VENV_DIR)/bin/python

# COLOR CONSTANTS
# https://misc.flogisoft.com/bash/tip_colors_and_formatting
NC		= '\033[0m'
RED		= '\033[31m'
GRN		= '\033[32m'
BLUE	= '\033[34m'
CYAN	= '\033[36m'
IRED	= '\033[91m'
IGRN	= '\033[92m'
IBLUE	= '\033[94m'
ICYAN	= '\033[96m'

FB		= '\033[1m'
FC		= '\033[3m'
FT		= '\033[1;5;7m'


all:
	echo -e "Required section:\n\
	 develop - create environment,  database and prepare configs \n\
	 build - build project into build directory, with configuration file and environment\n\
	 clean - clean all addition file, build directory and output archive file\n\
	 test - run all tests\n\
	 pack - make output archive\n\
	"