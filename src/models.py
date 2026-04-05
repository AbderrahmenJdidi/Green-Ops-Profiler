import torch
import torchvision.models as models

def get_model(model_name):
    """
    Factory function to load models.
    """
    registry = {
        "resnet18": models.resnet18,
        "resnet50": models.resnet50,
        "mobilenet_v2": models.mobilenet_v2,
        "vit_b_16": models.vit_b_16,
    }
    
    if model_name not in registry:
        raise ValueError(f"Model {model_name} not found in registry.")
    
    return registry[model_name](weights="DEFAULT")

def get_dummy_input(model_name, device="cpu"):
    """
    Generates standard input tensors. 
    ViT often requires 224x224, but you can scale this for your PFE tests.
    """
    size = 224 # Standard ImageNet size
    return torch.randn(1, 3, size, size).to(device)