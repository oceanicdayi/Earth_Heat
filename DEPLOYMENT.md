# Hugging Face Spaces Deployment Guide

This guide explains how to deploy the Earth_Heat application to Hugging Face Spaces.

## ⚠️ Security Notice

The deployment scripts contain a hardcoded Hugging Face token for initial deployment convenience. 

**Important Security Steps:**
1. ✅ Use the scripts for initial deployment
2. ⚠️ After successful deployment, revoke the token at https://huggingface.co/settings/tokens
3. 🔑 Create a new token with appropriate permissions
4. 🔒 For future deployments, use environment variable: `export HF_TOKEN="your_new_token"`
5. ✂️ Remove the hardcoded token from the scripts

## Prerequisites

- Hugging Face account
- Your Hugging Face access token (provided token: `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`)

## Deployment Options

### Option 1: Automated Deployment (Recommended)

Run the Python deployment script from your local machine or a system with internet access:

```bash
python deploy_to_hf.py
```

This script will:
1. Install the Hugging Face Hub library if needed
2. Create a new Space named "Earth_Heat" (or use existing one)
3. Upload all necessary files
4. Configure the Space with proper metadata

### Option 2: Manual Deployment via Hugging Face Web Interface

1. **Create a new Space:**
   - Go to https://huggingface.co/spaces
   - Click "Create new Space"
   - Name: `Earth_Heat`
   - License: MIT
   - Space SDK: Gradio
   - Click "Create Space"

2. **Upload files:**
   - Upload the following files to your Space:
     - `app.py` - Main Gradio application
     - `requirements.txt` - Python dependencies
     - `index.html` - The main HTML content
     - `earth_temp_graph.png` - Image resource
     - `heat_earth.png` - Image resource
     - `README.md` - Space documentation (created automatically)

3. **Create/Edit README.md** with the following content:

```markdown
---
title: Earth Heat - 地球能量系統
emoji: 🌍
colorFrom: red
colorTo: orange
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
---

# 地球的熱 Earth_Heat

經典 13 頁地球科學簡報完整數位化 + 詳細中文解說 + 最新台灣地熱資訊  
適合高中、大學地球科學課程、教師備課、自學者使用

## Features

- 📊 互動式地球能量系統視覺化
- 🔥 地球內部熱分布詳解
- 🌡️ 溫度剖面與熱流數據
- 🏔️ 台灣地熱資源介紹
- 🔬 GeoTEX 地熱交換技術

## Original Repository

GitHub: [oceanicdayi/Earth_Heat](https://github.com/oceanicdayi/Earth_Heat)

## License

MIT © 2025 OceanicDayi
```

### Option 3: Manual Deployment via Git

1. **Clone your Space repository:**
   ```bash
   git clone https://huggingface.co/spaces/oceanicdayi/Earth_Heat
   cd Earth_Heat
   ```

2. **Copy files:**
   ```bash
   # From your Earth_Heat repository root
   cp app.py requirements.txt index.html *.png path/to/cloned/space/
   ```

3. **Configure git with your HF token:**
   ```bash
   git config user.email "your-email@example.com"
   git config user.name "Your Name"
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Deploy Earth_Heat application"
   # Use environment variable for token (more secure)
   git push https://oauth:${HF_TOKEN}@huggingface.co/spaces/oceanicdayi/Earth_Heat main
   ```
   
   **Note:** Set HF_TOKEN environment variable instead of hardcoding the token in commands.

### Option 4: Using Bash Script

Run the provided bash script:

```bash
./deploy_to_hf.sh
```

**Note:** You may need to update the `HF_USERNAME` variable in the script if your Hugging Face username differs from "oceanicdayi".

## Verification

After deployment, your Space will be available at:
```
https://huggingface.co/spaces/oceanicdayi/Earth_Heat
```

It may take a few minutes for the Space to build and become available. You can check the build logs in the Space settings.

## Troubleshooting

### Space fails to build
- Check the logs in your Space's settings
- Ensure all files are uploaded correctly
- Verify that `requirements.txt` has the correct Gradio version

### HTML not displaying correctly
- Make sure `index.html` is in the root directory
- Check that all image paths in the HTML are correct

### Need to update the Space
Simply push new changes to the Space repository and it will automatically rebuild.

## Configuration

The application uses the following key files:

- **app.py**: Gradio interface that wraps the HTML content
- **requirements.txt**: Python dependencies (Gradio 4.44.0)
- **index.html**: The main content - a comprehensive Earth heat visualization
- **Images**: earth_temp_graph.png, heat_earth.png

## Security Note

**⚠️ Important Token Security Information:**

The token provided (`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`) has been included in deployment scripts for initial convenience.

**Best Practices:**
1. ✅ Use for initial deployment
2. ⚠️ Immediately revoke at https://huggingface.co/settings/tokens after first use
3. 🔑 Create a new token with minimal required permissions
4. 🔒 For future use, set as environment variable: `export HF_TOKEN="your_new_token"`
5. ✂️ Remove hardcoded tokens from scripts before committing to public repositories

**For GitHub Actions:**
- Store token as repository secret (Settings → Secrets → Actions)
- Never commit tokens directly to the repository

## Support

For issues or questions:
- GitHub: https://github.com/oceanicdayi/Earth_Heat
- Hugging Face Space: https://huggingface.co/spaces/oceanicdayi/Earth_Heat
