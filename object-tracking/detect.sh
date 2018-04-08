#!/usr/bin/env bash

function detect_dir {
    mkdir predictions
    
    case $1 in
        /*) dir=$1 ;;
        *) dir="../$1"
    esac

    for file in "$dir"/*; do
        echo "FILE $file"
        detect "$file"
        mv predictions.png predictions/$(basename "$file")
    done
}

function detect {
    cp "$file" .
    ./darknet detect cfg/yolov3.cfg yolov3.weights "$file" -thresh 0.5
    rm "$file"
}

if [ "$#" -lt 1 ]; then
    echo "Supply at least one filename."
    exit 1
fi

if [ ! -d darknet ]; then
    echo "Missing darknet, aborting."
    exit 1
fi

if [ -d "$1" ]; then
    pushd darknet
    detect_dir $1
    popd
elif [ -f "$1" ]; then
    pushd darknet
    detect $1
    popd
fi

popd

