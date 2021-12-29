for i in $(grep 'tft\[0\]=' *.sh | cut -f2 -d'=' | tr -d '"' | sort -u); do
echo "* $i"
done
