import { useEffect, useRef, useState } from "react";
import "./index.css";
import { Oval,Comment } from 'react-loader-spinner'

export default function App() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [caption, setCaption] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [backendReady, setBackendReady] = useState(false);
  const [backendLoading, setBackendLoading] = useState(true);
  const [backendError, setBackendError] = useState("");
  const intervalRef = useRef(null);

  const startHealthPolling = () => {
    setBackendLoading(true);
    setBackendError("");
    setBackendReady(false);

    let attempts = 0;
    const MAX_ATTEMPTS = 30;

    if (intervalRef.current) {
      clearInterval(intervalRef.current);
    }

    intervalRef.current = setInterval(async () => {
      attempts++;

      try {
        const res = await fetch("http://127.0.0.1:8000/health");
        const data = await res.json();

        if (data.ready) {
          setBackendReady(true);
          setBackendLoading(false);

          clearInterval(intervalRef.current);
          intervalRef.current = null;
          return;
        }

        if (data.error) {
          setBackendLoading(false);
          setBackendError(data.error);

          clearInterval(intervalRef.current);
          intervalRef.current = null;
          return;
        }

        if (attempts >= MAX_ATTEMPTS) {
          setBackendLoading(false);
          setBackendError("Backend startup timeout");

          clearInterval(intervalRef.current);
          intervalRef.current = null;
        }
      } catch (err) {
        if (attempts >= MAX_ATTEMPTS) {
          setBackendLoading(false);
          setBackendError("Cannot connect to backend");

          clearInterval(intervalRef.current);
          intervalRef.current = null;
        }
      }
    }, 2000);
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;
    setImage(file);
    setPreview(URL.createObjectURL(file));
    setCaption("");
    setError("");
  };

  const handleSubmit = async () => {
    if (!image || !backendReady) return;

    setLoading(true);
    setError("");
    setCaption("");

    const formData = new FormData();
    formData.append("file", image);

    // Timeout controller (30s)
    const controller = new AbortController();
    const timeout = setTimeout(() => {
      controller.abort();
    }, 30000);

    try {
      const res = await fetch("http://127.0.0.1:8000/caption", {
        method: "POST",
        body: formData,
        signal: controller.signal,
      });

      clearTimeout(timeout);

      if (!res.ok) {
        throw new Error("Server error");
      }

      const data = await res.json();
      setCaption(data.caption);
    } catch (err) {
      if (err.name === "AbortError") {
        setError("Server is taking too long (maybe starting up). Try again.");
      } else {
        setError("Cannot connect to backend.");
      }
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    startHealthPolling();

    return () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
    };
  }, []);

  if (backendLoading) {
    return (
      <div className="container">
        <Comment
visible={true}
height="80"
width="80"
ariaLabel="comment-loading"
wrapperStyle={{}}
wrapperClass="comment-wrapper"
color="#fff"
backgroundColor="#4f46e5"
/>
      </div>
    );
  }

  if (backendError) {
    return (
      <div className="container">
        <div className="card">
          <h2>Backend Error</h2>
          <p>{backendError}</p>
          <button onClick={() => handleRetry} className="errb btn">
            Retry
          </button>
        </div>
      </div>
    );
  }

  const handleRetry = () => {
    startHealthPolling();
  };

  return (
    <div className="container">
      <div className="card">
        <h1>Image Captioning</h1>
        <p className="subtitle">Upload an image and AI will describe it</p>

        <label className="upload-box">
          <input type="file" accept="image/*" onChange={handleFileChange} />
          <span>{image ? "Change Image" : "Click to Upload"}</span>
        </label>

        {preview && (
          <div className="preview">
            <img src={preview} alt="Preview" />
          </div>
        )}

        <button
          className="btn"
          onClick={handleSubmit}
          disabled={!image || loading}
        >
          
         {loading ? (
  <div className="bb">
    <Oval
      visible={true}
      height={20}
      width={20}
      ariaLabel="comment-loading"
      wrapperClass="comment-wrapper"
      color="#fff"
      secondaryColor="#fff"
      strokeWidth={4}
      strokeWidthSecondary={4}
    />
    <span>Processing...</span>
  </div>
) : (
  "Generate Caption"
)}
        </button>

        {caption && (
          <div className="caption-box">
            <strong>Caption</strong>
            <p>{caption}</p>
          </div>
        )}
{ ! backendReady &&      <p className="note">First request may take time as server wakes up.</p>}
        {error && <p className="error">{error}</p>}
      </div>
    </div>
  );
}
