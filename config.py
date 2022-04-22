import torch
from torchvision import transforms

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
#paths and sets for the data
TRAIN_DIR = r'C:\Users\dell\Desktop\safe'
TRAIN_LIST = ["set00" , 'set01' , 'set02' , 'set06' , 'set07']
TEST_LIST = ["set08"]
VAL_DIR = r'C:\Users\dell\Desktop\safe'
#the list of models implemented.
MODEL_LIST = ["ResUnet", "Unet"]
#choosing the model to train.
MODEL = MODEL_LIST[0]
#hyper-parameters
LEARNING_RATE = 2e-4
BATCH_SIZE = 32
#the number of images saved by save_some_images
EVAL_BATCH_SIZE = 16
#the ressources allocated to loading the data
NUM_WORKERS = 2
IMAGE_SIZE = 256
#when true, initializes the wieghts with a normal distro with mean 0 and std 0.02 (paper values) if False random Init
INIT_WEIGHTS = True
CHANNELS_IMG = 3
L1_LAMBDA = 4
NUM_EPOCHS = 30
#when true loads the models saved as "disc.pth.tar" and "gen.pth.tar", they need to be in ./
LOAD_MODEL = False
#when true saves a checkpoint every 5 epochs
SAVE_MODEL = True
#the names of the checkpoints
CHECKPOINT_DISC = "disc.pth.tar"
CHECKPOINT_GEN = "gen.pth.tar"

#the data pre-processing used.
transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
