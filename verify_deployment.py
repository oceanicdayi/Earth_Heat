#!/usr/bin/env python3
"""
Pre-deployment verification script
Checks that all necessary files are present and valid before deployment
"""
import os
import sys

def check_file_exists(filename, required=True):
    """Check if a file exists"""
    exists = os.path.exists(filename)
    status = "✅" if exists else ("❌" if required else "⚠️")
    size = ""
    if exists:
        size_bytes = os.path.getsize(filename)
        if size_bytes > 1024 * 1024:
            size = f" ({size_bytes / 1024 / 1024:.2f} MB)"
        elif size_bytes > 1024:
            size = f" ({size_bytes / 1024:.2f} KB)"
        else:
            size = f" ({size_bytes} bytes)"
    print(f"{status} {filename}{size}")
    return exists

def main():
    print("🔍 Pre-Deployment Verification for Hugging Face Spaces\n")
    
    print("📦 Core Application Files:")
    errors = 0
    
    # Required files
    required_files = [
        "app.py",
        "requirements.txt",
        "index.html",
    ]
    
    for file in required_files:
        if not check_file_exists(file, required=True):
            errors += 1
    
    print("\n🖼️ Image Resources:")
    # Image files (nice to have but not critical)
    image_files = [
        "earth_temp_graph.png",
        "heat_earth.png",
    ]
    
    for file in image_files:
        check_file_exists(file, required=False)
    
    print("\n📚 Documentation:")
    doc_files = [
        "DEPLOYMENT.md",
        "DEPLOYMENT_SUMMARY.md",
        "QUICKSTART.md",
        "README_HUGGINGFACE.md",
    ]
    
    for file in doc_files:
        check_file_exists(file, required=False)
    
    print("\n🚀 Deployment Scripts:")
    script_files = [
        "deploy_to_hf.py",
        "deploy_to_hf.sh",
    ]
    
    for file in script_files:
        exists = check_file_exists(file, required=False)
        if exists and file.endswith('.sh'):
            # Check if executable
            is_executable = os.access(file, os.X_OK)
            if not is_executable:
                print(f"   ⚠️ {file} is not executable. Run: chmod +x {file}")
    
    print("\n🔍 Content Validation:")
    
    # Validate app.py
    try:
        with open("app.py", "r") as f:
            app_content = f.read()
            if "import gradio" in app_content and "index.html" in app_content:
                print("✅ app.py contains required imports and HTML loading")
            else:
                print("⚠️ app.py might be missing required code")
                errors += 1
    except Exception as e:
        print(f"❌ Error reading app.py: {e}")
        errors += 1
    
    # Validate requirements.txt
    try:
        with open("requirements.txt", "r") as f:
            reqs = f.read().strip()
            if "gradio" in reqs:
                print(f"✅ requirements.txt specifies Gradio: {reqs}")
            else:
                print("❌ requirements.txt missing Gradio dependency")
                errors += 1
    except Exception as e:
        print(f"❌ Error reading requirements.txt: {e}")
        errors += 1
    
    # Validate index.html
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            html_content = f.read()
            if len(html_content) > 10000:  # Should be a substantial HTML file
                print(f"✅ index.html loaded: {len(html_content)} characters")
            else:
                print(f"⚠️ index.html seems too small: {len(html_content)} characters")
    except Exception as e:
        print(f"❌ Error reading index.html: {e}")
        errors += 1
    
    print("\n" + "="*60)
    
    if errors > 0:
        print(f"\n❌ Verification failed with {errors} error(s)")
        print("Please fix the issues above before deploying.\n")
        sys.exit(1)
    else:
        print("\n✅ All checks passed! Ready to deploy to Hugging Face Spaces")
        print("\n🚀 To deploy, run:")
        print("   python deploy_to_hf.py")
        print("\nOr visit the documentation:")
        print("   - QUICKSTART.md for quick deployment")
        print("   - DEPLOYMENT.md for detailed options")
        print("   - DEPLOYMENT_SUMMARY.md for complete overview\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
