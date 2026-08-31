#!/bin/bash
export DIR="$HOME/cv"
up_setup() {
    if [[ ! -d ".venv" ]]; then 
        python3 -m venv .venv
    fi

    source .venv/bin/activate 
    pip install -r requirements.txt --retries=30 1>/dev/null
    python3 cv.py
}

main() {
    cd $DIR
    up_setup
}
main