import urllib.request

# Get input from user
url = input("Enter URL: ")

print(f"\nFetching content from: {url}")

try:
    # Open URL and read content
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        
    print("\nContent:")
    print(content[:500])  # Print first 500 characters
    print("\n... (content truncated)")
    
    print(f"\nTotal content length: {len(content)} characters")
except Exception as e:
    print(f"\nError fetching URL: {e}")
