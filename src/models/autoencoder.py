import torch
import torch.nn as nn
import numpy as np

class Autoencoder(nn.Module):
    def __init__(self, input_dim):
        super(Autoencoder, self).__init__()
        
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 4),
            nn.ReLU(),
            nn.Linear(4, 2)
        )

        self.decoder = nn.Sequential(
            nn.Linear(2, 4),
            nn.ReLU(),
            nn.Linear(4, input_dim)
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded


class AutoencoderModel:
    def __init__(self, input_dim):
        self.model = Autoencoder(input_dim)
        self.criterion = nn.MSELoss()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=0.01)

    def train(self, data, epochs=20):
        data_tensor = torch.tensor(data, dtype=torch.float32)

        for epoch in range(epochs):
            self.optimizer.zero_grad()
            output = self.model(data_tensor)
            loss = self.criterion(output, data_tensor)
            loss.backward()
            self.optimizer.step()

    def get_reconstruction_error(self, data):
        data_tensor = torch.tensor(data, dtype=torch.float32)
        output = self.model(data_tensor)
        
        error = torch.mean((data_tensor - output) ** 2, dim=1)
        
        return error.detach().numpy()