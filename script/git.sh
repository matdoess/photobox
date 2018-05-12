#!/bin/bash

echo "Bitte Kommentar zu den Änderungen eingeben"
read comment
git add -A
git commit -m "$comment"
git push
read -p "Press enter to quit"
