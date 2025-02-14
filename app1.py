from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from PIL import Image, ImageFilter
from pydub import AudioSegment
from pydub.playback import play
import sqlite3

# Add type hint for 'app'
app: Flask = Flask(__name__, static_folder='static1')

# Configuration
UPLOAD_FOLDER = 'static1/uploads1'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp3', 'wav'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folders exist
os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'images1'), exist_ok=True)
os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'audios1'), exist_ok=True)

# Database setup
def init_db():
    conn = sqlite3.connect('database1.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS files
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, filename TEXT, filetype TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home page
@app.route('/')
def index():
    return render_template('index1.html')

# Upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Check if files were uploaded
        if 'image' not in request.files and 'audio' not in request.files:
            return redirect(request.url)

        # Handle image upload
        if 'image' in request.files:
            image = request.files['image']
            if image and allowed_file(image.filename):
                # Use forward slashes for the file path
                filename = os.path.join('images1', image.filename).replace('\\', '/')
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\', '/')
                image.save(filepath)
                # Save metadata to database
                conn = sqlite3.connect('database1.db')
                c = conn.cursor()
                c.execute("INSERT INTO files (filename, filetype) VALUES (?, ?)", (filename, 'image'))
                conn.commit()
                conn.close()

        # Handle audio upload
        if 'audio' in request.files:
            audio = request.files['audio']
            if audio and allowed_file(audio.filename):
                # Use forward slashes for the file path
                filename = os.path.join('audios1', audio.filename).replace('\\', '/')
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\', '/')
                audio.save(filepath)
                # Save metadata to database
                conn = sqlite3.connect('database1.db')
                c = conn.cursor()
                c.execute("INSERT INTO files (filename, filetype) VALUES (?, ?)", (filename, 'audio'))
                conn.commit()
                conn.close()

        return redirect(url_for('gallery'))

    return render_template('upload1.html')

# Gallery page
@app.route('/gallery')
def gallery():
    # Fetch all files from the database
    conn = sqlite3.connect('database1.db')
    c = conn.cursor()
    c.execute("SELECT * FROM files")
    files = c.fetchall()
    conn.close()

    return render_template('gallery1.html', files=files)

# Apply image filter
@app.route('/apply_filter/<filename>/<filter_name>')
def apply_filter(filename, filter_name):
    # Construct the original image path
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'images1', filename).replace('\\', '/')
    image = Image.open(image_path)

    # Apply selected filter
    if filter_name == 'grayscale':
        image = image.convert('L')
    elif filter_name == 'blur':
        image = image.filter(ImageFilter.BLUR)
    elif filter_name == 'invert':
        image = image.convert('RGB')
        image = Image.eval(image, lambda x: 255 - x)
    elif filter_name == 'contour':
        image = image.filter(ImageFilter.CONTOUR)
    elif filter_name == 'emboss':
        image = image.filter(ImageFilter.EMBOSS)
    elif filter_name == 'sharpen':
        image = image.filter(ImageFilter.SHARPEN)
    elif filter_name == 'smooth':
        image = image.filter(ImageFilter.SMOOTH)
    elif filter_name == 'edge_enhance':
        image = image.filter(ImageFilter.EDGE_ENHANCE)

    # Save the filtered image with a new filename
    filtered_filename = f"filtered_{filter_name}_{filename}"
    filtered_path = os.path.join(app.config['UPLOAD_FOLDER'], 'images1', filtered_filename).replace('\\', '/')
    image.save(filtered_path)

    # Save metadata to database
    conn = sqlite3.connect('database1.db')
    c = conn.cursor()
    c.execute("INSERT INTO files (filename, filetype) VALUES (?, ?)", (filtered_path, 'image'))
    conn.commit()
    conn.close()

    return redirect(url_for('gallery'))

# Play audio
@app.route('/play_audio/<filename>')
def play_audio(filename):
    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], 'audios1', filename)
    audio = AudioSegment.from_file(audio_path)
    play(audio)
    return redirect(url_for('gallery'))

