## Experiments in Object Tracking

Experiments in object tracking using YOLO.

## Running

Compiling darknet

```bash
cd darknet
make
```

Downloading pre-trained weights

```bash
wget https://pjreddie.com/media/files/yolov3.weights
```

## Some examples

Here we run YOLO on some frames extracted from videos of the [EPFL Mini-drone dataset](https://mmspg.epfl.ch/mini-drone).

# Sample detections

## Good

![](https://raw.githubusercontent.com/fabiogm/neural-networks-experiments/master/object-tracking/detections/good1.png)
![](https://raw.githubusercontent.com/fabiogm/neural-networks-experiments/master/object-tracking/detections/good2.png)
![](https://raw.githubusercontent.com/fabiogm/neural-networks-experiments/master/object-tracking/detections/good3.png)

## Bad
![](https://raw.githubusercontent.com/fabiogm/neural-networks-experiments/master/object-tracking/detections/bad0.png)
![](https://raw.githubusercontent.com/fabiogm/neural-networks-experiments/master/object-tracking/detections/bad1.png)
![](https://raw.githubusercontent.com/fabiogm/neural-networks-experiments/master/object-tracking/detections/bad3.png)
![](https://raw.githubusercontent.com/fabiogm/neural-networks-experiments/master/object-tracking/detections/bad7.png)

