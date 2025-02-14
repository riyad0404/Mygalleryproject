Interactive Cyberpunk Art & Audio Gallery
Author: Riyad Moukhliss / GINF1

Project Overview
The Interactive Cyberpunk Art & Audio Gallery is a Flask-based web application that allows users to:

Upload and manage images and audio files.
Apply filters, resize, rotate, and flip images.
Merge and remix audio files with special effects.
Experience an interactive art tool to create digital artwork.
Explore a cyberpunk-themed UI with animations, themes, and background effects.
Features
Image Management: Upload, view, apply filters, and modify images.
Audio Processing: Upload, play, merge, and remix audio files with special effects.
Interactive Art Tool: Create digital artwork with brushes, shapes, and background effects.
Themed User Interface: Cyberpunk-inspired UI with dynamic themes and neon aesthetics.
Database Support: Stores file metadata in SQLite for better organization.
Installation & Setup
Prerequisites
Ensure you have the following installed:
Python 3.7+
Flask
SQLite3
Required Python libraries
Install Required Libraries
Run the following command to install dependencies:
pip install flask pillow pydub
Running the Application
Clone or download this repository
Navigate to the project directory:
cd my_gallery
Run the application:
python app1.py
Open your web browser and go to:
http://127.0.0.1:5000/
Directory Structure
my_gallery/  
│-- static1/  
│   ├── uploads1/  
│   │   ├── audios1/  
│   │   ├── images1/  
│   ├── styles1.css  
│   ├── cyberpunk-theme.mp3  
│-- templates/  
│   ├── index1.html  
│   ├── gallery1.html  
│   ├── upload1.html  
│   ├── art_tool.html  
│   ├── merge_audios.html  
│-- app1.py  
│-- database1.db  
How to Use the Features
Upload Files
Navigate to the Upload Files page.
Select an image/audio file and submit.
The file is stored and displayed in the gallery.
Image Processing
In the gallery, apply filters such as grayscale, blur, invert, emboss, contour, sharpen, smooth, and edge enhance.
Resize, rotate, and flip images directly.
Audio Processing
Play, merge, and remix audio with effects like speed change, echo, reverb, slow down, and distortion.
Interactive Art Tool
Draw using brushes and shapes.
Set different background effects (rain, glitch, neon grid, scanlines, none).
Save your artwork as an image.
Notes
Audio files must be in .mp3 or .wav format.
Images should be in .png, .jpg, .jpeg, or .gif format.
The database (database1.db) stores file metadata but does not store the actual files.
Future Improvements
Add user authentication for file management.
Support more file formats and advanced audio mixing.
Implement an AI-powered art generator for dynamic designs.
✨ Enjoy your cyberpunk art experience!






