#!/usr/bin/bash
set -eu

if [ $# != 3 ]; then
    echo Invalid Parameter: $*
    echo "param1 : atcoder-workspace path. Eg.) /User/yamadataro/atcoder-workspace"
    echo "param2 : target contest name. Eg.) abc123"
    echo "param3 : target problem. Eg.) D"
    exit 1
fi

ATCODER_WORKSPACE_PATH=$1
TARGET_CONTEST_NAME=$2
TARGET_PROBLEM=$3
TARGET_FILE_NAME="main.py"
TARGET_FILE_PATH=$ATCODER_WORKSPACE_PATH"/"$TARGET_CONTEST_NAME"/"$TARGET_PROBLEM"/"$TARGET_FILE_NAME
GREEDY_FILE_NAME="greedy.py"
GREEDY_FILE_PATH=$ATCODER_WORKSPACE_PATH"/"$TARGET_CONTEST_NAME"/"$TARGET_PROBLEM"/"$GREEDY_FILE_NAME
INPUT_FILE_NAME="random_1.txt"
INPUT_FILE_PATH=$ATCODER_WORKSPACE_PATH"/"$TARGET_CONTEST_NAME"/"$TARGET_PROBLEM"/"$INPUT_FILE_NAME
OUTPUT_FILE_GREEDY_NAME="out_expected_1.txt"
OUTPUT_FILE_GREEDY_PATH=$ATCODER_WORKSPACE_PATH"/"$TARGET_CONTEST_NAME"/"$TARGET_PROBLEM"/"$OUTPUT_FILE_GREEDY_NAME
OUTPUT_FILE_TARGET_NAME="out_actual_1.txt"
OUTPUT_FILE_TARGET_PATH=$ATCODER_WORKSPACE_PATH"/"$TARGET_CONTEST_NAME"/"$TARGET_PROBLEM"/"$OUTPUT_FILE_TARGET_PATH
COMPARE_FILE_PATH="compare.py"
TRY_COUNT=3

for i in $(seq 1 ${TRY_COUNT}) ; do
    echo "case${i} ... running"
    # 入出力ファイルの初期化
    cp /dev/null $INPUT_FILE_PATH
    cp /dev/null $OUTPUT_FILE_GREEDY_PATH
    cp /dev/null $OUTPUT_FILE_TARGET_PATH

    # 入力の生成
    python generateRandomInput.py > $INPUT_FILE_PATH

    # 貪欲法解の出力
    python $GREEDY_FILE_PATH < $INPUT_FILE_PATH > $OUTPUT_FILE_GREEDY_PATH

    # 提出解の出力
    python $TARGET_FILE_PATH < $INPUT_FILE_PATH > $OUTPUT_FILE_TARGET_PATH

    # 貪欲法解と提出解の出力差異の検証
    python $COMPARE_FILE_PATH

    echo "OK"
done