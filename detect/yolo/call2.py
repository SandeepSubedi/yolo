def calling():
    import nbformat
    import os
    from nbconvert.preprocessors import ExecutePreprocessor
    filename = '/home/sandeep/Desktop/major/CBIR/detect/yolo/yolov5_detection.ipynb'
    with open(filename) as ff:
        nb_in = nbformat.read(ff, nbformat.NO_CONVERT)
    ep = ExecutePreprocessor()
    nb_out = ep.preprocess(nb_in)


