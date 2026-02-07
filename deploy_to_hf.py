    api = HfApi(token=HF_TOKEN)
    
    # Create space if it doesn't exist
    try:
        print("📝 Creating space...")
        create_repo(
            repo_id=SPACE_REPO,
            repo_type="space",
            space_sdk="gradio",
            token=HF_TOKEN,
            exist_ok=True
        )
        print(f"✅ Space created/verified: https://huggingface.co/spaces/{SPACE_REPO}")
    except Exception as e:
        print(f"⚠️ Space might already exist: {e}")
    
    # Create README with metadata
    readme_content = """---
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
"""
    
    # Upload files
    files_to_upload = [
        "app.py",
        "requirements.txt",
        "index.html",
        "earth_temp_graph.png",
        "heat_earth.png"
    ]
    
    # Write README to temp file
    with open("README_HF.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print("⬆️ Uploading files to Hugging Face Spaces...")
    
    try:
        # Upload README
        api.upload_file(
            path_or_fileobj="README_HF.md",
            path_in_repo="README.md",
            repo_id=SPACE_REPO,
            repo_type="space",
            token=HF_TOKEN
        )
        print("  ✓ README.md")
        
        # Upload each file
        for filename in files_to_upload:
            if os.path.exists(filename):
                api.upload_file(
                    path_or_fileobj=filename,
                    path_in_repo=filename,
                    repo_id=SPACE_REPO,
                    repo_type="space",
                    token=HF_TOKEN
                )
                print(f"  ✓ {filename}")
            else:
                print(f"  ⚠️ {filename} not found, skipping...")
        
        print("\n✅ Deployment complete!")
        print(f"🌐 Your space is available at: https://huggingface.co/spaces/{SPACE_REPO}")
        print("\nNote: It may take a few minutes for the space to build and become available.")
        
    except Exception as e:
        print(f"❌ Error during upload: {e}")
        raise
    finally:
        # Cleanup
        if os.path.exists("README_HF.md"):
            os.remove("README_HF.md")

if __name__ == "__main__":
    main()
