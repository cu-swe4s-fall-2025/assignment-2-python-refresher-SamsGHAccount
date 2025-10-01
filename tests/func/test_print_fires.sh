set -u

test -e ssshtest || curl -s -O https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# Retrieves the file
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PRINT_FIRES_PY="${SCRIPT_DIR}/../../print_fires.py"

if [[ "${PRINT_FIRES_PY_OVERRIDE:-}" != "" ]]; then
  PRINT_FIRES_PY="${PRINT_FIRES_PY_OVERRIDE}"
fi

if [[ ! -f "${PRINT_FIRES_PY}" ]]; then
  echo "Could not find print_fires.py at ${PRINT_FIRES_PY}. Set PRINT_FIRES_PY_OVERRIDE to override."
  exit 1
fi

DATA_DIR="${SCRIPT_DIR}/data"
TEST_DATA="${DATA_DIR}/mini_fires.csv"
mkdir -p "${DATA_DIR}"

# Creates the mandatory data file
cat > "${TEST_DATA}" <<'CSV'
USA,a,10,alpha
USA,b,20.5,beta
Canada,c,5,gamma
USA,d,7,delta
Canada,e,12,epsilon
CSV

# Testing raw
run raw_list python "${PRINT_FIRES_PY}" --file "${TEST_DATA}" --country USA --return_col 2
assert_in_stdout "[10, 20, 7]"
assert_exit_code 0

# Testing mean
run mean_op python "${PRINT_FIRES_PY}" --file "${TEST_DATA}" --country USA --return_col 2 --info_ret mean
assert_in_stdout "12.333333333333334"
assert_exit_code 0

# Testing median
run median_op python "${PRINT_FIRES_PY}" --file "${TEST_DATA}" --country USA --return_col 2 --info_ret median
assert_in_stdout "10"
assert_exit_code 0

# Testing standard deviation
run stdev_op python "${PRINT_FIRES_PY}" --file "${TEST_DATA}" --country USA --return_col 2 --info_ret stdev
exp_stdev="$(
  python - <<'PY'
vals=[10,20,7]
m=sum(vals)/len(vals)
var=sum((x-m)**2 for x in vals)/len(vals)
print(var**0.5)
PY
)"
run stdev_op python "${PRINT_FIRES_PY}" --file "${TEST_DATA}" --country USA --return_col 2 --info_ret stdev
assert_in_stdout "$exp_stdev"
assert_exit_code 0

# Trying to convert strings into numbers
run non_numeric python "${PRINT_FIRES_PY}" --file "${TEST_DATA}" --country USA --return_col 1
assert_in_stdout "Could not convert values to integers!"
assert_exit_code 0

# Tests if files aren't found
MISSING="${DATA_DIR}/no_such.csv"
abs_missing="$(
  python - <<PY
import os, sys
print(os.path.abspath(sys.argv[1]))
PY
"$MISSING")"

run file_missing python "${PRINT_FIRES_PY}" --file "${MISSING}" --country USA --return_col 2
assert_in_stdout "Could not find file ${abs_missing}"
assert_exit_code 0

# Argparse error
run argparse_error python "${PRINT_FIRES_PY}" --file "${TEST_DATA}" --return_col 2
assert_exit_code 2