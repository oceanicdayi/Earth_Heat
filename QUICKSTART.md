# Quick Deploy to Hugging Face Spaces 🚀

## One-Command Deploy

```bash
python deploy_to_hf.py
```

That's it! The script will handle everything automatically.

## What Happens

1. ✅ Installs Hugging Face Hub library (if needed)
2. ✅ Creates/verifies your Space on Hugging Face
3. ✅ Uploads all necessary files (app.py, index.html, images)
4. ✅ Configures metadata and settings
5. ✅ Your app will be live at: https://huggingface.co/spaces/oceanicdayi/Earth_Heat

## Requirements

- Python 3.8+
- Internet connection
- The provided HF token (already configured in the script)

## Alternative: Manual Upload

If the script doesn't work due to network restrictions:

1. Go to https://huggingface.co/new-space
2. Create a Space with:
   - Name: `Earth_Heat`
   - SDK: Gradio
   - License: MIT
3. Upload these files:
   - app.py
   - requirements.txt
   - index.html
   - earth_temp_graph.png
   - heat_earth.png

## Troubleshooting

**"No address associated with hostname" error:**
- This means Hugging Face is blocked in your network
- Try from a different network or use manual upload

**Authentication error:**
- Verify your HF token is correct
- Check token permissions at https://huggingface.co/settings/tokens

## After Deployment

Your Space will take 1-2 minutes to build. You can:
- View build logs in the Space settings
- Share the URL: https://huggingface.co/spaces/oceanicdayi/Earth_Heat
- Embed it in your website

---

For detailed deployment options, see [DEPLOYMENT.md](DEPLOYMENT.md)