# Delete item
@app.route('/delete/<int:file_id>')
def delete(file_id):
    conn = sqlite3.connect('database1.db')
    c = conn.cursor()
    c.execute("SELECT filename FROM files WHERE id = ?", (file_id,))
    file = c.fetchone()
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file[0]).replace('\\', '/')
        if os.path.exists(file_path):
            os.remove(file_path)  # Delete the file from the folder
        c.execute("DELETE FROM files WHERE id = ?", (file_id,))  # Delete the file metadata from the database
        conn.commit()
    conn.close()
    return redirect(url_for('gallery'))

# Serve uploaded files
@app.route('/uploads1/<filetype>/<filename>')
def uploaded_file(filetype, filename):
    # Construct the correct file path
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filetype, filename).replace('\\', '/')
    return send_from_directory(os.path.dirname(filepath), os.path.basename(filepath))

# Interactive Art Tool
@app.route('/art_tool')
def art_tool():
    return render_template('art_tool.html')
from PIL import ImageOps

# Resize image
@app.route('/resize_image/<filename>/<int:width>/<int:height>')
def resize_image(filename, width, height):
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'images1', filename)
    image = Image.open(image_path)
    resized_image = image.resize((width, height))
    resized_image.save(image_path)
    return redirect(url_for('gallery'))

# Flip image
@app.route('/flip_image/<filename>/<direction>')
def flip_image(filename, direction):
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'images1', filename)
    image = Image.open(image_path)
    if direction == 'horizontal':
        flipped_image = ImageOps.mirror(image)
    elif direction == 'vertical':
        flipped_image = ImageOps.flip(image)
    flipped_image.save(image_path)
    return redirect(url_for('gallery'))

# Rotate image
@app.route('/rotate_image/<filename>/<int:degrees>')
def rotate_image(filename, degrees):
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'images1', filename)
    image = Image.open(image_path)
    rotated_image = image.rotate(degrees)
    rotated_image.save(image_path)
    return redirect(url_for('gallery'))
@app.route('/merge_audios', methods=['GET', 'POST'])
def merge_audios():
    if request.method == 'POST':
        # Get selected audio files
        audio1_id = request.form.get('audio1')
        audio2_id = request.form.get('audio2')

        # Fetch audio file paths from the database
        conn = sqlite3.connect('database1.db')
        c = conn.cursor()
        c.execute("SELECT filename FROM files WHERE id = ?", (audio1_id,))
        audio1_path = os.path.join(app.config['UPLOAD_FOLDER'], c.fetchone()[0]).replace('\\', '/')
        c.execute("SELECT filename FROM files WHERE id = ?", (audio2_id,))
        audio2_path = os.path.join(app.config['UPLOAD_FOLDER'], c.fetchone()[0]).replace('\\', '/')
        conn.close()

        # Debugging: Print the paths of the selected audios
        print(f"Audio 1 Path: {audio1_path}")
        print(f"Audio 2 Path: {audio2_path}")

        # Load audio files
        try:
            audio1 = AudioSegment.from_file(audio1_path)
            audio2 = AudioSegment.from_file(audio2_path)

            # Debugging: Print the duration of the selected audios
            print(f"Audio 1 Duration: {len(audio1) / 1000} seconds")
            print(f"Audio 2 Duration: {len(audio2) / 1000} seconds")

            # Add a 0.5-second delay (500 milliseconds) between the two audios
            silence = AudioSegment.silent(duration=500)  # 0.5-second silence
            merged_audio = audio1 + silence + audio2

            # Debugging: Print the duration of the merged audio
            print(f"Merged Audio Duration: {len(merged_audio) / 1000} seconds")

            # Save the merged audio
            merged_filename = f"merged_{os.path.basename(audio1_path)}_{os.path.basename(audio2_path)}.mp3"
            merged_path = os.path.join(app.config['UPLOAD_FOLDER'], 'audios1', merged_filename).replace('\\', '/')
            merged_audio.export(merged_path, format="mp3")

            # Debugging: Print the path of the merged audio
            print(f"Merged Audio Saved To: {merged_path}")

            # Save metadata to database
            conn = sqlite3.connect('database1.db')
            c = conn.cursor()
            c.execute("INSERT INTO files (filename, filetype) VALUES (?, ?)", (merged_path, 'audio'))
            conn.commit()
            conn.close()

            return redirect(url_for('gallery'))
        except Exception as e:
            # Debugging: Print any errors that occur
            print(f"Error merging audios: {e}")
            return "An error occurred while merging the audios. Please check the logs."

    # Fetch all audio files from the database
    conn = sqlite3.connect('database1.db')
    c = conn.cursor()
    c.execute("SELECT id, filename FROM files WHERE filetype = 'audio'")
    audio_files = c.fetchall()
    conn.close()

    return render_template('merge_audios.html', audio_files=audio_files)


