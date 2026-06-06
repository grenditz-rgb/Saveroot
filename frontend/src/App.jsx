import { useState } from "react"

function App() {
  const [url, setUrl] = useState("")
  const [videoInfo, setVideoInfo] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  const fetchInfo = async () => {
    setLoading(true)
    setError("")
    setVideoInfo(null)

    try {
      const response = await fetch("http://127.0.0.1:8000/info", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      })

      if (!response.ok) throw new Error("Failed to fetch video info")

      const data = await response.json()
      setVideoInfo(data)
    } catch (err) {
      setError("Something went wrong. Check the URL and try again.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <h1>SaveRoot</h1>
      <p>Download YouTube videos with ease</p>

      <div className="input-group">
        <input
          type="text"
          placeholder="Paste YouTube URL here..."
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button onClick={fetchInfo} disabled={loading}>
          {loading ? "Fetching..." : "Fetch"}
        </button>
      </div>

      {error && <p className="error">{error}</p>}

      {videoInfo && (
        <div className="video-info">
          {videoInfo.thumbnail && (
            <img src={videoInfo.thumbnail} alt={videoInfo.title} />
          )}
          <h2>{videoInfo.title}</h2>
          <p>{Math.floor(videoInfo.duration / 60)}:{String(videoInfo.duration % 60).padStart(2, "0")}</p>
        </div>
      )}
    </div>
  )
}

export default App