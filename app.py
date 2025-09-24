from fastapi import FastAPI, UploadFile, File
from PIL import Image
import torch
from torchvision import transforms
import pickle
from model import EncoderCNN, DecoderRNN

app = FastAPI()

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Params
embed_size = 256
hidden_size = 512

# Load vocab
with open("./models/vocab.pkl", "rb") as f:
    vocab = pickle.load(f)

if not hasattr(vocab, "idx2word"):
    vocab.idx2word = {idx: word for word, idx in vocab.word2idx.items()}

vocab_size = len(vocab)

# Load models
encoder = EncoderCNN(embed_size).to(device)
decoder = DecoderRNN(embed_size, hidden_size, vocab_size).to(device)

encoder.load_state_dict(torch.load("./models/encoder-1.pkl", map_location=device))
decoder.load_state_dict(torch.load("./models/decoder-1.pkl", map_location=device))

encoder.eval()
decoder.eval()

# Transform
transform_test = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), 
                         (0.229, 0.224, 0.225)),
])

def clean_sentence(output, idx2word):
    words = [idx2word[token_id] for token_id in output if token_id in idx2word]
    words = [word for word in words if word not in {"<start>", "<end>"}]
    return " ".join(words)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    image = transform_test(image).unsqueeze(0).to(device)

    with torch.no_grad():
        features = encoder(image).unsqueeze(1)
        output = decoder.sample(features)

    caption = clean_sentence(output, vocab.idx2word)
    return {"caption": caption}
