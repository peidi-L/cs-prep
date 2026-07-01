#!/usr/bin/env bash
echo "Hello from demo.sh"
echo "First argument: $1"
echo "Second argument: $2"
echo "Third argument: $3
echo "All arguments: $@"
"echo "Number of arguments: $#"
echo "Looping over arguments:"
for item in "$@"; do
  echo "Argument item: $item"
done
if [[ $# -eq 0 ]]; then
  echo "You gave me no arguments"
else
  echo "You gave me at least one argument"
fi
