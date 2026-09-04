# ============================================================
# main.py — Entry point for SignBridge
# Run this file to start the entire system
# It starts the Flask backend server
# Then open frontend/index.html in your browser
# ============================================================

from backend.app import app

if __name__ == "__main__":
    print("=" * 50)
    print("  SignBridge — Sign Language Recognition System")
    print("  Enhancing Accessibility using ML & DL")
    print("=" * 50)
    print("\n  Server starting at: http://localhost:5000")
    print("  Open frontend/index.html in your browser")
    print("  Press Ctrl+C to stop\n")
    # Enable threaded server so streaming and API requests can be handled concurrently
    # debug=False avoids reloader spawning a duplicate process that fights for the camera
    app.run(debug=False, port=5000, threaded=True)