from pydub.effects import speedup
import soundfile as sf
import numpy as np


@app.route('/remix_audio/<filename>/<effect>')
def remix_audio(filename, effect):
    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], 'audios1', filename)
    if not os.path.exists(audio_path):
        return "Error: File not found."

    try:
        audio = AudioSegment.from_file(audio_path)

        if effect == "speed_up":
            from pydub.effects import speedup
            audio = speedup(audio, playback_speed=1.5)
        elif effect == 'slow_down':
            factor = 0.5  # Slow down to 50% speed
            audio = audio._spawn(audio.raw_data, overrides={"frame_rate": int(audio.frame_rate * factor)})
            audio = audio.set_frame_rate(audio.frame_rate)  # Maintain compatibility




        elif effect == "reverb":
            audio = audio + AudioSegment.silent(duration=500)  # Simple reverb effect
        elif effect == "echo":
            import numpy as np

            samples = np.array(audio.get_array_of_samples(), dtype=np.float32)

            delay_ms = 300  # Echo delay in milliseconds
            decay = 0.6  # How much the echo fades

            # Convert delay time from ms to number of samples
            delay_samples = int((delay_ms / 1000.0) * audio.frame_rate)

            # Ensure delay_samples does not exceed the buffer length
            if delay_samples >= len(samples):
                print("⚠️ Delay time too long, reducing delay.")
                delay_samples = len(samples) // 2  # Reduce delay to half buffer size

            echo_signal = np.zeros_like(samples)

            # Apply decay and shift the signal
            echo_signal[delay_samples:] = samples[:-delay_samples] * decay

            # Mix original and echo signals
            output_signal = samples + echo_signal

            # Normalize to prevent clipping
            output_signal = np.int16(output_signal / np.max(np.abs(output_signal)) * np.iinfo(np.int16).max)

            audio = audio._spawn(output_signal.tobytes())

        elif effect == "distortion":
            import numpy as np

            samples = np.array(audio.get_array_of_samples(), dtype=np.float32)

            # 🔥 Distortion intensity (increase for more aggressive distortion)
            gain = 5.0
            threshold = np.iinfo(np.int16).max * 0.7  # Prevents extreme clipping

            # 🔧 Apply gain to make distortion more pronounced
            samples *= gain

            # ✂️ Hard Clipping: Any values above threshold are set to threshold
            samples = np.clip(samples, -threshold, threshold)

            # 🔊 Normalize output back to 16-bit PCM range
            samples = np.int16(samples / np.max(np.abs(samples)) * np.iinfo(np.int16).max)

            audio = audio._spawn(samples.tobytes())

        # Save the remixed audio
        remixed_filename = f"remixed_{effect}_{filename}"
        remixed_path = os.path.join(app.config['UPLOAD_FOLDER'], 'audios1', remixed_filename)
        audio.export(remixed_path, format="mp3")

        # Save to the database
        conn = sqlite3.connect('database1.db')
        c = conn.cursor()
        c.execute("INSERT INTO files (filename, filetype) VALUES (?, ?)", (remixed_filename, 'audio'))
        conn.commit()
        conn.close()

        return redirect(url_for('gallery'))

    except Exception as e:
        return f"Error processing audio: {e}"


if __name__ == '__main__':
    app.run(debug=True)