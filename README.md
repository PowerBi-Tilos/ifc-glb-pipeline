# IFC to GLB Pipeline with GUIDs + Babylon.js Viewer

Automated pipeline to convert `.ifc` files into `.glb`, embed unique `GlobalId` metadata (GUIDs), and render interactively using Babylon.js — ready to embed in **Power Apps** or any web app.

---

## 🚀 How It Works

1. Drop an `.ifc` file into the `input/` folder (named `model.ifc` for now).
2. GitHub Actions automatically:
   - Runs Blender headlessly
   - Converts IFC → GLB
   - Embeds each object's GUID as metadata
   - Deploys updated `.glb` + viewer to GitHub Pages
3. The Babylon viewer loads the model and lets you:
   - Click objects to get their GUIDs
   - Customize rendering, filtering, metadata links

---

## 🔧 Usage

### 1. Drop an IFC File

- Upload a new file at: `input/model.ifc`

### 2. Wait for GitHub Actions

- A job will run automatically on commit
- Output will appear in: `public/model.glb`

### 3. View the Model

Visit:  
