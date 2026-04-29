#!/bin/bash

FILE_PATH=$1

TAG=$(dirname "$FILE_PATH")
FILENAME=$(basename "$FILE_PATH")

RAW_NUM=$(echo "$FILENAME" | cut -d'_' -f1) # e.g., 001
PROBLEM_NUM=$(echo "$RAW_NUM" | sed 's/^0*//') # 1

touch "$FILE_PATH"

read -p 'Level(Easy, Medium, Hard): ' level
read -p 'Status(Accepted, Failed): ' status
read -p 'Note(optional): ' note

cat <<EOF > "$FILE_PATH"
"""LeetCode Top 150
Level:
    $level
Status:
    $status
Note:
    $note

$(date)
"""
EOF

if [[ "$status" == "Accepted" ]]; then
    ICON="✅"
elif [[ "$status" == "Failed" ]]; then
    ICON="❌"
else
    ICON="$PROBLEM_NUM"
fi

sed -i '' "s/| $PROBLEM_NUM |/| $ICON |/" README.md

echo "Created $FILE_PATH and updated README"
