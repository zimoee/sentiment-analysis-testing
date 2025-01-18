from textblob import TextBlob

def analyze_text(text):
    blob = TextBlob(text)
    subjectivity = blob.sentiment.subjectivity
    polarity = blob.sentiment.polarity
    return subjectivity, polarity

if __name__ == "__main__":
    text = input("Enter text to analyze: ")
    subjectivity, polarity = analyze_text(text)
    print(f"Subjectivity: {subjectivity}")
    print(f"Polarity: {polarity}")