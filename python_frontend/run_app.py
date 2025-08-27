import threading
import webview
import app  # This imports your Flask app from app.py

def start_flask():
    app.app.run()

if __name__ == '__main__':
    threading.Thread(target=start_flask, daemon=True).start()
    webview.create_window('Live insights', 'https://ai-interview-416w.onrender.com')
