#   - Interactive Cyberpunk Art & Audio Gallery

### **Author:** Riyad Moukhliss

## 📌 Project Overview

**PycharmProjectsmy\_gallery** is a Flask-based web application designed for an immersive cyberpunk-themed experience. This project enables users to:
✅ Upload and manage images & audio files.
✅ Apply filters, resize, rotate, and flip images.
✅ Merge and remix audio files with built-in effects.
✅ Use an **Interactive Art Tool** for digital creation.
✅ Explore a cyberpunk-inspired UI with dynamic themes and animations.

---

## 🔥 Features

🎨 **Image Management** - Upload, view, edit (filters, resize, rotate, flip).
🎵 **Audio Processing** - Upload, play, merge, remix with effects.
🖌 **Interactive Art Tool** - Draw with brushes, shapes, and effects.
🌌 **Cyberpunk UI** - Dynamic themes, animated backgrounds, neon effects.
📂 **Database Integration** - SQLite for metadata storage.

---

## ⚡ Installation & Setup

### **🛠 Prerequisites**

Ensure you have the following installed:

- Python **3.7+**
- Flask
- SQLite3
- Required Python libraries

### **📥 Install Required Libraries**

Run the following command:

```sh
pip install flask pillow pydub
```

### **🚀 Running the Application**

1️⃣ Clone or download this repository.
2️⃣ Navigate to the project directory:

```sh
cd PycharmProjectsmy_gallery
```

3️⃣ Run the application:

```sh
python app1.py
```

4️⃣ Open your browser and go to:

```sh
http://127.0.0.1:5000/
```

---

## 📂 Project Structure

```
PycharmProjectsmy_gallery/
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
```

---

## 🎨 How to Use

### 📤 **Upload Files**

➡ Navigate to the **Upload Files** page.
➡ Select an **image** or **audio file**, then submit.
➡ The file is stored and displayed in the gallery.

### 🖼 **Image Editing**

✅ Apply **filters** (grayscale, blur, invert, emboss, contour, sharpen, smooth, edge enhance).
✅ **Resize**, **rotate**, and **flip** images.

### 🎶 **Audio Editing**

🎵 Play, merge, and remix audio.
🎵 Apply effects (**speed up, slow down, reverb, echo, distortion**).

### 🖌 **Interactive Art Tool**

🎨 Draw using brushes and shapes.
🎨 Choose background effects (**rain, glitch, neon grid, scanlines, none**).
🎨 Save your artwork as an image.

---

## ⚠️ Notes

📌 **Audio files** must be in `.mp3` or `.wav` format.
📌 **Image files** should be in `.png`, `.jpg`, `.jpeg`, or `.gif` format.
📌 The **database (****`database1.db`****)** stores metadata, not actual files.

---

## 🎯 Future Improvements

🔹 **User authentication** for file management.
🔹 **Support for more file formats** (video, 3D models).
🔹 **AI-powered art generator** for digital creations.

---

💾 **Enjoy your Cyberpunk Art & Audio Gallery Experience!** 🚀

