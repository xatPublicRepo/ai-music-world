### **Prerequisites**  
1. **Get API keys** for:  
   - OpenAI (for GPT)  
   - Twitter/X API (to fetch trending hashtags)  
2. **Install required libraries:**  
   ```bash

    python -m venv myenv
    source myenv/bin/activate
    <!-- deactivate venv-->
    deactivate

   pip install openai tweepy
   ```  

### **How It Works**
1. Fetches **top 5 Twitter trending hashtags**.
2. Uses **GPT-4** to generate **song lyrics** based on those hashtags.
3. Prints out the generated lyrics.