set -eu

if [ $# != 3 ]; then
    echo Invalid Parameter: $*
    echo "param1 : initial test case number. Eg.) 1"
    echo "param2 : final test case number. Eg.) 7"
    echo "param3 : username"
    exit 1
fi
TEST_CASE_INITIAL=$1
TEST_CASE_FINAL=$2
USER_NAME=$3

for i in $(seq ${TEST_CASE_INITIAL} ${TEST_CASE_FINAL}) ; do
    echo "test case${i} ... running"
    # 入力の生成
    python ../generateRandomInput.py cond_${i}.txt format_${i}.txt res_${i}.txt $USER_NAME
    echo "OK"
done
echo "All Test Done"