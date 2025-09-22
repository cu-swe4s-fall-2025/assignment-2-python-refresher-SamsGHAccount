
echo "Running starts here, should return one array of integers, a file error, and then an integer error."
python print_fires.py --file Agrofood_co2_emission.csv --country "United States of America" --county_column 0 --return_col 3
python print_fires.py --file not_a_file.csv --country "United States of America" --county_column 0 --return_col 3
python print_fires.py --file Agrofood_co2_emission.csv --country "United States of America" --county_column 0 --return_col 0
echo "Finished running."
