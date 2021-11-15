import os
def main():
    for items in os.listdir('temp'):
        os.remove(f"temp/{items}")
