Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
=========== RESTART: C:/Users/dhaks/OneDrive/Documents/program011.py ===========
----- ROLE-BASED AND EXAMPLE-BASED PROMPTING -----

ID: T101 | Technique: Zero-Shot
Constructed prompt: You are a Sentiment analyst. Classify review sentiment: The delivery was quick and the product works perfectly.
Python demonstration response: Positive

ID: T102 | Technique: One-Shot
Constructed prompt: You are a Customer feedback analyst. Classify review sentiment. Example: The service was excellent and helpful. -> Positive. New input: The battery stopped working after one day.
Python demonstration response: Negative

ID: T103 | Technique: Few-Shot
Constructed prompt: You are a Product review analyst. Classify review sentiment. Examples: Excellent service -> Positive; Poor quality -> Negative. New input: The camera quality is poor and the screen is dull.
Python demonstration response: Negative

ID: T104 | Technique: Role-Based
Constructed prompt: Act as a Academic writing tutor. Rewrite the sentence professionally: hey, send me the project file now
Python demonstration response: Suggested rewrite: Please share the project file at your earliest convenience.

ID: T105 | Technique: Few-Shot
Constructed prompt: You are a Support analyst. Classify ticket priority. Examples: Excellent service -> Positive; Poor quality -> Negative. New input: The application is unavailable for every user.
Python demonstration response: High

Demonstration completed. Responses use predefined Python rules, not a live LLM.
