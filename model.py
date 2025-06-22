import torch
import torch.nn as nn
from torchvision.utils import save_image
from torchvision import transforms
from PIL import Image
import io

# ---- Generator Definition ----
class Generator(nn.Module):
    def __init__(self, z_dim=100, num_classes=10, img_shape=(1, 28, 28)):
        super(Generator, self).__init__()
        self.label_emb = nn.Embedding(num_classes, num_classes)
        input_dim = z_dim + num_classes
        self.img_shape = img_shape

        self.model = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.ReLU(True),
            nn.Linear(256, 512),
            nn.ReLU(True),
            nn.Linear(512, 1024),
            nn.ReLU(True),
            nn.Linear(1024, int(torch.prod(torch.tensor(img_shape)))),
            nn.Tanh()
        )

    def forward(self, z, labels):
        label_embedding = self.label_emb(labels)
        x = torch.cat((z, label_embedding), dim=1)
        img = self.model(x)
        return img.view(img.size(0), *self.img_shape)

# ---- Image Generator Function ----
def generate_digit_images(digit, z_dim=100, num_images=5):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Initialize the generator and load weights
    generator = Generator(z_dim=z_dim).to(device)
    generator.load_state_dict(torch.load("generator.pth", map_location=device))
    generator.eval()

    # Prepare input noise and labels
    z = torch.randn(num_images, z_dim).to(device)
    labels = torch.full((num_images,), digit, dtype=torch.long).to(device)

    with torch.no_grad():
        generated = generator(z, labels)
        generated = (generated + 1) / 2  # Rescale from [-1, 1] to [0, 1]

    # Convert to PIL Images
    images = []
    for img_tensor in generated:
        img = transforms.ToPILImage()(img_tensor.cpu())
        images.append(img)

    return images
