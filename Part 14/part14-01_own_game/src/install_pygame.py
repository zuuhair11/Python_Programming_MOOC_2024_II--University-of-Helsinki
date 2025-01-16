import subprocess
import sys

def install(package):
    """Install a Python package using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import pygame
except ImportError:
    print("Pygame is not installed. Installing it now...")
    install("pygame")
    print("Pygame has been installed. You can now run the game.")
