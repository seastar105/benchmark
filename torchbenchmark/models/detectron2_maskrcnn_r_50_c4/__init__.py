from torchbenchmark.tasks import COMPUTER_VISION
from torchbenchmark.util.framework.detectron2 import Detectron2Model

class Model(Detectron2Model):
    task = COMPUTER_VISION.SEGMENTATION
    DEFAULT_TRAIN_BSIZE = 1
    DEFAULT_EVAL_BSIZE = 2

    def __init__(self, test, device, variant="mask_rcnn_R_50_C4_1x.yaml", jit=False, batch_size=None, extra_args=[]):
        super.__init__(self, test, device, variant, jit, batch_size, extra_args)