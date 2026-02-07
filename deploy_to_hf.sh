#!/bin/bash

# Hugging Face Spaces Deployment Script
# This script deploys the Earth_Heat application to Hugging Face Spaces

set -e

# Configuration
HF_TOKEN="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"
SPACE_NAME="Earth_Heat"
HF_USERNAME="oceanicdayi"  # You may need to update this with your actual HF username
SPACE_URL="https://huggingface.co/spaces/${HF_USERNAME}/${SPACE_NAME}"

echo "🚀 Starting deployment to Hugging Face Spaces..."
echo "Space URL will be: ${SPACE_URL}"

# Install Hugging Face CLI if not already installed
if ! command -v huggingface-cli &> /dev/null; then
    echo "📦 Installing Hugging Face CLI..."
    pip install -q huggingface_hub
fi

# Login to Hugging Face
echo "🔐 Logging in to Hugging Face..."
huggingface-cli login --token "${HF_TOKEN}"

# Check if space exists, if not create it
echo "🔍 Checking if space exists..."
if huggingface-cli repo info "${HF_USERNAME}/${SPACE_NAME}" --repo-type space &> /dev/null; then
    echo "✅ Space already exists: ${SPACE_URL}"
else
    echo "📝 Creating new space..."
    huggingface-cli repo create "${SPACE_NAME}" --type space --space_sdk gradio
fi

# Clone the space repository
echo "📥 Cloning space repository..."
TEMP_DIR=$(mktemp -d)
cd "${TEMP_DIR}"
git clone "https://huggingface.co/spaces/${HF_USERNAME}/${SPACE_NAME}"
cd "${SPACE_NAME}"

# Copy files to the space
echo "📋 Copying files to space..."
cp -v "${OLDPWD}/app.py" .
cp -v "${OLDPWD}/requirements.txt" .
cp -v "${OLDPWD}/index.html" .
cp -v "${OLDPWD}/earth_temp_graph.png" .
cp -v "${OLDPWD}/heat_earth.png" .
cp -v "${OLDPWD}/README.md" ./README_PROJECT.md

# Create README.md with Hugging Face Space metadata
cat > README.md << 'EOF'
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
EOF

# Configure git
git config user.email "github-actions@github.com"
git config user.name "GitHub Actions"

# Add and commit files
echo "💾 Committing changes..."
git add .
git commit -m "Deploy Earth_Heat application to Hugging Face Spaces" || echo "No changes to commit"

# Push to Hugging Face
echo "⬆️ Pushing to Hugging Face Spaces..."
git push "https://oauth:${HF_TOKEN}@huggingface.co/spaces/${HF_USERNAME}/${SPACE_NAME}" main

echo "✅ Deployment complete!"
echo "🌐 Your space is available at: ${SPACE_URL}"
echo ""
echo "Note: It may take a few minutes for the space to build and become available."

# Cleanup
cd -
rm -rf "${TEMP_DIR}"
