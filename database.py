from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.college_chatbot
collection = db.qa


# Define sample data representing intents, questions, and responses
sample_data = [
   
    {
        "intent": "Order Status",
        "questions": [
            "Can you tell me the status of my order?",
            "Where is my order right now?",
            "How can I track my order?"
        ],
        "response": "You can track your order using the tracking number provided in your confirmation email. Simply visit our website's order tracking page and enter the number for the latest updates."
    },
    {
        "intent": "Refund Policy",
        "questions": [
            "How can I get a refund?",
            "What is your refund policy?",
            "Are refunds available for all items?"
        ],
        "response": "Our refund policy allows you to return items within 30 days of purchase if they are in original condition. Once we receive the returned item, refunds will be processed within 5-7 business days. For more details, please visit our refund policy page."
    },
    {
        "intent": "Product Availability",
        "questions": [
            "Is this product in stock?",
            "When will this product be back in stock?",
            "Do you have this item available?"
        ],
        "response": "Product availability can vary. You can check the current stock status directly on the product's page. If an item is out of stock, you can sign up for notifications to be alerted when it becomes available."
    },
    {
        "intent": "Shipping Information",
        "questions": [
            "What are your shipping options?",
            "How long does delivery take?",
            "Do you ship internationally?"
        ],
        "response": "We offer various shipping options, including standard and express delivery. Shipping times depend on your location, with standard delivery taking 5-7 business days and express within 2-3 days. Yes, we do ship internationally, but times may vary."
    },
    {
        "intent": "Returns and Exchanges",
        "questions": [
            "How can I return an item?",
            "What is the process for exchanging a product?",
            "Are there any items that cannot be returned?"
        ],
        "response": "To return an item, please visit our returns page and follow the instructions. For exchanges, you can request a different size or item. Note that personalized or final-sale items may not be eligible for returns or exchanges."
    },
    {
        "intent": "Payment Methods",
        "questions": [
            "What payment methods do you accept?",
            "Can I pay using PayPal?",
            "Do you offer installment payments?"
        ],
        "response": "We accept various payment methods, including credit/debit cards, PayPal, and digital wallets like Apple Pay and Google Pay. Yes, installment payment options are also available through select providers."
    },
    {
        "intent": "Technical Support",
        "questions": [
            "I'm having trouble with the website. Can you help?",
            "Why can't I complete my order?",
            "How do I reset my account password?"
        ],
        "response": "For technical issues, try clearing your browser cache or using a different device. If the problem persists, please contact our support team. To reset your password, click 'Forgot Password' on the login page and follow the instructions."
    },
    {
        "intent": "Product Information",
        "questions": [
            "Can you tell me more about this product?",
            "What are the specifications of this item?",
            "Does this product come with a warranty?"
        ],
        "response": "You can find detailed product information, including specifications and warranty details, on the product's page. If you have specific questions, feel free to ask our support team."
    },
    {
        "intent": "Account Management",
        "questions": [
            "How do I create an account?",
            "Can I update my personal information?",
            "How do I delete my account?"
        ],
        "response": "To create an account, click on 'Sign Up' and fill in your details. You can update your personal information in the 'My Account' section. If you wish to delete your account, please reach out to our support team for assistance."
    },
    
    {
        "intent": "Promotions and Discounts",
        "questions": [
            "Do you have any ongoing promotions?",
            "How can I apply a discount code?",
            "Are there any student discounts?"
        ],
        "response": "We often run promotions and offer discount codes. You can apply a discount code at checkout. We also offer special discounts for students and first-time customers—check our promotions page for the latest deals."
    },
    {
        "intent": "Contact Support",
        "questions": [
            "How can I contact customer support?",
            "Do you have a phone number or email for support?",
            "Is live chat available?"
        ],
        "response": "You can reach our customer support via live chat on our website, email us at support@company.com, or call our helpline. Live chat is available from 9 AM to 8 PM, Monday to Friday."
    },
    {
        "intent": "Store Locations",
        "questions": [
            "Where is your nearest store?",
            "Do you have any physical locations?",
            "Can I pick up an order in-store?"
        ],
        "response": "You can find our store locations on our website under 'Find a Store.' We also offer in-store pickup options for online orders at select locations."
    },
    {
        "intent": "hi",
        "questions": [
            "HI",
            "Hello",
            "Hay"
        ],
        "response": "Hi,How can we help you today?"
    }
]




# Insert sample data into MongoDB collection
collection.insert_many(sample_data)


# Print success message
print("Sample data inserted successfully.")
db.qa.create_index([("questions", "text")])
