import { useState } from "react"

function App() {
  const [url, setUrl] = useState("")

  return (
    <div>
      <h1>SaveRoot</h1>
      <p>Download Youtube Videos with ease</p>

      <div className="input-group">
        <input
        type="text"
        placeholder="Paste YouTube URL here..."
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        />  
        <button>Fetch</button>
      </div>
    </div>
  )
}

export default App