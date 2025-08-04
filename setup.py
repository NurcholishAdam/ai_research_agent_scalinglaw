#!/usr/bin/env python3
"""
Setup script for AI Research Agent
Helps configure the environment and dependencies
"""

import os
import subprocess
import sys

def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def check_environment():
    """Check environment variables"""
    print("\n🔧 Checking environment configuration...")
    
    required_vars = ["GROQ_API_KEY"]
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
        else:
            print(f"✅ {var} is set")
    
    if missing_vars:
        print(f"\n⚠️  Missing environment variables: {', '.join(missing_vars)}")
        print("\nTo set them:")
        for var in missing_vars:
            if var == "GROQ_API_KEY":
                print(f"export {var}='your_groq_api_key_here'")
        print("\nOr create a .env file with these variables")
        return False
    
    return True

def create_env_template():
    """Create a .env template file"""
    env_template = """# AI Research Agent Environment Variables
# Copy this file to .env and fill in your actual API keys

# Groq API Key (required)
# Get from: https://console.groq.com/keys
GROQ_API_KEY=your_groq_api_key_here

# Optional: Mistral API Key
# Get from: https://console.mistral.ai/
MISTRAL_API_KEY=your_mistral_api_key_here

# Optional: OpenAI API Key (for embeddings)
# Get from: https://platform.openai.com/api-keys
OPENAI_API_KEY=your_openai_api_key_here
"""
    
    try:
        with open(".env.template", "w") as f:
            f.write(env_template)
        print("✅ Created .env.template file")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env.template: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 AI Research Agent Setup")
    print("=" * 40)
    
    # Install requirements
    if not install_requirements():
        print("Setup failed at requirements installation")
        return
    
    # Check environment
    env_ok = check_environment()
    
    # Create env template
    create_env_template()
    
    print("\n" + "=" * 40)
    if env_ok:
        print("🎉 Setup completed successfully!")
        print("\nNext steps:")
        print("1. Run 'python test_agent.py' to test the agent")
        print("2. Run 'python main.py' to start researching")
    else:
        print("⚠️  Setup completed with warnings")
        print("Please set the required environment variables before running the agent")
        print("See .env.template for guidance")

if __name__ == "__main__":
    main()