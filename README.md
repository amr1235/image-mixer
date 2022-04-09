# Magnitude & phase Mixer

A piece of software that explains the relative importance of the magnitude and phase components. We will do this task on a 2D signal (i.e. image) just for clarity but the same concept applies to any signal. Our software have the following features:

Ability to open and show two images. For each image, the software have two displays (one fixed display for the image, while the second display can show several components based on a combo-box/drop-menu selection of 1) FT Magnitude, 2) FT Phase, 3) FT Real component, 4) FT Imaginary component.

A mixing panel where an output will be formed based on the mix of two components. Each one of these components determined from:
which image (via a combo or drop-menu). Available images are image 1, and image 2.
Which component of the image FT (via a combo or drop-menu). Available components are: Magnitude, Phase, Real, Imaginary, uniform magnitude (i.e. all magnitude values are set to 1), uniform phase (i.e. all phase values are set to 0).

the mixing ratio (via a slider ranging from 0 to 100%).
Based on the mixing panel, an output image generated and displayed for the user. There are two available displays, each for one output. The mixing panel will be sending the output to either display-Output 1 or 2. The display is determined using a drop-menu in the mixing panel. And the output image will be updated whenever the user makes a change in the mixing options.

# Setup

1. From the command line create a virtual environment and activate.
```sh
# Windows
> python -m venv .venv
> .venv\Scripts\activate

# Linux
> python3 -m venv .venv
> source .venv/bin/activate
```

2. Install dependencies.
```sh
> pip install -r requirements.txt
```

4. Run the application.
```sh
> python UI.py
```
